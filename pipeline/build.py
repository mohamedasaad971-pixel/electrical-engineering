#!/usr/bin/env python3
"""Build one video from a script JSON: slides -> TTS -> timeline -> subtitles -> mp4 + QA.

  python pipeline/build.py --script scripts/E/01-berufsbilder.json [--synthesize] [--burn] [--silent]
  python pipeline/build.py --run pipeline/run.json --index 0

Outputs to out/<ID>/: <ID>.mp4, <ID>.{ar,en,de}.srt, contact-sheet.png, qa.json
"""
import argparse, hashlib, json, math, os, re, shutil, subprocess, sys, time, wave
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import qa as qamod
import slides as slidemod

ROOT = Path(__file__).resolve().parent.parent
LINE_GAP = 0.35
SCENE_GAP = 0.8
LEAD_IN = 0.3
SUB_HOLD = 0.25            # subtitle stays this long after speech ends
FPS = 25
SR = 44100
VOICE_NAME = "Eleonore"
MODEL_ID = "eleven_multilingual_v2"
API = "https://api.elevenlabs.io/v1"
CUE_CHARS = {"ar": 38, "en": 44, "de": 44}   # chars per subtitle line (2 lines per cue)


def log(*a):
    print(*a, flush=True)


def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        raise RuntimeError(f"command failed ({cmd[0]}): {' '.join(map(str, cmd))[:300]}\n{r.stderr[-1500:]}")
    return r


