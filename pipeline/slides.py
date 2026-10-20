"""Render scene slides (1920x1080, light theme) to PNG via HTML + Playwright/Chromium."""
import base64, html, os, re, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
W, H = 1920, 1080
SAFE_BOTTOM = 740          # below this the burned subtitles live
SAFE_RIGHT = W - 80
AR_RE = re.compile(r"[؀-ۿݐ-ݿ]")

SANS = "'Noto Sans','Inter','DejaVu Sans','FreeSans',sans-serif"
ARAB = "'Noto Naskh Arabic','Noto Sans Arabic','Amiri','DejaVu Sans','FreeSerif',serif"


def fc_has(family):
    """True if fontconfig resolves `family` to itself."""
    try:
        out = subprocess.run(["fc-match", "-f", "%{family}", family], capture_output=True, text=True).stdout
    except FileNotFoundError:
        return False
    return family.lower() in out.lower()


def pick_font(candidates):
    for c in candidates:
        if fc_has(c):
            return c
    return candidates[-1]


def esc(s):
    return html.escape(str(s), quote=True)


CSS = f"""
:root{{--bg:#F6F8FB;--ink:#10243A;--muted:#56677A;--brand:#0B4F6C;--accent:#E8A317;--card:#FFFFFF;--line:#D5DEE8;--soft:#E7F0F7}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:var(--bg);font-family:{SANS};color:var(--ink)}}
[lang=ar],[dir=rtl]{{font-family:{ARAB}}}
.stage{{position:relative;width:{W}px;height:{H}px;background:linear-gradient(180deg,#FBFCFE 0%,#F1F5FA 100%)}}
.bar{{position:absolute;left:0;top:0;width:18px;height:{H}px;background:var(--brand)}}
.logo{{position:absolute;right:56px;top:36px;height:92px}}
.kicker{{position:absolute;left:96px;top:50px;width:1500px;font-size:30px;font-weight:700;letter-spacing:.06em;
  text-transform:uppercase;color:var(--brand)}}
.kicker::after{{content:"";display:block;width:90px;height:6px;background:var(--accent);margin-top:12px;border-radius:3px}}
.content{{position:absolute;left:96px;top:150px;width:1728px;height:{SAFE_BOTTOM-150}px;overflow:hidden}}
h1{{font-size:62px;line-height:1.32;font-weight:800;color:var(--ink);max-height:170px;overflow:hidden;width:1560px}}
ul.b{{list-style:none;margin-top:26px;width:1560px}}
ul.b li{{position:relative;font-size:42px;line-height:1.28;padding:10px 0 10px 56px;font-weight:500}}
ul.b li::before{{content:"";position:absolute;left:8px;top:25px;width:20px;height:20px;border-radius:5px;background:var(--accent)}}
.cards{{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:26px;width:1700px}}
.card{{background:var(--card);border:2px solid var(--line);border-radius:22px;padding:22px 30px;height:150px;overflow:hidden;
  display:flex;align-items:center;gap:26px;box-shadow:0 6px 18px rgba(16,36,58,.07)}}
.card .n{{flex:0 0 74px;height:74px;border-radius:50%;background:var(--brand);color:#fff;font-size:38px;font-weight:800;
  display:flex;align-items:center;justify-content:center}}
.card .t{{font-size:38px;font-weight:700;line-height:1.2;flex:1}}
table{{margin-top:24px;border-collapse:separate;border-spacing:0 10px;width:1700px}}
td{{background:var(--card);font-size:36px;padding:14px 28px;line-height:1.2;border-top:2px solid var(--line);border-bottom:2px solid var(--line)}}
td.k{{width:36%;font-weight:800;color:var(--brand);border-left:2px solid var(--line);border-radius:16px 0 0 16px;background:var(--soft)}}
td.v{{border-right:2px solid var(--line);border-radius:0 16px 16px 0}}
td.only{{border-left:2px solid var(--line);border-right:2px solid var(--line);border-radius:16px}}
.title-wrap{{position:absolute;left:96px;top:250px;width:1500px}}
.title-wrap h1{{font-size:88px;line-height:1.25;max-height:330px;width:1500px}}
.title-wrap .sub{{font-size:38px;color:var(--muted);margin-top:30px}}
.quote{{margin-top:20px;border-left:10px solid var(--accent);padding:10px 40px;font-size:54px;line-height:1.3;font-style:italic;width:1500px}}
.quote small{{display:block;font-size:34px;font-style:normal;color:var(--muted);margin-top:18px}}
ul.s li::before{{content:"\\2713";background:none;color:var(--brand);font-weight:800;font-size:40px;top:6px;width:auto;height:auto}}
.terms{{position:absolute;left:96px;top:{SAFE_BOTTOM-92}px;width:1728px;display:flex;gap:12px;overflow:hidden;height:80px}}
.term{{background:var(--soft);border:2px solid #BCD3E3;border-radius:40px;padding:0 20px;height:76px;display:flex;align-items:center;gap:10px;
  font-size:25px;white-space:nowrap}}
.term b{{color:var(--brand)}} .term i{{color:var(--muted);font-style:normal}} .term .ar{{font-size:28px;direction:rtl}}
"""


def logo_uri():
    p = ROOT / "assets" / "logo-cropped.png"
    return "data:image/png;base64," + base64.b64encode(p.read_bytes()).decode()


