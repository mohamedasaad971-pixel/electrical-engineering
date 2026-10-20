#!/usr/bin/env python3
"""Audio check: transcribe the narration with Whisper (open source, CPU, free) and compare it with the script.

Runs only for synthesized builds. Flags scenes whose transcript differs a lot from the script
(possible mispronunciation, truncated audio, wrong language). It cannot judge voice beauty.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_audio(path):
    """Decode to 16 kHz mono float32 with ffmpeg (avoids PyAV version problems)."""
    import wave
    import numpy as np
    tmp = Path(str(path) + ".16k.wav")
    subprocess.run(["ffmpeg", "-y", "-i", str(path), "-vn", "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le", str(tmp)],
                   check=True, capture_output=True)
    with wave.open(str(tmp), "rb") as w:
        data = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
    tmp.unlink()
    return data


def norm(t):
    t = t.lower().replace("ß", "ss")
    return re.sub(r"[^a-z0-9äöüé]", "", t)


def words(t):
    t = t.lower().replace("-", "")
    return re.findall(r"[a-z0-9äöüß]+", t)


def lev(a, b):
    prev = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        cur = [i]
        for j, y in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (x != y)))
        prev = cur
    return prev[-1]


def audition_check():
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "faster-whisper"], check=True)
    from faster_whisper import WhisperModel
    model = WhisperModel("small", device="cpu", compute_type="int8")
    adir = ROOT / "out" / "audition"
    meta = json.loads((adir / "audition.json").read_text(encoding="utf-8"))
    ref = " ".join(meta["texts"])
    res = []
    for v in meta["voices"]:
        segs, _ = model.transcribe(load_audio(adir / v["file"]), language="de", vad_filter=True, beam_size=5)
        hyp = " ".join(s.text for s in segs)
        rw, hw = words(ref), words(hyp)
        cer = lev(list(norm(ref)), list(norm(hyp))) / max(1, len(norm(ref)))
        wer = lev(rw, hw) / max(1, len(rw))
        res.append({"name": v["name"], "id": v["id"], "cer": round(cer, 3), "wer": round(wer, 3), "hyp": hyp[:400]})
    res.sort(key=lambda r: r["cer"])
    (adir / "audition_check.json").write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    for r in res:
        print(f"audition: {r['name']:<45} cer={r['cer']:.3f} wer={r['wer']:.3f}")


def main():
    run = json.loads((ROOT / "pipeline" / "run.json").read_text(encoding="utf-8"))
    import os as _os
    if run.get("action") == "audition":
        if _os.environ.get("VIDEO_INDEX", "0") in ("", "0"):
            audition_check()
        return
    if run.get("action") != "build" or not run.get("synthesize"):
        print("audio_check: build is not synthesized; skipped")
        return
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "faster-whisper"], check=True)
    from faster_whisper import WhisperModel
    model = WhisperModel("small", device="cpu", compute_type="int8")
    vids = run["video"] if isinstance(run["video"], list) else [run["video"]]
    import os
    idx = os.environ.get("VIDEO_INDEX", "")
    if idx != "":
        vids = [vids[int(idx)]] if int(idx) < len(vids) else []
    for vp in vids:
        script = json.loads((ROOT / vp).read_text(encoding="utf-8"))
        vid = script["id"]
        out = ROOT / "out" / vid
        rep = json.loads((out / "report.json").read_text(encoding="utf-8"))
        audio = load_audio(out / f"{vid}.clean.mp4")
        segs, _ = model.transcribe(audio, language="de", vad_filter=True, beam_size=5, word_timestamps=True)
        ws = [(w.start, w.end, w.word) for s in segs for w in (s.words or [])]
        res = []
        scenes = script["scenes"]
        for si, info in enumerate(rep["scenes"]):
            ref = " ".join((ln.get("tts") or ln["de"]) for ln in scenes[si]["lines"])
            hyp = " ".join(w for st, en, w in ws if info["start"] - 0.3 <= st < info["end"])
            rw, hw = words(ref), words(hyp)
            wer = lev(rw, hw) / max(1, len(rw))
            rc, hc = norm(ref), norm(hyp)
            cer = lev(list(rc), list(hc)) / max(1, len(rc))
            res.append({"scene": info["id"], "wer": round(wer, 3), "cer": round(cer, 3),
                        "flag": cer > 0.35 or wer > 0.5, "hyp_excerpt": hyp[:160], "ref_excerpt": ref[:160]})
        (out / "audio_check.json").write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
        flagged = [r for r in res if r["flag"]]
        print(f"{vid}: audio check scenes={len(res)} flagged={len(flagged)} "
              f"mean_cer={sum(r['cer'] for r in res)/max(1,len(res)):.3f}")
        for r in flagged:
            print("  FLAG scene", r["scene"], "cer", r["cer"], "wer", r["wer"], "|", r["hyp_excerpt"])


if __name__ == "__main__":
    main()
