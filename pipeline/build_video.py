#!/usr/bin/env python3
"""Video pipeline: script JSON -> German voice (ElevenLabs) -> animated branded slides -> MP4 + AR/EN/DE subtitles.

Runs in GitHub Actions (cloud), controlled by pipeline/run.json (matrix index via VIDEO_INDEX); for local
tests use: python pipeline/build_video.py --script scripts/E/01-berufsbilder.json --no-synthesize --burn
Never prints the API key. Dry-run (no synthesize) uses silent audio and costs nothing.

Motion: every scene is a web page whose animations are driven deterministically
(document.getAnimations -> currentTime). Only frames where something moves are rendered;
static holds are encoded as long frame durations (fast).
"""
import base64
import hashlib
import html as htmlmod
import json
import math
import os
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "out"
CACHE = ROOT / "cache" / "tts"
API = "https://api.elevenlabs.io/v1"
FPS = 30

# Measured boxes inside assets/logo-lockup.png (2400x600): whole logo, bars, wordmark.
LK_IMG_W, LK_IMG_H = 2400, 600
LK_X0, LK_Y0, LK_X1, LK_Y1 = 92, 126, 2250, 557
LK_BARS_X1 = 519
LK_TEXT_X0 = 579


def log(*a):
    print(*a, flush=True)


