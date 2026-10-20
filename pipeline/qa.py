#!/usr/bin/env python3
"""QA helpers: duration, integrated loudness (pyloudnorm), subtitle speed, overflow summary.

Usage: python pipeline/qa.py out/E-F01      (prints summary of out/E-F01/qa.json, exit 1 on problems)
"""
import json, subprocess, sys, tempfile
from pathlib import Path

MAX_CPS = 20.0          # chars per second limit for AR/EN
TARGET_LUFS = -16.0
LUFS_TOL = 1.5


def duration(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)],
                       capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        raise RuntimeError(f"ffprobe failed for {path}: {r.stderr.strip()}")


def lufs(path):
    """Integrated loudness of the audio in `path` (any media). None if silent/too short."""
    import numpy as np, soundfile as sf, pyloudnorm as pyln
    with tempfile.TemporaryDirectory() as td:
        wav = Path(td) / "a.wav"
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(path), "-vn", "-ac", "2", "-ar", "48000", str(wav)], check=True)
        data, rate = sf.read(str(wav))
    if len(data) < rate * 0.5 or float(np.max(np.abs(data))) < 1e-5:
        return None
    v = pyln.Meter(rate).integrated_loudness(data)
    return None if v != v or v == float("-inf") else round(float(v), 2)


def speed_warnings(cues, lang, max_cps=MAX_CPS):
    """cues: list of (start, end, text). Return warnings for cues above max_cps."""
    out = []
    for n, (a, b, t) in enumerate(cues, 1):
        chars = len(t.replace("\n", " ").strip())
        cps = chars / max(b - a, 0.01)
        if cps > max_cps:
            out.append({"lang": lang, "cue": n, "start": round(a, 2), "cps": round(cps, 1), "text": t.replace("\n", " ")[:60]})
    return out


def summarize(qa):
    lines = [f"{qa.get('id','?')}: duration {qa.get('duration_s')} s, LUFS {qa.get('lufs')}"]
    sw = qa.get("subtitle_speed_warnings", [])
    ov = qa.get("overflow_issues", [])
    lines.append(f"subtitle lines > {MAX_CPS:.0f} chars/s: {len(sw)}")
    for w in sw[:10]:
        lines.append(f"  [{w['lang']}] #{w['cue']} @{w['start']}s {w['cps']} cps: {w['text']}")
    lines.append(f"slide overflow/DOM issues: {len(ov)}")
    for o in ov[:10]:
        lines.append(f"  scene {o['scene']}: {o['issue']}")
    if qa.get("synthesized") is False:
        lines.append("NOTE: audio is silence (not synthesized); LUFS not meaningful")
    return "\n".join(lines)


def problems(qa):
    p = []
    if qa.get("subtitle_speed_warnings"):
        p.append("subtitle speed")
    if qa.get("overflow_issues"):
        p.append("overflow")
    if qa.get("synthesized") and qa.get("lufs") is not None and abs(qa["lufs"] - TARGET_LUFS) > LUFS_TOL:
        p.append("loudness")
    return p


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    d = Path(sys.argv[1])
    qa = json.loads((d / "qa.json").read_text(encoding="utf-8"))
    print(summarize(qa))
    pr = problems(qa)
    print("PROBLEMS: " + ", ".join(pr) if pr else "OK")
    sys.exit(1 if pr else 0)