def scene_html(slide, idx, total):
    lay = slide.get("layout", "bullets")
    items = slide.get("items") or []
    head = esc(slide.get("heading", ""))
    kick = esc(slide.get("kicker", ""))
    body = ""
    if lay == "title":
        body = (f'<div class="title-wrap" data-chk><h1 dir="auto">{head}</h1></div>')
    elif lay == "bullets" or lay == "summary":
        cls = "b s" if lay == "summary" else "b"
        lis = "".join(f'<li dir="auto" data-chk>{esc(i)}</li>' for i in items)
        body = f'<div class="content" data-chk><h1 dir="auto" data-chk>{head}</h1><ul class="{cls}">{lis}</ul></div>'
    elif lay == "cards":
        cs = "".join(f'<div class="card" data-chk><div class="n">{n}</div><div class="t" dir="auto" data-chk>{esc(i)}</div></div>'
                     for n, i in enumerate(items, 1))
        body = f'<div class="content" data-chk><h1 dir="auto" data-chk>{head}</h1><div class="cards">{cs}</div></div>'
    elif lay == "table":
        rows = ""
        for it in items:
            t = it if isinstance(it, str) else " : ".join(map(str, it.values())) if isinstance(it, dict) else str(it)
            if ":" in t:
                k, v = t.split(":", 1)
                rows += f'<tr><td class="k" dir="auto" data-chk>{esc(k.strip())}</td><td class="v" dir="auto" data-chk>{esc(v.strip())}</td></tr>'
            else:
                rows += f'<tr><td class="only" colspan="2" dir="auto" data-chk>{esc(t)}</td></tr>'
        body = f'<div class="content" data-chk><h1 dir="auto" data-chk>{head}</h1><table>{rows}</table></div>'
    elif lay == "quote":
        sub = "".join(f'<small dir="auto">{esc(i)}</small>' for i in items)
        body = f'<div class="content" data-chk><div class="quote" dir="auto" data-chk>{head}{sub}</div></div>'
    else:
        raise ValueError(f"unknown layout {lay!r}")
    terms = ""
    if lay != "title":
        for t in (slide.get("terms") or [])[:3]:
            terms += (f'<div class="term" data-chk><b lang="de">{esc(t.get("de",""))}</b><i>·</i>'
                      f'<span class="ar" lang="ar" dir="rtl">{esc(t.get("ar",""))}</span><i>·</i>'
                      f'<span lang="en">{esc(t.get("en",""))}</span></div>')
        terms = f'<div class="terms" data-chk>{terms}</div>' if terms else ""
    kicker = f'<div class="kicker" dir="auto">{kick}</div>' if kick else ""
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="stage"><div class="bar"></div>{kicker}<img class="logo" src="{logo_uri()}">{body}{terms}</div></body></html>')


CHECK_JS = f"""
() => {{
  const issues = [];
  const name = e => (e.className || e.tagName) + ': ' + (e.textContent||'').trim().slice(0,40);
  document.querySelectorAll('[data-chk]').forEach(e => {{
    if (e.scrollHeight > e.clientHeight + 4 || e.scrollWidth > e.clientWidth + 2)
      issues.push('overflow ' + name(e) + ' (' + e.scrollWidth + 'x' + e.scrollHeight + ' in ' + e.clientWidth + 'x' + e.clientHeight + ')');
    const r = e.getBoundingClientRect();
    if (e.textContent.trim() && (r.bottom > {SAFE_BOTTOM} + 1 || r.right > {SAFE_RIGHT} + 1))
      issues.push('outside safe area ' + name(e) + ' bottom=' + Math.round(r.bottom) + ' right=' + Math.round(r.right));
  }});
  const logo = document.querySelector('.logo').getBoundingClientRect();
  document.querySelectorAll('h1,.kicker,.title-wrap').forEach(e => {{
    const r = e.getBoundingClientRect();
    if (!(r.right < logo.left || r.left > logo.right || r.bottom < logo.top || r.top > logo.bottom) && e.textContent.trim())
      issues.push('overlaps logo ' + name(e));
  }});
  const sc = document.querySelector('.content') || document.querySelector('.title-wrap');
  if (sc) {{
    const kids = [...sc.querySelectorAll('li,.card,tr,.quote')];
    kids.forEach(k => {{ const r = k.getBoundingClientRect(); if (r.bottom > {SAFE_BOTTOM} - 90 && document.querySelector('.terms')) issues.push('collides with terms strip ' + name(k)); }});
  }}
  return issues;
}}
"""


def render_slides(scenes, outdir, log=print):
    """Render all scenes. Returns (list of png paths, list of issue dicts)."""
    from playwright.sync_api import sync_playwright
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    paths, issues = [], []
    with sync_playwright() as p:
        try:
            b = p.chromium.launch(args=["--font-render-hinting=none"])
        except Exception as e:
            exe = _find_chromium()
            if not exe:
                raise RuntimeError(f"Chromium not available: {e}")
            b = p.chromium.launch(executable_path=exe, args=["--font-render-hinting=none"])
        pg = b.new_page(viewport={"width": W, "height": H})
        for i, sc in enumerate(scenes, 1):
            pg.set_content(scene_html(sc["slide"], i, len(scenes)), wait_until="load")
            pg.evaluate("document.fonts.ready")
            found = pg.evaluate(CHECK_JS)
            for f in found:
                issues.append({"scene": i, "issue": f})
            out = outdir / f"slide-{i:02d}.png"
            pg.screenshot(path=str(out))
            paths.append(out)
        b.close()
    return paths, issues


def _find_chromium():
    base = Path(os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers"))
    for pat in ("chromium/chrome-linux/chrome", "chromium-*/chrome-linux/chrome", "chromium_headless_shell-*/chrome-linux/headless_shell"):
        for c in sorted(base.glob(pat)):
            return str(c)
    return None