def sh(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        log("COMMAND FAILED:", " ".join(map(str, cmd))[:300])
        log(r.stderr[-1500:])
        sys.exit(1)
    return r


# ---------------------------------------------------------------- ElevenLabs
def el_headers():
    key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not key:
        log("ERROR: ELEVENLABS_API_KEY is not set (repository secret).")
        sys.exit(1)
    return {"xi-api-key": key}


def el_get(path, params=None):
    import requests
    return requests.get(API + path, headers=el_headers(), params=params, timeout=60)


def subscription_info():
    r = el_get("/user/subscription")
    if r.status_code != 200:
        log(f"subscription: HTTP {r.status_code} (key may lack user_read permission); plan unknown")
        return None
    d = r.json()
    info = {"tier": d.get("tier"), "status": d.get("status"),
            "character_count": d.get("character_count"), "character_limit": d.get("character_limit")}
    log("subscription:", json.dumps(info))
    return info


def list_voices():
    sub = subscription_info()
    out = {"subscription": sub, "voices": [], "shared_de": []}
    r = el_get("/voices")
    if r.status_code == 200:
        for v in r.json().get("voices", []):
            out["voices"].append({
                "name": v.get("name"), "voice_id": v.get("voice_id"), "category": v.get("category"),
                "labels": v.get("labels"), "preview_url": v.get("preview_url"),
                "verified_languages": [x.get("language") for x in (v.get("verified_languages") or [])]})
    else:
        log("voices: HTTP", r.status_code, r.text[:200])
    r = el_get("/shared-voices", {"language": "de", "page_size": 40, "sort": "usage_character_count_7d"})
    if r.status_code == 200:
        for v in r.json().get("voices", []):
            out["shared_de"].append({
                "name": v.get("name"), "voice_id": v.get("voice_id"), "public_owner_id": v.get("public_owner_id"),
                "accent": v.get("accent"), "gender": v.get("gender"), "age": v.get("age"),
                "use_case": v.get("use_case"), "descriptive": v.get("descriptive"),
                "category": v.get("category"), "preview_url": v.get("preview_url")})
    else:
        log("shared-voices: HTTP", r.status_code, r.text[:200])
    OUT.mkdir(exist_ok=True)
    (OUT / "voices.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    log(f"voices: {len(out['voices'])} account voices, {len(out['shared_de'])} shared German voices")
    for v in out["voices"]:
        log("  account:", v["name"], v["voice_id"], v["category"], v["verified_languages"])
    for v in out["shared_de"][:40]:
        log("  shared-de:", v["name"], v["voice_id"], v["accent"], v["gender"], v["use_case"], v["category"])


def tts_key(cfg, voice_id, text, prev_t, next_t):
    return hashlib.sha256(json.dumps(
        [cfg["model_id"], voice_id, cfg["voice_settings"], text, prev_t, next_t],
        sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()


def synth(text, prev_t, next_t, cfg, voice_id):
    import requests
    path = CACHE / f"{tts_key(cfg, voice_id, text, prev_t, next_t)}.mp3"
    if path.exists():
        return path
    body = {"text": text, "model_id": cfg["model_id"], "voice_settings": cfg["voice_settings"]}
    if prev_t:
        body["previous_text"] = prev_t
    if next_t:
        body["next_text"] = next_t
    url = f"{API}/text-to-speech/{voice_id}?output_format=mp3_44100_128"
    for attempt in range(1, 8):
        r = requests.post(url, headers={**el_headers(), "Content-Type": "application/json"},
                          data=json.dumps(body), timeout=180)
        if r.status_code == 200:
            CACHE.mkdir(parents=True, exist_ok=True)
            path.write_bytes(r.content)
            return path
        if r.status_code in (429, 500, 502, 503, 504):
            wait = min(60, 4 * attempt)
            log(f"  TTS HTTP {r.status_code}, retry {attempt} in {wait}s")
            time.sleep(wait)
            continue
        log(f"TTS failed: HTTP {r.status_code}: {r.text[:400]}")
        sys.exit(1)
    log("TTS failed after retries")
    sys.exit(1)


# ---------------------------------------------------------------- media helpers
def duration(path):
    r = sh(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)])
    return float(r.stdout.strip())


def silence(path, seconds):
    sh(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-t", f"{seconds:.3f}", str(path)])


def to_wav(src, dst):
    sh(["ffmpeg", "-y", "-i", str(src), "-ar", "44100", "-ac", "2", str(dst)])


def concat_files(files, dst):
    lst = Path(str(dst) + ".txt")
    lst.write_text("".join(f"file '{Path(f).resolve()}'\n" for f in files), encoding="utf-8")
    sh(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(dst)])
    lst.unlink(missing_ok=True)


# ---------------------------------------------------------------- HTML building blocks
def esc(s):
    return htmlmod.escape(str(s), quote=True)


def data_uri(path):
    return "data:image/png;base64," + base64.b64encode(Path(path).read_bytes()).decode()


CSS = """
:root{--navy:#062B43;--teal:#11BCC4;--mint:#6ADCC6;--terra:#A5573A;--teal-dark:#2D6A6A;--ink:#17323f;--muted:#5b7380}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1920px;height:1080px;overflow:hidden}
body{background:#F9FCFC;color:var(--ink);
 font-family:'Noto Sans','Noto Sans Arabic','DejaVu Sans',sans-serif;position:relative}
.band{position:absolute;left:0;top:0;bottom:0;width:18px;background:linear-gradient(180deg,var(--navy),var(--teal) 55%,var(--mint))}
.lk{position:relative;display:block}
.lk .lb,.lk .lt{position:absolute;top:0;background-image:var(--lk);background-repeat:no-repeat}
.corner{position:absolute;top:40px;right:120px}
.subband{position:absolute;left:18px;right:0;bottom:0;height:206px;background:#EEF6F7;border-top:3px solid var(--mint)}
.subtext{position:absolute;left:18px;right:0;bottom:0;height:206px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;padding:0 120px;z-index:5}
.sa{font-family:'Noto Sans Arabic','Noto Sans',sans-serif;font-weight:700;font-size:56px;line-height:1.3;color:#062B43;text-align:center;direction:rtl;unicode-bidi:plaintext;max-width:1640px;text-wrap:balance}
.se{font-family:'Noto Sans','Noto Sans Arabic',sans-serif;font-size:42px;line-height:1.25;color:#2D6A6A;text-align:center;direction:ltr;max-width:1640px;text-wrap:balance}
.subtext:empty{display:none}
.head{position:absolute;left:120px;top:44px;right:560px;height:200px}
.kicker{font-size:26px;letter-spacing:.14em;text-transform:uppercase;color:var(--terra);font-weight:700;display:flex;align-items:center;gap:16px;height:36px}
.kicker:before{content:"";display:inline-block;width:6px;height:30px;background:var(--terra);border-radius:3px}
h1{font-family:'Noto Serif Display','Noto Serif',serif;font-weight:700;font-size:58px;line-height:1.08;color:var(--navy);margin-top:6px;text-wrap:balance}
h1.long{font-size:48px}
h2{font-size:30px;font-weight:500;color:var(--teal-dark);margin-top:8px;min-height:38px}
.rule{position:absolute;left:0;top:190px;width:220px;height:6px;border-radius:3px;background:var(--terra);transform-origin:left center}
.content{position:absolute;left:120px;right:120px;top:262px;height:430px;display:flex;align-items:center;justify-content:center}
.terms{position:absolute;left:120px;right:120px;top:704px;display:grid;grid-template-columns:repeat(3,1fr);gap:18px;align-items:start}
.chip{background:#fff;border:2px solid var(--teal);border-radius:16px;padding:10px 20px 12px;display:flex;flex-direction:column;gap:2px;box-shadow:0 4px 14px rgba(6,43,67,.07);min-height:132px}
.chip b{font-size:34px;line-height:1.15;color:var(--navy)}
.chip span{font-size:28px;line-height:1.25;color:#0B6E75;display:-webkit-box;-webkit-line-clamp:1;-webkit-box-orient:vertical;overflow:hidden}
.chip.sm b{font-size:30px}.chip.sm span{font-size:24px}.chip.sm i{font-size:21px}
.chip i{font-style:normal;font-size:25px;line-height:1.2;color:#4A5B68;display:-webkit-box;-webkit-line-clamp:1;-webkit-box-orient:vertical;overflow:hidden}
.badge{position:absolute;right:120px;top:150px;background:var(--terra);color:#fff;border-radius:999px;padding:8px 24px;font-size:24px;font-weight:700}
.wm{position:absolute;left:50%;transform:translateX(-50%);top:8px;background:#c0392b;color:#fff;padding:4px 22px;border-radius:0 0 12px 12px;font-size:20px;font-weight:700;letter-spacing:.06em;z-index:99}
.hook{font-family:'Noto Serif Display','Noto Serif',serif;font-size:84px;line-height:1.16;color:var(--navy);text-align:center;max-width:1560px;text-wrap:balance}
body.dark{background:var(--navy)}body.dark .hook{color:#fff}body.dark .head h1,body.dark .kicker{color:#fff}body.dark .kicker:before{background:var(--mint)}
body.dark .rule{background:var(--mint)}body.dark h2{color:var(--mint)}body.dark .corner{background:#fff;border-radius:16px;padding:10px 18px;top:34px;right:100px}body.dark .subband{background:#0B3F61;border-top-color:var(--teal)}body.dark .chip{background:#0B3F61;border-color:var(--teal)}
body.dark .chip b{color:#fff}body.dark .chip span{color:var(--mint)}body.dark .chip i{color:#C9E1EA}
.blocks{display:grid;grid-template-columns:repeat(3,1fr);gap:26px;width:100%}
.blocks.d .bh{padding:14px 24px;font-size:34px}.blocks.d .br{font-size:33px;padding:10px 22px;line-height:1.2;gap:16px}.blocks.d .bn{width:44px;height:44px;font-size:24px}
.blk{background:#fff;border-radius:22px;overflow:hidden;box-shadow:0 10px 30px rgba(6,43,67,.10)}
.blk .bh{padding:18px 24px;font-size:36px;font-weight:700;color:#fff}
.blk.teal .bh{background:var(--teal);color:var(--navy)}.blk.mint .bh{background:var(--mint);color:var(--navy)}.blk.terra .bh{background:var(--terra)}
.blk .br{display:flex;align-items:center;gap:18px;padding:15px 24px;font-size:38px;color:var(--navy);border-bottom:1px solid #e4eef0}
.blk .bn{width:52px;height:52px;border-radius:50%;background:var(--navy);color:#fff;font-weight:700;font-size:28px;display:flex;align-items:center;justify-content:center;flex:none}
ul.b{list-style:none;width:100%;max-width:1500px}
ul.b li{font-size:52px;line-height:1.25;margin:22px 0;padding-left:68px;position:relative;color:var(--ink)}
ul.b li:before{content:"";position:absolute;left:0;top:20px;width:28px;height:28px;border-radius:50%;background:var(--teal);box-shadow:0 0 0 8px rgba(17,188,196,.18)}
ul.b.dense li{font-size:40px;margin:10px 0;padding-left:56px}ul.b.dense li:before{top:12px;width:24px;height:24px}
ul.r li:before{background:var(--mint);box-shadow:0 0 0 8px rgba(106,220,198,.25)}
.cards{display:grid;gap:36px;width:100%}.cards.dense{gap:22px}.cards.dense .card{padding:20px 28px}.cards.dense .card h3{font-size:36px;margin-bottom:6px}.cards.dense .card p{font-size:28px}
.card{background:#fff;border-radius:26px;padding:34px 38px;border-left:12px solid var(--teal);box-shadow:0 10px 30px rgba(6,43,67,.10);position:relative}
.card h3{font-size:44px;color:var(--navy);margin-bottom:12px;font-family:'Noto Serif Display','Noto Serif',serif}
.card p{font-size:34px;line-height:1.3;color:#4A5B68}
.card .tag{position:absolute;top:-16px;right:26px;background:var(--terra);color:#fff;border-radius:999px;padding:4px 18px;font-size:22px;font-weight:700}
.flow{display:flex;flex-direction:column;gap:30px;width:100%;align-items:center}
.row{display:flex;gap:0;align-items:stretch;justify-content:center;width:100%}
.step{background:#fff;border-radius:22px;padding:22px 20px;text-align:center;flex:1;max-width:330px;min-width:0;box-shadow:0 8px 24px rgba(6,43,67,.10);border-top:8px solid var(--teal);display:flex;flex-direction:column;align-items:center;gap:8px;justify-content:center}
.step .n{width:46px;height:46px;border-radius:50%;background:var(--navy);color:#fff;font-weight:700;font-size:26px;display:flex;align-items:center;justify-content:center}
.step .l{font-size:30px;font-weight:700;color:var(--navy);line-height:1.15;word-break:break-word}
.step .l.big{font-size:56px;font-family:'Noto Serif Display','Noto Serif',serif}
.step .s{font-size:22px;color:var(--muted)}
.arrow{width:46px;display:flex;align-items:center;justify-content:center;color:var(--terra);font-size:40px;flex:none}
.flow.s1 .step{max-width:520px;padding:38px 30px;gap:14px}.flow.s1 .l{font-size:46px}.flow.s1 .s{font-size:28px}
.flow.s1 .n{width:64px;height:64px;font-size:36px}.flow.s1 .arrow{width:90px;font-size:60px}.flow.s1 .l.big{font-size:84px}
.flow.s2 .step{max-width:380px;padding:30px 24px}.flow.s2 .l{font-size:30px;word-break:normal;overflow-wrap:normal;hyphens:none}.flow.s2 .s{font-size:24px}.flow.s2 .n{width:54px;height:54px;font-size:30px}.flow.s2 .arrow{width:60px;font-size:48px}
.tree{width:100%;max-width:1400px}.tree.d1 .node{font-size:36px;margin:8px 0}.tree.d2 .node{font-size:31px;margin:3px 0}
.node{font-size:44px;margin:14px 0;color:var(--navy);display:flex;align-items:center;gap:16px}
.node:before{content:"";width:16px;height:16px;border-radius:4px;background:var(--teal);flex:none}
table{border-collapse:separate;border-spacing:0;width:100%;font-size:34px;font-variant-numeric:tabular-nums;background:#fff;border-radius:20px;overflow:hidden;box-shadow:0 10px 30px rgba(6,43,67,.10)}
th{background:var(--navy);color:#fff;text-align:left;padding:16px 20px;font-size:30px}
th.num,td.num{text-align:right}
table.d{font-size:28px}table.d td{padding:8px 18px}table.d th{padding:12px 18px;font-size:26px}table.d tr.total td{font-size:32px}
tr.total td{font-weight:700;font-size:38px;border-top:3px solid var(--navy);background:#EAFBF8}
td{padding:14px 20px;border-bottom:1px solid #e4eef0;vertical-align:top;color:var(--ink)}
tr:nth-child(even) td{background:#f6fbfb}
.cmp{display:grid;grid-template-columns:1fr 1fr;gap:44px;width:100%}
.col{background:#fff;border-radius:26px;padding:34px 40px;box-shadow:0 10px 30px rgba(6,43,67,.10)}
.col:first-child{border-top:10px solid var(--teal)}.col:last-child{border-top:10px solid var(--terra)}
.col h3{font-size:44px;color:var(--navy);margin-bottom:16px;font-family:'Noto Serif Display','Noto Serif',serif}
.col li{font-size:36px;margin:12px 0 12px 26px;color:var(--ink)}
.cmp.d .col{padding:24px 38px}.cmp.d .col h3{font-size:40px;margin-bottom:8px}.cmp.d .col li{font-size:31px;margin:6px 0 6px 26px}
.center{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:30px;text-align:center;padding:0 160px}
.center h1{font-size:70px;margin:0;text-wrap:balance}
.center .sub{font-size:34px;color:var(--teal-dark);max-width:1400px}
.center .ar{font-size:44px;color:var(--navy);direction:rtl}
.disc{position:absolute;left:0;right:0;bottom:46px;text-align:center;font-size:24px;line-height:1.5;color:#4A5B68}
.center .tag{font-size:26px;letter-spacing:.14em;text-transform:uppercase;color:var(--terra);font-weight:700}
.wipe{position:absolute;inset:0;z-index:50}
.w1{background:var(--navy)}.w2{background:var(--teal)}.w3{background:var(--mint)}
"""


def lockup_html(height, extra_cls=""):
    """Wide logo cut out of logo-lockup.png: bars layer + wordmark layer (separately animatable)."""
    s = height / (LK_Y1 - LK_Y0 + 1)
    w = (LK_X1 - LK_X0 + 1) * s
    bg = f"background-size:{LK_IMG_W*s:.2f}px {LK_IMG_H*s:.2f}px;"
    bars_w = (LK_BARS_X1 - LK_X0 + 1) * s
    text_left = (LK_TEXT_X0 - LK_X0) * s
    text_w = (LK_X1 - LK_TEXT_X0 + 1) * s
    return (f'<div class="lk {extra_cls}" style="width:{w:.1f}px;height:{height}px">'
            f'<div class="lb" style="left:0;width:{bars_w:.1f}px;height:{height}px;{bg}'
            f'background-position:{-LK_X0*s:.2f}px {-LK_Y0*s:.2f}px"></div>'
            f'<div class="lt" style="left:{text_left:.1f}px;width:{text_w:.1f}px;height:{height}px;{bg}'
            f'background-position:{-LK_TEXT_X0*s:.2f}px {-LK_Y0*s:.2f}px"></div></div>')


def _chip_width(t, with_en):
    w = 72 + 16.8 * len(t.get("de", "")) + 11.0 * len(t.get("ar", ""))
    if with_en:
        w += 10.0 * len(t.get("en", "")) + 12
    return w


def _rows(widths, avail=1680, gap=14):
    rows, cur = 1, 0.0
    for w in widths:
        if cur and cur + gap + w > avail:
            rows += 1
            cur = w
        else:
            cur = cur + (gap if cur else 0) + w
    return rows


def _short(t, n):
    t = " ".join(str(t).split())
    if len(t) <= n:
        return t
    cut = t[:n].rsplit(" ", 1)[0]
    return cut.rstrip(",;:·/ -(") + "…"


def _short_de(t):
    t = " ".join(str(t).split())
    if len(t) > 28 and " (" in t:
        head = t.split(" (", 1)[0]
        if len(head) >= 3:
            t = head
    return _short(t, 30)


def terms_html(terms):
    if not terms:
        return ""
    ts_ = terms[:3]
    show_en = [True] * len(ts_)
    pass
    out = ['<div class="terms">']
    for i, t in enumerate(ts_):
        de_t, ar_t, en_t = _short_de(t.get("de", "")), _short(t.get("ar", ""), 34), _short(t.get("en", ""), 40)
        en = f'<i>{esc(en_t)}</i>' if show_en[i] else ""
        sm = " sm" if (len(ar_t) > 24 or len(en_t) > 30 or len(de_t) > 22) else ""
        out.append(f'<div class="chip{sm}" data-t="{i}"><b>{esc(de_t)}</b>'
                   f'<span dir="rtl">{esc(ar_t)}</span>{en}</div>')
    out.append("</div>")
    return "".join(out)


_SOL_ROWS = []


def content_html(slide):
    """Returns (html, number_of_revealable_items). Items carry data-it="k"."""
    lay = slide.get("layout", "bullets")
    items = slide.get("items", [])
    if lay == "hook":
        txt = esc(items[0] if items else slide.get("heading", ""))
        return f'<div class="hook" data-it="0">{txt}</div>', 1
    if lay in ("bullets", "recap"):
        its = items[:6]
        cls = ("b r" if lay == "recap" else "b") + (" dense" if len(its) >= 5 else "")
        lis = "".join(f'<li data-it="{k}">{esc(i)}</li>' for k, i in enumerate(its))
        return f'<ul class="{cls}">{lis}</ul>', len(its)
    if lay == "cards":
        its = items[:4]
        cols = len(its) if len(its) <= 3 else 2
        cs = "".join(
            f'<div class="card" data-it="{k}">{"<span class=tag>"+esc(c.get("tag"))+"</span>" if c.get("tag") else ""}'
            f'<h3>{esc(c.get("title",""))}</h3><p>{esc(c.get("body",""))}</p></div>' for k, c in enumerate(its))
        dense = " dense" if len(its) >= 4 else ""
        return f'<div class="cards{dense}" style="grid-template-columns:repeat({max(cols,1)},1fr)">{cs}</div>', len(its)
    if lay == "flow":
        steps = items[:9]
        per = len(steps) if len(steps) <= 5 else math.ceil(len(steps) / 2)
        rows = [steps[i:i + per] for i in range(0, len(steps), per)]
        html_rows, k = [], 0
        for r in rows:
            parts = []
            for j, s in enumerate(r):
                if j > 0:
                    parts.append(f'<div class="arrow" data-it="{k}">&#10140;</div>')
                lab = str(s.get("label", ""))
                badge = "" if lab.strip().isdigit() else f'<div class="n">{k+1}</div>'
                cls = "l big" if lab.strip().isdigit() else "l"
                parts.append(f'<div class="step" data-it="{k}">{badge}'
                             f'<div class="{cls}">{esc(lab)}</div>'
                             + (f'<div class="s">{esc(s.get("sub"))}</div>' if s.get("sub") else "") + "</div>")
                k += 1
            html_rows.append(f'<div class="row">{"".join(parts)}</div>')
        size = 1 if len(steps) <= 3 else (2 if len(steps) <= 5 else 3)
        return f'<div class="flow s{size}">{"".join(html_rows)}</div>', len(steps)
    if lay == "tree":
        its = items[:10]
        ns = "".join(f'<div class="node" data-it="{k}" style="margin-left:{int(n.get("level",0))*56}px">{esc(n.get("label",""))}</div>'
                     for k, n in enumerate(its))
        d = " d2" if len(its) > 7 else (" d1" if len(its) > 5 else "")
        return f'<div class="tree{d}">{ns}</div>', len(its)
    if lay == "table":
        cols = items.get("columns", [])
        rows = items.get("rows", [])[:6]
        isnum = lambda x: bool(re.fullmatch(r"[−\-+]?[\d.,]+\s*(€|m³|m²|t|kg|%)?", str(x).strip()))
        numcols = [j for j in range(len(cols)) if rows and all(isnum(r[j]) for r in rows if j < len(r) and str(r[j]).strip() not in ("", "—"))]
        th = "".join(f'<th class="{"num" if j in numcols else ""}">{esc(c)}</th>' for j, c in enumerate(cols))

        solcols = [j for j, c in enumerate(cols) if str(c).strip().lower() in ("lösung", "loesung", "solution")]

        def tr(k, r):
            total = any(re.search(r"\bsumme\b", str(c).lower()) for c in r)
            tds = "".join(f'<td class="{"num" if j in numcols else ""}"' + (f' data-sol="{k}"' if j in solcols else "") + f'>{esc(c)}</td>'
                          for j, c in enumerate(r))
            return f'<tr data-it="{k}" class="{"total" if total else ""}">{tds}</tr>'
        _SOL_ROWS.append(len(rows) if solcols else 0)
        trs = "".join(tr(k, r) for k, r in enumerate(rows))
        return f'<table class="{"d" if len(rows) >= 6 else ""}"><tr>{th}</tr>{trs}</table>', len(rows)
    if lay == "blocks":
        out = []
        for k, b in enumerate(items[:3]):
            rows = "".join(f'<div class="br"><div class="bn">{esc(r.get("n",""))}</div><div>{esc(r.get("label",""))}</div></div>' for r in b.get("rows", [])[:6])
            out.append(f'<div class="blk {esc(b.get("tone","teal"))}" data-it="{k}"><div class="bh">{esc(b.get("title",""))}</div>{rows}</div>')
        dn = " d" if max((len(b.get("rows", [])) for b in items[:3]), default=0) >= 3 else ""
        return f'<div class="blocks{dn}">{"".join(out)}</div>', len(items[:3])
    if lay == "compare":
        def col(c, k):
            lis = "".join(f"<li>{esc(p)}</li>" for p in c.get("points", [])[:5])
            return f'<div class="col" data-it="{k}"><h3>{esc(c.get("title",""))}</h3><ul>{lis}</ul></div>'
        dn = " d" if max(len(items.get("left", {}).get("points", [])), len(items.get("right", {}).get("points", []))) >= 4 else ""
        return f'<div class="cmp{dn}">{col(items.get("left",{}),0)}{col(items.get("right",{}),1)}</div>', 2
    return "", 0


def wipes_html():
    return '<div class="wipe w1"></div><div class="wipe w2"></div><div class="wipe w3"></div>'


def page_css(lk_uri):
    return f"<style>:root{{--lk:url('{lk_uri}')}}{CSS}</style>"


def scene_page(scene, lk_uri, watermark):
    """Returns (html, n_items, n_terms, kind)."""
    s = scene["slide"]
    wm = f'<div class="wm">{esc(watermark)}</div>' if watermark else ""
    if s.get("layout") == "endcard":
        nxt = esc((s.get("items") or [""])[0])
        return (page_css(lk_uri) + f"<body><div class='band'></div>{wm}"
                f"<div class='center'>{lockup_html(230, 'big')}<h1 id='ec-h'>{esc(s.get('heading',''))}</h1>"
                f"<div class='sub' id='ec-s'>{nxt}</div></div>"
                f"<div class='disc' id='ec-d'>{esc(s.get('stand',''))}<br>Sprecherstimme: KI-generiert · <span dir='rtl'>الصوت مُولَّد بالذكاء الاصطناعي</span> · Narration: AI-generated voice</div>"
                f"<div class='subtext' id='subtext'></div>{wipes_html()}</body>"), 0, 0, "end"
    kicker = f'<div class="kicker">{esc(s["kicker"])}</div>' if s.get("kicker") else ""
    sub = f'<h2>{esc(s["subheading"])}</h2>' if s.get("subheading") else ""
    badge = f'<div class="badge">{esc(s["badge"])}</div>' if s.get("badge") else ""
    _SOL_ROWS.clear()
    body, n_items = content_html(s)
    terms = s.get("terms") or []
    dark = ""
    longcls = " class='long'" if len(s.get("heading", "")) > 34 else ""
    return (page_css(lk_uri) + f"<body{dark}><div class='band'></div>{wm}<div class='subband'></div><div class='subtext' id='subtext'></div>"
            f"<div class='corner'>{lockup_html(76)}</div>"
            f"<div class='head'>{kicker}<h1{longcls}>{esc(s.get('heading',''))}</h1>{sub}<div class='rule'></div></div>{badge}"
            f"<div class='content'>{body}</div>{terms_html(terms)}{wipes_html()}</body>"), n_items, min(len(terms), 3), "scene"


def intro_page(meta, lk_uri, watermark):
    t = meta["title"]
    wm = f'<div class="wm">{esc(watermark)}</div>' if watermark else ""
    return (page_css(lk_uri) + f"<body><div class='band'></div>{wm}<div class='center'>"
            f"{lockup_html(170, 'big')}<div class='tag' id='in-tag'>Deutsch Beruf · Online-Akademie</div>"
            f"<h1 id='in-de'>{esc(t.get('de',''))}</h1><div class='ar' id='in-ar'>{esc(t.get('ar',''))}</div>"
            f"<div class='sub' id='in-en'>{esc(t.get('en',''))}</div></div><div class='subtext' id='subtext'></div></body>")


# ---------------------------------------------------------------- animation specs
EASE = "cubic-bezier(.22,.8,.26,1)"


def fade_up(sel, delay, dur=0.55, dy=34):
    return {"sel": sel, "delay": delay, "dur": dur,
            "kf": [{"opacity": 0, "transform": f"translateY({dy}px)"}, {"opacity": 1, "transform": "translateY(0px)"}]}


def pop(sel, delay, dur=0.5):
    return {"sel": sel, "delay": delay, "dur": dur, "easing": "cubic-bezier(.3,1.5,.5,1)",
            "kf": [{"opacity": 0, "transform": "scale(.6)"}, {"opacity": 1, "transform": "scale(1)"}]}


def slide_in(sel, delay, dur=0.5, dx=-40):
    return {"sel": sel, "delay": delay, "dur": dur,
            "kf": [{"opacity": 0, "transform": f"translateX({dx}px)"}, {"opacity": 1, "transform": "translateX(0px)"}]}


def wipe_events():
    out = []
    for sel, delay in ((".w3", 0.0), (".w2", 0.06), (".w1", 0.12)):
        out.append({"sel": sel, "delay": delay, "dur": 0.4, "easing": "cubic-bezier(.6,0,.3,1)",
                    "kf": [{"clipPath": "inset(0 0 0 0)"}, {"clipPath": "inset(0 0 0 100%)"}]})
    return out


def logo_build(prefix_sel, delay):
    """Bars pop in one after another feeling, then the wordmark is wiped in."""
    return [
        {"sel": f"{prefix_sel} .lb", "delay": delay, "dur": 0.7, "easing": "cubic-bezier(.3,1.4,.5,1)",
         "kf": [{"opacity": 0, "transform": "translateY(60px) scale(.7)"}, {"opacity": 1, "transform": "translateY(0px) scale(1)"}]},
        {"sel": f"{prefix_sel} .lt", "delay": delay + 0.45, "dur": 0.8, "easing": EASE,
         "kf": [{"clipPath": "inset(0 100% 0 0)", "opacity": 0.2}, {"clipPath": "inset(0 0% 0 0)", "opacity": 1}]},
    ]


def reveal_lines(n_items, n_lines):
    """Spoken-line index at which each of n_items appears (first item after the intro line, spread evenly)."""
    if n_items <= 0 or n_lines <= 0:
        return []
    if n_lines > n_items:
        return [1 + j * (n_lines - 1) // n_items for j in range(n_items)]
    return [j * n_lines // n_items for j in range(n_items)]


def scene_events(kind, n_items, n_terms, scene_dur, tail, task_times=None, sol_times=None, line_times=None):
    if kind == "end":
        ev = wipe_events()
        ev += logo_build(".center .lk", 0.7)
        ev += [fade_up("#ec-h", 1.9), fade_up("#ec-s", 2.4), fade_up("#ec-d", 2.9, 0.5, 14)]
        return ev
    ev = wipe_events()
    ev += [slide_in(".head .kicker", 0.35), fade_up(".head h1", 0.4, 0.55), fade_up(".head h2", 0.5),
           {"sel": ".rule", "delay": 0.5, "dur": 0.6, "easing": EASE,
            "kf": [{"transform": "scaleX(0)"}, {"transform": "scaleX(1)"}]},
           {"sel": ".corner", "delay": 0.35, "dur": 0.45,
            "kf": [{"opacity": 0, "transform": "translateY(-16px)"}, {"opacity": 1, "transform": "translateY(0px)"}]},
           pop(".badge", 1.1)]
    t0 = 1.0
    sol_rows = _SOL_ROWS[-1] if _SOL_ROWS else 0
    t1 = max(t0 + 1.0, scene_dur - tail - 1.2)
    # items (then term chips) appear one after another at the start of the spoken line they belong to
    total = n_items + n_terms
    lt = list(line_times or [])
    idx = reveal_lines(total, len(lt)) if lt else []
    for k in range(n_items):
        d = t0 + (t1 - t0) * k / max(n_items, 1)
        if idx:
            d = max(t0, lt[idx[k]] - 0.05)
        if n_items == 1 and not idx:
            d = 0.95
        if sol_rows and task_times and len(task_times) >= n_items:
            d = max(t0, task_times[k] - 0.1)  # exercise rows appear with their Aufgabe line
        ev.append(fade_up(f'[data-it="{k}"]', round(d, 3)))
    for k in range(sol_rows):
        d = t0 + (t1 - t0) * k / max(n_items, 1)
        d = min(d + 5.0, scene_dur - tail - 0.8)
        if sol_times and len(sol_times) >= sol_rows:
            d = sol_times[k] + 0.15  # the solution appears only when the voice reads it (retrieval practice)
        ev.append(fade_up(f'[data-sol="{k}"]', round(d, 3), 0.5, 10))
    for i in range(n_terms):
        d = 1.3 + 0.35 * i
        if idx:
            d = max(t0, lt[idx[n_items + i]] - 0.05)
        ev.append(pop(f'.chip[data-t="{i}"]', round(d, 3)))
    return ev


def intro_events():
    ev = logo_build(".center .lk", 0.15)
    ev += [fade_up("#in-tag", 1.2, 0.45, 20), fade_up("#in-de", 1.5, 0.5), fade_up("#in-ar", 1.9, 0.45), fade_up("#in-en", 2.2, 0.45)]
    return ev


# ---------------------------------------------------------------- rendering
INIT_JS = """(anims) => {
  const all = [];
  for (const a of anims) {
    for (const el of document.querySelectorAll(a.sel)) {
      const an = el.animate(a.kf, {delay: a.delay*1000, duration: a.dur*1000, fill: 'both',
                                   easing: a.easing || 'cubic-bezier(.22,.8,.26,1)'});
      an.pause(); all.push(an);
    }
  }
  window.__A = all;
}"""
SET_JS = "(t) => { for (const an of window.__A) { an.currentTime = t*1000; } }"
SUB_JS = """(h) => { const el = document.getElementById('subtext'); if (el) { el.innerHTML = h; } }"""


def sub_html(c):
    ar, en = c.get("ar"), c.get("en")
    out = ""
    if ar:
        out += f'<div class="sa" dir="rtl">{esc(ar)}</div>'
    if en:
        out += f'<div class="se">{esc(en)}</div>'
    return out


DOM_QA_JS = """() => {
  const issues = []; const W = 1920, H = 1080, SUB_TOP = 872;
  const lum = (c) => { const m = c.match(/rgba?\\((\\d+),\\s*(\\d+),\\s*(\\d+)(?:,\\s*([\\d.]+))?/); if (!m) return null;
    const f = v => { v/=255; return v<=0.03928? v/12.92 : Math.pow((v+0.055)/1.055,2.4); };
    return {l: 0.2126*f(+m[1])+0.7152*f(+m[2])+0.0722*f(+m[3]), a: m[4]===undefined?1:+m[4]}; };
  const bgOf = (e) => { for (let n=e; n; n=n.parentElement) { const c = getComputedStyle(n).backgroundColor; const x = lum(c); if (x && x.a>0.9) return x.l; } return 0.96; };
  for (const e of document.querySelectorAll('body *')) {
    if (e.closest('.wipe') || e.classList.contains('wm') || e.closest('.disc')) continue;
    const cs = getComputedStyle(e);
    if (cs.visibility==='hidden' || cs.display==='none' || parseFloat(cs.opacity)<0.05) continue;
    const r = e.getBoundingClientRect(); if (r.width===0 || r.height===0) continue;
    const hasText = [...e.childNodes].some(n => n.nodeType===3 && n.textContent.trim());
    if (!hasText) continue;
    const txt = e.textContent.trim().slice(0,40); const fs = parseFloat(cs.fontSize);
    if (fs < 20) issues.push({type:'small-font', text:txt, size:fs});
    if (r.right > W-30 || r.left < 20 || r.bottom > H-4 || r.top < 0) issues.push({type:'out-of-bounds', text:txt});
    if (r.bottom > SUB_TOP && r.top < H-20) issues.push({type:'subtitle-zone-overlap', text:txt, bottom:Math.round(r.bottom)});
    if ((e.scrollWidth > e.clientWidth+2 || e.scrollHeight > e.clientHeight+2) && cs.overflow!=='visible') issues.push({type:'clipped', text:txt});
    const tt = document.querySelector('.terms'); const ct = e.closest('.content');
    if (tt && ct && r.bottom > tt.getBoundingClientRect().top - 2) issues.push({type:'content-overlaps-terms', text:txt, bottom:Math.round(r.bottom)});
    const fg = lum(cs.color), bg = bgOf(e);
    if (fg) { const a=Math.max(fg.l,bg), b=Math.min(fg.l,bg); const ratio=(a+0.05)/(b+0.05);
      const large = fs>=24 && (parseInt(cs.fontWeight)>=700) || fs>=32;
      if (ratio < (large?3:4.5)) issues.push({type:'low-contrast', text:txt, ratio:Math.round(ratio*100)/100}); }
  }
  return issues; }"""


def render_animated(page, html_doc, events, total_dur, outdir, tag, qa_out=None, subs=None):
    """Renders only frames where something changes. Returns (clean_entries, burn_entries), each a list of [frame_path, duration_s].
    subs = list of cues with scene-local start/end for the burned-in (AR + EN) variant."""
    page.set_content(f"<!doctype html><meta charset='utf-8'>{html_doc}", wait_until="load")
    page.evaluate("document.fonts.ready")
    page.evaluate(INIT_JS, events)
    step = 1.0 / FPS
    windows = [(e["delay"] - 1e-6, e["delay"] + e["dur"] + step) for e in events]
    last_end = max((w[1] for w in windows), default=0.0)
    cues = subs or []

    def cue_at(t):
        for k, c in enumerate(cues):
            if c["start"] <= t < c["end"]:
                return k
        return -1

    n_frames = max(1, int(math.ceil(total_dur / step)))
    clean, burn = [], []
    prev_cue = -2
    for f in range(n_frames):
        t = f * step
        need_clean = f == 0 or (t <= last_end + 1e-9 and any(a_ <= t <= b_ for a_, b_ in windows))
        k = cue_at(t) if cues else -1
        need_burn = need_clean or (cues and k != prev_cue)
        if need_clean or need_burn:
            page.evaluate(SET_JS, t)
            if need_clean:
                page.evaluate(SUB_JS, "")
                path = outdir / f"{tag}_{f:05d}_c.jpg"
                page.screenshot(path=str(path), type="jpeg", quality=95)
                clean.append([path, step])
            elif clean:
                clean[-1][1] += step
            if cues:
                page.evaluate(SUB_JS, sub_html(cues[k]) if k >= 0 else "")
                path = outdir / f"{tag}_{f:05d}_b.jpg"
                page.screenshot(path=str(path), type="jpeg", quality=95)
                burn.append([path, step])
        else:
            if clean:
                clean[-1][1] += step
            if burn:
                burn[-1][1] += step
        prev_cue = k
    for lst in (clean, burn):
        if lst:
            used = sum(e[1] for e in lst)
            lst[-1][1] += max(0.0, total_dur - used)
    if qa_out is not None:
        page.evaluate(SET_JS, last_end + 1.0)
        page.evaluate(SUB_JS, "")
        for it in page.evaluate(DOM_QA_JS):
            it["scene"] = tag
            qa_out.append(it)
        longest = max(cues, key=lambda c: len(c.get("ar") or "") + len(c.get("en") or ""), default=None)
        if longest:
            page.evaluate(SUB_JS, sub_html(longest))
            h = page.evaluate("() => { const e = document.getElementById('subtext'); if (!e) return null; const r = e.getBoundingClientRect(); const kids = [...e.children].map(x => x.getBoundingClientRect()); return {top: Math.min(...kids.map(k => k.top)), bottom: Math.max(...kids.map(k => k.bottom))}; }")
            if h and (h["top"] < 884 or h["bottom"] > 1074):
                qa_out.append({"type": "subtitle-overflow", "text": (longest.get("en") or "")[:40], "scene": tag, "top": round(h["top"]), "bottom": round(h["bottom"])})
            page.evaluate(SUB_JS, "")
    return clean, burn


def frames_to_video(entries, audio, dst, total_dur):
    lst = Path(str(dst) + ".ffconcat")
    lines = ["ffconcat version 1.0"]
    for p, d in entries:
        lines.append(f"file '{Path(p).resolve()}'")
        lines.append(f"duration {d:.5f}")
    lines.append(f"file '{Path(entries[-1][0]).resolve()}'")
    lst.write_text("\n".join(lines) + "\n", encoding="utf-8")
    sh(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-i", str(audio),
        "-vf", f"fps={FPS},format=yuv420p", "-c:v", "libx264", "-preset", "slow", "-crf", "16",
        "-r", str(FPS), "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "2",
        "-af", "apad", "-t", f"{total_dur:.3f}", "-movflags", "+faststart", str(dst)])


# ---------------------------------------------------------------- subtitles
def _split_text(text):
    """Split into two parts near the middle, preferring punctuation, then spaces."""
    mid = len(text) / 2
    best, best_d = None, None
    for m in re.finditer(r"[.!?؟,;:،]\s+", text):
        pos = m.end()
        d = abs(pos - mid)
        if 0.25 * len(text) <= pos <= 0.75 * len(text) and (best is None or d < best_d):
            best, best_d = pos, d
    if best is None:
        for m in re.finditer(r"\s+", text):
            pos = m.end()
            d = abs(pos - mid)
            if best is None or d < best_d:
                best, best_d = pos, d
    if best is None:
        return text, ""
    return text[:best].strip(), text[best:].strip()


def split_long_cues(cues, en_max=78, ar_max=64, min_part=1.1):
    """Long AR/EN cues become several cues that switch at the same time (stacked AR+EN stays aligned).
    Parts are split again until each fits the subtitle box (AR one line, EN at most two)."""
    def too_long(c):
        return len(c.get("en") or "") > en_max or len(c.get("ar") or "") > ar_max

    def rec(c, depth=0):
        ar, en = c.get("ar") or "", c.get("en") or ""
        dur_ = c["end"] - c["start"]
        if depth < 3 and too_long(c) and dur_ >= 2 * min_part:
            a1, a2 = _split_text(ar) if ar else ("", "")
            e1, e2 = _split_text(en) if en else ("", "")
            if (not ar or a2) and (not en or e2):
                ratios = []
                if ar:
                    ratios.append(len(a1) / max(1, len(ar)))
                if en:
                    ratios.append(len(e1) / max(1, len(en)))
                r = min(0.7, max(0.3, sum(ratios) / len(ratios)))
                tm = c["start"] + dur_ * r
                return (rec({**c, "end": tm, "ar": a1 or None, "en": e1 or None, "de": c["de"]}, depth + 1)
                        + rec({**c, "start": tm, "ar": a2 or None, "en": e2 or None, "de": None}, depth + 1))
        return [c]

    out = []
    for c in cues:
        out.extend(rec(c))
    return out


def extend_cues(cues, extra=0.45):
    """Keep subtitles a little longer (reading time), never overlapping the next cue."""
    for i, c in enumerate(cues):
        nxt = cues[i + 1]["start"] - 0.05 if i + 1 < len(cues) else c["end"] + extra
        c["end"] = max(c["end"], min(c["end"] + extra, nxt))
    return cues


def ts(t, sep=","):
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}{sep}{ms:03d}"


def ass_ts(t):
    cs = int(round(t * 100))
    h, cs = divmod(cs, 360000)
    m, cs = divmod(cs, 6000)
    s, cs = divmod(cs, 100)
    return f"{h}:{m:02d}:{s:02d}.{cs:02d}"


def write_subs(cues, vid, outdir, cues_de=None):
    outdir.mkdir(parents=True, exist_ok=True)
    for lang in ("de", "ar", "en"):
        srt, vtt = [], ["WEBVTT", ""]
        n = 0
        for c in (cues_de if (lang == "de" and cues_de is not None) else cues):
            txt = c.get(lang)
            if not txt:
                continue
            n += 1
            if lang == "ar":
                txt = "\u200f" + txt + "\u200f"
            srt += [str(n), f"{ts(c['start'])} --> {ts(c['end'])}", txt, ""]
            vtt += [f"{ts(c['start'], '.')} --> {ts(c['end'], '.')}", txt, ""]
        (outdir / f"{vid}.{lang}.srt").write_text("\n".join(srt), encoding="utf-8")
        (outdir / f"{vid}.{lang}.vtt").write_text("\n".join(vtt), encoding="utf-8")


def write_ass(cues, langs, path):
    """One event per cue with all languages stacked (AR on top, EN below) so wrapped lines never collide."""
    head = ("[Script Info]\nScriptType: v4.00+\nPlayResX: 1920\nPlayResY: 1080\nWrapStyle: 0\nScaledBorderAndShadow: yes\n\n"
            "[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, "
            "Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n"
            "Style: base,Noto Sans,44,&H00432B06,&H00432B06,&H00FFFFFF,&H00000000,0,0,0,0,100,100,0,0,1,3,0,2,120,120,48,1\n\n"
            "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n")
    tags = {"ar": r"{\fnNoto Sans Arabic\fs58\b1\c&H00432B06&}",
            "en": r"{\fnNoto Sans\fs44\b0\c&H006A6A2D&}",
            "de": r"{\fnNoto Sans\fs44\b0\c&H00432B06&}"}
    ar_open, ar_close = r"{\fnNoto Sans\fs46\b1}", r"{\fnNoto Sans Arabic\fs58\b1}"
    latin = re.compile(r"([A-Za-zÄÖÜäöüß0-9][A-Za-zÄÖÜäöüß0-9./§%&\-]*(?: [A-Za-zÄÖÜäöüß0-9./§%&\-]+)*)")
    emb = {"ar": ("\u202b", "\u202c"), "en": ("\u202a", "\u202c"), "de": ("\u202a", "\u202c")}
    ev = []
    for c in cues:
        parts = []
        for l in langs:
            if not c.get(l):
                continue
            txt = c[l]
            if l == "ar":
                txt = latin.sub(lambda m: ar_open + m.group(1) + ar_close, txt)
            parts.append(tags[l] + emb[l][0] + txt + emb[l][1])
        if parts:
            ev.append(f"Dialogue: 0,{ass_ts(c['start'])},{ass_ts(c['end'])},base,,0,0,0,," + r"\N".join(parts))
    path.write_text(head + "\n".join(ev) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- voice audition
def audition(run, cfg):
    """Same hard sentences for several voices, so a human can listen and Whisper can score intelligibility."""
    adir = ROOT / "out" / "audition"
    adir.mkdir(parents=True, exist_ok=True)
    sub = subscription_info()
    lines = []
    for vp in ("scripts/E/01-berufsbilder.json", "scripts/E/02-normen.json"):
        j = json.loads((ROOT / vp).read_text(encoding="utf-8"))
        for sc in j["scenes"]:
            lines += [(0, ln) for ln in sc["lines"]]
    with_tts, seen = [], set()
    for sid, ln in lines:
        tts_ = ln.get("tts")
        if tts_ and tts_[:40] not in seen and len(tts_) < 140:
            with_tts.append(ln)
            seen.add(tts_[:40])
        if len(with_tts) >= 5:
            break
    plain = [ln for sid, ln in lines if not ln.get("tts") and 70 <= len(ln["de"]) <= 120][::7][:3]
    texts = [(ln.get("tts") or ln["de"]) for ln in with_tts + plain]
    voices = run["voices"]
    total = sum(len(t) for t in texts) * len(voices)
    log(f"audition: {len(voices)} voices x {len(texts)} sentences = {total} characters")
    if total > 20000:
        log("ERROR: audition too large")
        sys.exit(1)
    silence(adir / "gap.wav", 0.7)
    meta = {"texts": texts, "voices": []}
    for v in voices:
        parts = []
        for i, t in enumerate(texts):
            mp3 = synth(t, None, None, cfg, v["id"])
            wav = adir / f"tmp_{i}.wav"
            to_wav(mp3, wav)
            parts += [wav.resolve(), (adir / "gap.wav").resolve()]
            Path(adir / f"tmp_{i}_keep").write_text("x")
        lst = adir / "list.txt"
        lst.write_text("".join(f"file '{p}'\n" for p in parts), encoding="utf-8")
        safe = re.sub(r"[^A-Za-z0-9]+", "_", v["name"]).strip("_")
        sh(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c:a", "libmp3lame", "-b:a", "160k", str(adir / f"{safe}.mp3")])
        for f in adir.glob("tmp_*"):
            f.unlink()
        meta["voices"].append({"name": v["name"], "id": v["id"], "file": f"{safe}.mp3", "note": v.get("note", "")})
        log("  voice done:", v["name"])
    (adir / "audition.json").write_text(json.dumps({**meta, "subscription": sub}, ensure_ascii=False, indent=2), encoding="utf-8")
    for f in ("gap.wav", "list.txt"):
        (adir / f).unlink(missing_ok=True)


# ---------------------------------------------------------------- main
def main():
    import argparse
    ap = argparse.ArgumentParser(description="Build videos listed in pipeline/run.json (or --script for a local test)")
    ap.add_argument("--script", action="append", help="build this script instead of run.json's list")
    ap.add_argument("--synthesize", dest="synthesize", action="store_true", default=None)
    ap.add_argument("--no-synthesize", dest="synthesize", action="store_false")
    ap.add_argument("--silent", action="store_true", help="accepted for compatibility (no-synthesize is always silent)")
    ap.add_argument("--burn", dest="burn", action="store_true", default=None)
    ap.add_argument("--no-burn", dest="burn", action="store_false")
    ap.add_argument("--rev", type=int, default=None)
    args = ap.parse_args()
    run = json.loads((ROOT / "pipeline" / "run.json").read_text(encoding="utf-8"))
    if args.script:
        run["video"] = args.script
        run["action"] = "build"
        os.environ.pop("VIDEO_INDEX", None)
    if args.synthesize is not None:
        run["synthesize"] = args.synthesize
    if args.burn is not None:
        run["burn"] = args.burn
    if args.rev is not None:
        run["rev"] = args.rev
    cfg = json.loads((ROOT / "pipeline" / "config.json").read_text(encoding="utf-8"))
    action = run.get("action", "none")
    OUT.mkdir(exist_ok=True)
    if action != "build" and os.environ.get("VIDEO_INDEX", "0") not in ("", "0"):
        return
    if action == "list-voices":
        list_voices()
        return
    if action == "audition":
        audition(run, cfg)
        return
    if action != "build":
        log("run.json action is not 'build' or 'list-voices'; nothing to do")
        return

    vids = run["video"] if isinstance(run["video"], list) else [run["video"]]
    idx = os.environ.get("VIDEO_INDEX", "")
    if idx != "":
        i = int(idx)
        if i >= len(vids):
            log(f"no video for matrix index {i}; nothing to do")
            return
        vids = [vids[i]]
    for v in vids:
        build_one(run, cfg, v)


MONTHS_DE = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]


def _de(x):
    return (x.get("de") or "") if isinstance(x, dict) else (x or "")


def stand_line(script):
    """Short closing-card line 'Stand: Monat Jahr' (the script's `stand` field is an internal review note)."""
    st = str(script.get("stand", ""))
    m = re.match(r"\s*(\d{4})-(\d{2})", st)
    if m:
        return f"Keine Rechts- oder Steuerberatung · Stand: {MONTHS_DE[int(m.group(2)) - 1]} {m.group(1)}"
    return st if len(st) < 90 else "Keine Rechts- oder Steuerberatung"


def map_slide(s):
    """Map this repo's layouts (title|bullets|cards|table|quote|summary) onto those build_video.py renders."""
    s = dict(s)
    lay, items = s.get("layout", "bullets"), s.get("items") or []
    if lay in ("title", "quote"):
        s.update(layout="hook", items=[s.get("heading", "")], heading="")
    elif lay == "summary":
        s["layout"] = "recap"
    elif lay == "cards":
        cards = []
        for it in items:
            t, _, b = str(it).partition(": ")
            cards.append({"title": t.strip(), "body": b.strip()})
        s["items"] = cards
    elif lay == "table" and isinstance(items, list):
        rows = []
        for it in items:
            t = it if isinstance(it, str) else " : ".join(map(str, it.values())) if isinstance(it, dict) else str(it)
            k, sep, v = t.partition(": ")
            rows.append([k.strip(), v.strip()] if sep else [t.strip()])
        two = all(len(r) == 2 for r in rows)
        s["items"] = {"columns": ["Thema", "Kernaussage"] if two else ["Thema"], "rows": rows}
    return s


def normalize_script(script):
    """Defaults so scripts without scene id/name work: id = index+1, name = slide heading."""
    first_title = True
    for i, sc in enumerate(script["scenes"]):
        sc.setdefault("id", i + 1)
        sc.setdefault("name", sc.get("slide", {}).get("heading", ""))
        sl = sc["slide"]
        if sl.get("layout") == "title" and first_title:
            sl = dict(sl, badge=sl.get("badge") or "Keine Rechts- oder Steuerberatung")
            first_title = False
        sc["slide"] = map_slide(sl)
    script["stand_line"] = stand_line(script)
    return script


def launch_chromium(p):
    """Default launch (CI: playwright install chromium); local fallback to any pre-installed Chromium."""
    try:
        return p.chromium.launch()
    except Exception as e:
        base = Path(os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers"))
        for pat in ("chromium-*/chrome-linux/chrome", "chromium/chrome-linux/chrome", "chromium_headless_shell-*/chrome-linux/headless_shell"):
            for c in sorted(base.glob(pat)):
                return p.chromium.launch(executable_path=str(c))
        raise e


def build_one(run, cfg, video_path):
    global OUT
    script = normalize_script(json.loads((ROOT / video_path).read_text(encoding="utf-8")))
    vid = script["id"]
    OUT = ROOT / "out" / vid
    OUT.mkdir(parents=True, exist_ok=True)
    log(f"=== building {vid} ===")
    synthesize = bool(run.get("synthesize", False))
    burn = bool(run.get("burn", True))
    only_scenes = run.get("only_scenes")  # optional: list of scene ids for quick previews
    voice_id = run.get("voice_id") or cfg.get("voice_id") or ""
    warnings = []

    commercial, sub = False, None
    if synthesize:
        if not voice_id:
            log("ERROR: no voice_id (set it in pipeline/run.json). Run action 'list-voices' first.")
            sys.exit(1)
        sub = subscription_info()
        tier = (sub or {}).get("tier")
        commercial = bool(tier and tier != "free") or os.environ.get("ELEVENLABS_COMMERCIAL", "").lower() == "true"
        if not commercial:
            warnings.append("Free/unknown ElevenLabs plan: audio is NOT licensed for commercial use. Do not publish.")
    watermark = None
    if not synthesize:
        watermark = "DRY RUN · ohne Ton · nicht veröffentlichen"
    elif not commercial:
        watermark = "TEST · nicht veröffentlichen"

    scenes = script["scenes"]
    if only_scenes:
        scenes = [s for s in scenes if s["id"] in only_scenes]
    flat = [(si, li, ln) for si, sc in enumerate(scenes) for li, ln in enumerate(sc["lines"])]
    texts = [(ln.get("tts") or ln["de"]) for _, _, ln in flat]
    total_chars = sum(len(t) for t in texts)
    log(f"{vid}: {len(scenes)} scenes, {len(flat)} lines, {total_chars} characters")

    adir = OUT / "audio"
    adir.mkdir(exist_ok=True)
    uncached = 0
    if synthesize:
        for i in range(len(flat)):
            key = tts_key(cfg, voice_id, texts[i], texts[i - 1] if i > 0 else None,
                          texts[i + 1] if i + 1 < len(texts) else None)
            if not (CACHE / f"{key}.mp3").exists():
                uncached += len(texts[i])
        limit = int(run.get("allow_chars", cfg.get("max_chars_per_run", 12000)))
        log(f"characters to synthesize now (uncached): {uncached} (limit {limit})")
        if sub and sub.get("character_limit") is not None:
            remaining = sub["character_limit"] - (sub.get("character_count") or 0)
            log(f"plan credits remaining: {remaining}")
            if uncached > remaining:
                log("ERROR: not enough credits for this run.")
                sys.exit(1)
        if uncached > limit:
            log("ERROR: uncached characters exceed the per-run limit; raise allow_chars in run.json to proceed.")
            sys.exit(1)

    files = {}
    for i, (si, li, ln) in enumerate(flat):
        wav = adir / f"s{si:02d}_l{li:02d}.wav"
        if synthesize:
            mp3 = synth(texts[i], texts[i - 1] if i > 0 else None,
                        texts[i + 1] if i + 1 < len(texts) else None, cfg, voice_id)
            to_wav(mp3, wav)
        else:
            silence(wav, max(1.0, len(texts[i]) / 13.0))
        files[(si, li)] = wav

    lead, gap, tail, intro_s = cfg["lead"], cfg["gap_line"], cfg["tail"], cfg["intro_seconds"]
    sil = {}
    outro_s = 4.5
    for name, secs in (("lead", lead), ("gap", gap), ("tail", tail), ("intro", intro_s), ("outro", outro_s)):
        p = adir / f"sil_{name}.wav"
        silence(p, secs)
        sil[name] = p
    t = intro_s
    cues, scene_info, scene_audio = [], [], []
    for si, sc in enumerate(scenes):
        parts = [sil["lead"]]
        st, cur = t, t + lead
        task_times, sol_times, line_times = [], [], []
        for li, ln in enumerate(sc["lines"]):
            d = duration(files[(si, li)])
            line_times.append(round(cur - st, 3))
            if ln["de"].startswith("Aufgabe"):
                task_times.append(round(cur - st, 3))
            elif ln["de"].startswith("Lösung"):
                sol_times.append(round(cur - st, 3))
            if d > 12:
                warnings.append(f"scene {sc['id']} line {li+1}: {d:.1f}s long")
            cues.append({"start": cur, "end": cur + d + 0.15, "de": ln["de"], "ar": ln.get("ar"), "en": ln.get("en")})
            for lang in ("ar", "en"):
                if ln.get(lang) and len(ln[lang]) > 92:
                    warnings.append(f"scene {sc['id']} line {li+1}: {lang} subtitle {len(ln[lang])} chars")
            parts.append(files[(si, li)])
            cur += d
            if li < len(sc["lines"]) - 1:
                parts.append(sil["gap"])
                cur += gap
        parts.append(sil["tail"])
        cur += tail
        sa = adir / f"scene_{si:02d}.wav"
        concat_files(parts, sa)
        scene_audio.append(sa)
        scene_info.append({"id": sc["id"], "name": sc.get("name"), "start": round(st, 2), "end": round(cur, 2),
                           "task_times": task_times, "sol_times": sol_times, "line_times": line_times})
        t = cur

    # --- animated slides -> segments
    lk_uri = data_uri(ROOT / "assets" / "logo-lockup.png")
    fdir = OUT / "frames"
    vdir = OUT / "seg"
    fdir.mkdir(exist_ok=True)
    vdir.mkdir(exist_ok=True)
    seg_files, seg_burn, finals, dom_issues = [], [], [], []
    cues_de = [dict(c) for c in cues]
    cues = extend_cues(split_long_cues([dict(c) for c in cues], en_max=76, ar_max=58))

    def local_cues(t0, t1):
        return [{**c, "start": max(0.0, c["start"] - t0), "end": min(t1 - t0, c["end"] - t0)}
                for c in cues if c["end"] > t0 and c["start"] < t1]

    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = launch_chromium(p)
        page = b.new_page(viewport={"width": 1920, "height": 1080})
        t_render = time.time()
        # intro
        ent, entb = render_animated(page, intro_page(script, lk_uri, watermark), intro_events(), intro_s, fdir, "intro", dom_issues, None)
        frames_to_video(ent, sil["intro"], vdir / "seg00.mp4", intro_s)
        seg_files.append(vdir / "seg00.mp4")
        seg_burn.append(vdir / "seg00.mp4")
        finals.append(ent[-1][0])
        n_frames = len(ent)
        for si, sc in enumerate(scenes):
            info = scene_info[si]
            sd = info["end"] - info["start"]
            html_doc, n_items, n_terms, kind = scene_page(sc, lk_uri, watermark)
            ev = scene_events(kind, n_items, n_terms, sd, tail, info.get("task_times"), info.get("sol_times"), info.get("line_times"))
            ent, entb = render_animated(page, html_doc, ev, sd, fdir, f"s{si+1:02d}", dom_issues,
                                        local_cues(info["start"], info["end"]) if burn else None)
            frames_to_video(ent, scene_audio[si], vdir / f"seg{si+1:02d}.mp4", sd)
            seg_files.append(vdir / f"seg{si+1:02d}.mp4")
            if burn and entb:
                frames_to_video(entb, scene_audio[si], vdir / f"segb{si+1:02d}.mp4", sd)
                seg_burn.append(vdir / f"segb{si+1:02d}.mp4")
            finals.append(ent[-1][0])
            n_frames += len(ent) + len(entb)
            log(f"  scene {sc['id']}: {len(ent)} clean + {len(entb)} subtitled frames, {sd:.1f}s")
        if script.get("outro", True):
            oc = {"slide": {"layout": "endcard", "heading": "Deutsch Beruf · Online-Akademie",
                            "items": [_de(script.get("next", ""))], "stand": script.get("stand_line", "")}}
            html_doc, n_items, n_terms, kind = scene_page(oc, lk_uri, watermark)
            ent, entb = render_animated(page, html_doc, scene_events(kind, 0, 0, outro_s, 0.0), outro_s, fdir, "outro", dom_issues, None)
            frames_to_video(ent, sil["outro"], vdir / "seg_outro.mp4", outro_s)
            seg_files.append(vdir / "seg_outro.mp4")
            seg_burn.append(vdir / "seg_outro.mp4")
            finals.append(ent[-1][0])
            n_frames += len(ent)
        b.close()
        log(f"rendered {n_frames} frames in {time.time()-t_render:.0f}s")

    joined = OUT / "joined.mp4"
    concat_files(seg_files, joined)
    clean = OUT / f"{vid}.clean.mp4"
    sh(["ffmpeg", "-y", "-i", str(joined), "-c:v", "copy", "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
        "-c:a", "aac", "-b:a", "192k", "-ar", "44100", str(clean)])
    joined.unlink()

    write_subs(cues, vid, OUT / "subtitles", cues_de)
    burned = None
    if burn:
        joinedb = OUT / "joinedb.mp4"
        concat_files(seg_burn, joinedb)
        burned = OUT / f"{vid}.ar-en.mp4"
        sh(["ffmpeg", "-y", "-i", str(joinedb), "-c:v", "copy", "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
            "-c:a", "aac", "-b:a", "192k", "-ar", "44100", str(burned)])
        joinedb.unlink()

    # --- previews: one contact sheet of final states + a few frames from the burned video
    fin_dir = OUT / "finals"
    fin_dir.mkdir(exist_ok=True)
    for i, f in enumerate(finals):
        (fin_dir / f"f{i:02d}.jpg").write_bytes(Path(f).read_bytes())
    cs_dir = OUT / "cs"
    cs_dir.mkdir(exist_ok=True)
    for i, f in enumerate(finals):
        (cs_dir / f"c{i:02d}.jpg").write_bytes(Path(f).read_bytes())
    cols = 4
    rows_n = math.ceil(len(finals) / cols)
    sh(["ffmpeg", "-y", "-framerate", "1", "-start_number", "0", "-i", str(cs_dir / "c%02d.jpg"),
        "-vf", f"scale=480:-1,tile={cols}x{rows_n}:padding=6:color=white", "-frames:v", "1", str(OUT / "contact-sheet.png")])
    for f in cs_dir.glob("*"):
        f.unlink()
    cs_dir.rmdir()
    if burned:
        picks = [cues[0], cues[len(cues) // 3], cues[len(cues) // 2], cues[-1]]
        for k, c in enumerate(picks):
            sh(["ffmpeg", "-y", "-ss", f"{(c['start'] + c['end']) / 2:.2f}", "-i", str(burned),
                "-frames:v", "1", str(OUT / f"frame{k}.png")])
        # a short burst of the first scene transition to check the motion
        t0 = scene_info[0]["start"]
        for k, off in enumerate((0.1, 0.3, 0.5, 0.9, 1.5)):
            sh(["ffmpeg", "-y", "-ss", f"{t0 + off:.2f}", "-i", str(burned), "-frames:v", "1", str(OUT / f"motion{k}.png")])
        lat = [c for c in cues if re.search(r"[A-Za-z]{2}", c.get("ar") or "")]
        for k, c in enumerate([lat[i * len(lat) // 5] for i in range(5)] if len(lat) >= 5 else lat):
            sh(["ffmpeg", "-y", "-ss", f"{(c['start'] + c['end']) / 2:.2f}", "-i", str(burned), "-frames:v", "1", str(OUT / f"bidi{k}.png")])
        sh(["ffmpeg", "-y", "-ss", "0.3", "-i", str(burned), "-frames:v", "1", str(OUT / "intro0.png")])
        sh(["ffmpeg", "-y", "-ss", "1.2", "-i", str(burned), "-frames:v", "1", str(OUT / "intro1.png")])
        sh(["ffmpeg", "-y", "-ss", "3.0", "-i", str(burned), "-frames:v", "1", str(OUT / "intro2.png")])

    total_dur = duration(clean)
    qa = {"duration_s": round(total_dur, 1), "animated_frames": n_frames}
    # subtitle reading speed (characters per second) and length
    lim = {"en": 20.0, "ar": 17.0, "de": 17.0}
    sub_qa = {"over_cps": [], "max_cps": {}, "too_long": []}
    for c in cues:
        dur_ = max(0.3, c["end"] - c["start"])
        for lang in ("ar", "en"):
            tx = c.get(lang)
            if not tx:
                continue
            cps = len(tx) / dur_
            sub_qa["max_cps"][lang] = round(max(sub_qa["max_cps"].get(lang, 0), cps), 1)
            if cps > lim[lang]:
                sub_qa["over_cps"].append({"t": round(c["start"], 1), "lang": lang, "cps": round(cps, 1), "chars": len(tx)})
            if len(tx) > (72 if lang == "en" else 58):
                sub_qa["too_long"].append({"t": round(c["start"], 1), "lang": lang, "chars": len(tx)})
    qa["subtitles"] = {"cues": len(cues), "over_cps_count": len(sub_qa["over_cps"]), "too_long_count": len(sub_qa["too_long"]),
                       "max_cps": sub_qa["max_cps"], "worst": sorted(sub_qa["over_cps"], key=lambda x: -x["cps"])[:8]}
    probe = sh(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,width,height,r_frame_rate,duration",
                "-of", "json", str(clean)])
    qa["streams"] = json.loads(probe.stdout).get("streams", [])
    vd = [float(x.get("duration", 0)) for x in qa["streams"] if x.get("codec_type") == "video"]
    ad = [float(x.get("duration", 0)) for x in qa["streams"] if x.get("codec_type") == "audio"]
    if vd and ad and abs(vd[0] - ad[0]) > 0.25:
        warnings.append(f"audio/video duration differ by {abs(vd[0]-ad[0]):.2f}s")
    qa["dom_issues_count"] = len(dom_issues)
    kinds = {}
    for it in dom_issues:
        kinds[it["type"]] = kinds.get(it["type"], 0) + 1
    qa["dom_issue_kinds"] = kinds
    if synthesize:
        r = subprocess.run(["ffmpeg", "-i", str(clean), "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True)
        ms = re.findall(r"I:\s+(-?\d+\.\d+) LUFS", r.stderr)
        if ms:
            qa["loudness_lufs"] = float(ms[-1])
        r = subprocess.run(["ffmpeg", "-i", str(clean), "-af", "silencedetect=n=-45dB:d=2.6", "-f", "null", "-"], capture_output=True, text=True)
        qa["long_silences"] = len(re.findall(r"silence_start", r.stderr))
        if qa["long_silences"]:
            warnings.append(f"{qa['long_silences']} silent stretches > 2.6 s in the audio")
    report = {
        "video": vid, "synthesized": synthesize, "voice_id": voice_id or None, "model": cfg["model_id"],
        "subscription": sub, "commercial_ok": commercial, "characters_total": total_chars,
        "characters_synthesized_now": uncached, "scenes": scene_info, "qa": qa, "dom_issues": dom_issues[:80],
        "subtitle_over_cps": sub_qa["over_cps"][:40], "subtitle_too_long": sub_qa["too_long"][:40], "warnings": warnings,
        "files": sorted(p.name for p in OUT.iterdir() if p.is_file()),
    }
    (OUT / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    log(json.dumps({k: report[k] for k in ("video", "synthesized", "commercial_ok", "characters_total", "qa", "warnings")}, ensure_ascii=False, indent=2))
    for d in (adir, vdir, fdir):
        for f in d.glob("*"):
            f.unlink()
        d.rmdir()


if __name__ == "__main__":
    main()