# ---------------------------------------------------------------- TTS
class Tts:
    def __init__(self, work, synthesize, silent):
        self.cache = Path(work) / "tts"
        self.cache.mkdir(parents=True, exist_ok=True)
        self.key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
        self.silent = silent
        self.synth = bool(synthesize and self.key)
        if synthesize and not self.key and not silent:
            raise SystemExit("ERROR: synthesize=true but ELEVENLABS_API_KEY is not set (use --silent for a key-less test build)")
        if synthesize and not self.key:
            log("WARN: no ELEVENLABS_API_KEY -> silent audio")
        if not synthesize and not silent:
            raise SystemExit("ERROR: synthesize=false requires --silent (a video without audio is not produced otherwise)")
        self.voice_id = None
        self.n_api = 0

    def _req(self, method, url, **kw):
        import requests
        last = None
        for attempt in range(5):
            try:
                r = requests.request(method, url, headers={"xi-api-key": self.key, **kw.pop("headers", {})}, timeout=120, **kw)
                if r.status_code in (429, 500, 502, 503, 504):
                    last = f"HTTP {r.status_code}"
                    time.sleep(2 ** attempt * 2)
                    continue
                if r.status_code in (401, 403):
                    raise SystemExit(f"ERROR: ElevenLabs auth failed (HTTP {r.status_code}); check the ELEVENLABS_API_KEY secret")
                if r.status_code >= 400:
                    raise RuntimeError(f"ElevenLabs HTTP {r.status_code}: {r.text[:200]}")
                return r
            except (requests.ConnectionError, requests.Timeout) as e:
                last = str(e)
                time.sleep(2 ** attempt * 2)
        raise RuntimeError(f"ElevenLabs request failed after retries: {last}")

    def voice(self):
        if self.voice_id:
            return self.voice_id
        r = self._req("GET", f"{API}/voices").json()
        voices = r.get("voices", [])
        for v in voices:
            if v.get("name", "").strip().lower() == VOICE_NAME.lower():
                self.voice_id = v["voice_id"]
                return self.voice_id
        for v in voices:
            if v.get("name", "").lower().startswith(VOICE_NAME.lower()):
                self.voice_id = v["voice_id"]
                return self.voice_id
        raise SystemExit(f"ERROR: voice '{VOICE_NAME}' not found in account ({len(voices)} voices); add it to My Voices")

    def audio(self, text):
        """Return path to an audio file for `text` (mp3 from API, or wav silence)."""
        if self.synth:
            h = hashlib.sha256(f"{MODEL_ID}|{VOICE_NAME}|{text}".encode()).hexdigest()[:24]
            p = self.cache / f"{h}.mp3"
            if p.exists() and p.stat().st_size > 1000:
                return p
            vid = self.voice()
            r = self._req("POST", f"{API}/text-to-speech/{vid}", params={"output_format": "mp3_44100_128"},
                          json={"text": text, "model_id": MODEL_ID,
                                "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}},
                          headers={"Accept": "audio/mpeg"})
            if len(r.content) < 1000:
                raise RuntimeError("ElevenLabs returned a tiny audio payload")
            p.write_bytes(r.content)
            self.n_api += 1
            return p
        words = max(1, len(text.split()))
        dur = max(0.8, words / 2.3)
        h = hashlib.sha256(f"sil|{dur:.2f}".encode()).hexdigest()[:12]
        p = self.cache / f"sil-{h}.wav"
        if not p.exists():
            run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", f"anullsrc=r={SR}:cl=mono", "-t", f"{dur:.3f}", str(p)])
        return p


def to_wav(src, dst):
    run(["ffmpeg", "-y", "-v", "error", "-i", str(src), "-ac", "1", "-ar", str(SR), "-sample_fmt", "s16", str(dst)])
    return dst


def wav_len(p):
    with wave.open(str(p), "rb") as w:
        return w.getnframes() / w.getframerate()


# ---------------------------------------------------------------- timeline
def build_timeline(scenes, tts, work):
    """Returns (timeline, audio_wav_path). timeline: scenes with start/end and lines with start/end."""
    wdir = Path(work) / "wav"
    wdir.mkdir(parents=True, exist_ok=True)
    out = wave.open(str(Path(work) / "voice.wav"), "wb")
    out.setnchannels(1); out.setsampwidth(2); out.setframerate(SR)

    def silence(sec):
        out.writeframes(b"\x00\x00" * int(round(sec * SR)))

    t = 0.0
    silence(LEAD_IN); t += LEAD_IN
    tl = []
    for si, sc in enumerate(scenes):
        s_start = t if si else 0.0
        lines = []
        for li, ln in enumerate(sc["lines"]):
            text = ln.get("tts") or ln["de"]
            src = tts.audio(text)
            w = wdir / (src.stem + ".wav")
            if not w.exists():
                to_wav(src, w)
            with wave.open(str(w), "rb") as r:
                frames = r.readframes(r.getnframes())
                d = r.getnframes() / r.getframerate()
            out.writeframes(frames)
            lines.append({"start": t, "end": t + d, "ar": ln["ar"], "en": ln["en"], "de": ln["de"]})
            t += d
            if li < len(sc["lines"]) - 1:
                silence(LINE_GAP); t += LINE_GAP
        silence(SCENE_GAP); t += SCENE_GAP
        tl.append({"start": s_start, "end": t, "lines": lines})
    out.close()
    return tl, Path(work) / "voice.wav"


# ---------------------------------------------------------------- subtitles
def wrap2(text, width):
    """Balanced wrap into <=2 lines (\n separated) at word boundaries."""
    words = text.split()
    if len(text) <= width:
        return text
    best, bs = None, 1e9
    for i in range(1, len(words)):
        a, b = " ".join(words[:i]), " ".join(words[i:])
        score = max(len(a), len(b)) + (50 if max(len(a), len(b)) > width else 0)
        if score < bs:
            best, bs = a + "\n" + b, score
    return best or text


def split_cues(text, width):
    """Split a sentence-ish text into chunks of <= 2*width chars, preferring punctuation."""
    cap = width * 2
    text = " ".join(text.split())
    if len(text) <= cap:
        return [text]
    n = math.ceil(len(text) / cap)
    words = text.split()
    chunks, cur = [], []
    target = len(text) / n
    for i, w in enumerate(words):
        cur.append(w)
        cl = len(" ".join(cur))
        remaining = len(chunks) < n - 1
        punct = re.search(r"[.,;:!?؟،؛»)]$", w)
        nxt = len(words[i + 1]) + 1 if i + 1 < len(words) else 0
        if remaining and nxt and ((cl >= target * 0.8 and punct) or cl >= target * 1.1 or cl + nxt > cap):
            chunks.append(" ".join(cur)); cur = []
    if cur:
        chunks.append(" ".join(cur))
    return chunks


def make_cues(tl, lang):
    width = CUE_CHARS[lang]
    cues = []
    for sc in tl:
        for ln in sc["lines"]:
            parts = split_cues(ln[lang], width)
            tot = sum(len(p) for p in parts)
            start, end = ln["start"], ln["end"] + SUB_HOLD
            span = end - start
            a = start
            for p in parts:
                b = a + span * len(p) / tot
                cues.append((a, b, wrap2(p, width)))
                a = b
    return cues


def ts_srt(x):
    ms = int(round(x * 1000))
    return f"{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}"


def write_srt(cues, path):
    Path(path).write_text("".join(f"{i}\n{ts_srt(a)} --> {ts_srt(b)}\n{t}\n\n" for i, (a, b, t) in enumerate(cues, 1)), encoding="utf-8")


def ts_ass(x):
    cs = int(round(x * 100))
    return f"{cs//360000}:{cs//6000%60:02d}:{cs//100%60:02d}.{cs%100:02d}"


def write_ass(cues_ar, cues_en, path, ar_font, en_font):
    hdr = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: AR,{ar_font},50,&H00FFFFFF,&H00FFFFFF,&HB0201408,&HB0201408,0,0,0,0,100,100,0,0,3,12,0,2,120,120,190,178
Style: EN,{en_font},38,&H0080DFFF,&H0080DFFF,&HB0201408,&HB0201408,0,0,0,0,100,100,0,0,3,10,0,2,120,120,48,1

[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
"""
    ev = []
    for style, cues in (("AR", cues_ar), ("EN", cues_en)):
        for a, b, t in cues:
            ev.append((a, f"Dialogue: 0,{ts_ass(a)},{ts_ass(b)},{style},,0,0,0,,{t.replace(chr(10), chr(92) + 'N')}"))
    ev.sort(key=lambda x: x[0])
    Path(path).write_text(hdr + "\n".join(e for _, e in ev) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- video
def normalize_audio(wav, out_wav):
    """Two-pass loudnorm to -16 LUFS. Returns True if normalised, False if silent (copied)."""
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(wav), "-af",
                        "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True)
    m = re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r.stderr, re.S)
    stats = json.loads(m.group(0)) if m else None
    if not stats or stats["input_i"] in ("-inf", "inf") or float(stats["input_i"]) < -70:
        shutil.copy(wav, out_wav)
        return False
    af = (f"loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={stats['input_i']}:measured_TP={stats['input_tp']}:"
          f"measured_LRA={stats['input_lra']}:measured_thresh={stats['input_thresh']}:offset={stats['target_offset']}:linear=true")
    run(["ffmpeg", "-y", "-v", "error", "-i", str(wav), "-af", af, "-ar", "48000", str(out_wav)])
    return True


def write_concat(slide_paths, tl, path):
    lines = []
    for p, sc in zip(slide_paths, tl):
        lines.append(f"file '{Path(p).resolve()}'")
        lines.append(f"duration {sc['end'] - sc['start']:.3f}")
    lines.append(f"file '{Path(slide_paths[-1]).resolve()}'")   # concat demuxer quirk: repeat last
    Path(path).write_text("\n".join(lines) + "\n")


def encode(concat, audio, ass, out, burn, fontsdir):
    vf = [f"fps={FPS}", "format=yuv420p"]
    if burn:
        a = str(ass).replace("\\", "/").replace(":", "\\:").replace("'", "\\'")
        f = f":fontsdir={fontsdir}" if fontsdir else ""
        vf.insert(1, f"ass={a}{f}")
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(concat), "-i", str(audio),
         "-vf", ",".join(vf), "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-tune", "stillimage",
         "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(out)])


def contact_sheet(paths, out, cols=4, tw=480):
    from PIL import Image, ImageDraw
    th = tw * 9 // 16
    rows = math.ceil(len(paths) / cols)
    sheet = Image.new("RGB", (cols * (tw + 8) + 8, rows * (th + 8) + 8), (40, 40, 40))
    d = ImageDraw.Draw(sheet)
    for i, p in enumerate(paths):
        im = Image.open(p).convert("RGB").resize((tw, th), Image.LANCZOS)
        x, y = 8 + (i % cols) * (tw + 8), 8 + (i // cols) * (th + 8)
        sheet.paste(im, (x, y))
        d.rectangle([x, y + th - 22, x + 34, y + th], fill=(0, 0, 0))
        d.text((x + 6, y + th - 17), str(i + 1), fill=(255, 255, 255))
    sheet.save(out)


def build(script, args):
    d = json.loads(Path(script).read_text(encoding="utf-8"))
    vid = d["id"]
    work = Path(args.work) / vid
    out = Path(args.out) / vid
    for p in (work, out):
        p.mkdir(parents=True, exist_ok=True)
    scenes = d["scenes"]
    log(f"[{vid}] {len(scenes)} scenes")

    log(f"[{vid}] rendering slides")
    sl_paths, overflow = slidemod.render_slides(scenes, work / "slides")
    log(f"[{vid}] slide issues: {len(overflow)}")

    log(f"[{vid}] audio")
    tts = Tts(work, args.synthesize, args.silent)
    tl, voice = build_timeline(scenes, tts, work)
    total = tl[-1]["end"]

    cues = {l: make_cues(tl, l) for l in ("ar", "en", "de")}
    for l in cues:
        write_srt(cues[l], out / f"{vid}.{l}.srt")
    warns = qamod.speed_warnings(cues["ar"], "ar") + qamod.speed_warnings(cues["en"], "en")

    ar_font = slidemod.pick_font(["Noto Naskh Arabic", "Noto Sans Arabic", "Amiri", "DejaVu Sans", "FreeSerif"])
    en_font = slidemod.pick_font(["Noto Sans", "Inter", "DejaVu Sans"])
    ass = work / f"{vid}.ass"
    write_ass(cues["ar"], cues["en"], ass, ar_font, en_font)
    log(f"[{vid}] fonts: AR={ar_font} EN={en_font}")

    norm = work / "voice-norm.wav"
    normalized = normalize_audio(voice, norm)
    concat = work / "concat.txt"
    write_concat(sl_paths, tl, concat)
    mp4 = out / f"{vid}.mp4"
    log(f"[{vid}] encoding {total:.0f}s")
    encode(concat, norm, ass, mp4, args.burn, None)
    contact_sheet(sl_paths, out / "contact-sheet.png")

    qa = {"id": vid, "rev": args.rev, "duration_s": round(qamod.duration(mp4), 2), "lufs": qamod.lufs(mp4),
          "synthesized": bool(tts.synth), "burned": bool(args.burn), "scenes": len(scenes),
          "tts_api_calls": tts.n_api, "fonts": {"ar": ar_font, "en": en_font},
          "subtitle_speed_warnings": warns, "overflow_issues": overflow,
          "subtitle_cues": {l: len(c) for l, c in cues.items()}}
    (out / "qa.json").write_text(json.dumps(qa, ensure_ascii=False, indent=1), encoding="utf-8")
    log(qamod.summarize(qa))
    return qa


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--script", action="append", default=[])
    ap.add_argument("--run", help="pipeline/run.json")
    ap.add_argument("--index", type=int, help="with --run: build only video #index")
    ap.add_argument("--synthesize", action="store_true", default=None)
    ap.add_argument("--no-synthesize", dest="synthesize", action="store_false")
    ap.add_argument("--burn", action="store_true", default=None)
    ap.add_argument("--no-burn", dest="burn", action="store_false")
    ap.add_argument("--silent", action="store_true", help="allow silent audio when not synthesizing / no key")
    ap.add_argument("--rev", type=int, default=None)
    ap.add_argument("--out", default=str(ROOT / "out"))
    ap.add_argument("--work", default=str(ROOT / "work"))
    args = ap.parse_args()
    scripts = list(args.script)
    if args.run:
        rj = json.loads(Path(args.run).read_text(encoding="utf-8"))
        vids = rj.get("video", [])
        scripts += [vids[args.index]] if args.index is not None else vids
        if args.synthesize is None: args.synthesize = rj.get("synthesize", True)
        if args.burn is None: args.burn = rj.get("burn", True)
        if args.rev is None: args.rev = rj.get("rev", 1)
    args.synthesize = True if args.synthesize is None else args.synthesize
    args.burn = True if args.burn is None else args.burn
    args.rev = args.rev or 1
    if not scripts:
        sys.exit("no scripts given")
    for s in scripts:
        build(ROOT / s if not os.path.isabs(s) else s, args)


if __name__ == "__main__":
    main()
