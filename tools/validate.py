#!/usr/bin/env python3
"""Check E-series script JSON files against the layout limits in docs/PLAN.md."""
import json, re, sys

LATIN_OR_DIGIT = re.compile(r"[A-Za-z0-9]")
PUNCT = ".,:;!?\u060c\u061b\u061f\"'\u00ab\u00bb\u201c\u201d()[]-\u2013\u2014 "
NEEDS_TTS = re.compile(r"\d|\b[A-ZÄÖÜ]{2,}[A-Za-zÄÖÜ0-9-]*\b|\b(?:DIN|VDE|IEC|EN|ISO)\b")

def check(path):
    errs = []
    try:
        d = json.load(open(path, encoding="utf-8"))
    except Exception as e:
        return [f"JSON parse error: {e}"]
    for k in ("id", "title", "scenes", "glossary", "quiz", "next", "stand"):
        if k not in d:
            errs.append(f"missing key {k}")
    words = 0
    for i, sc in enumerate(d.get("scenes", []), 1):
        s = sc.get("slide", {})
        lay = s.get("layout", "")
        if len(s.get("heading", "")) > 52: errs.append(f"scene {i}: heading >52")
        if len(s.get("kicker", "")) > 40: errs.append(f"scene {i}: kicker >40")
        items = s.get("items", [])
        cap = 4 if lay == "cards" else 6 if lay == "table" else 5
        if len(items) > cap: errs.append(f"scene {i}: {len(items)} items > {cap}")
        for it in items:
            t = it if isinstance(it, str) else json.dumps(it, ensure_ascii=False)
            if lay != "table" and len(t) > 50: errs.append(f"scene {i}: item >50: {t[:30]}")
        if len(s.get("terms", [])) > 3: errs.append(f"scene {i}: terms >3")
        for j, ln in enumerate(sc.get("lines", []), 1):
            for l in ("de", "ar", "en"):
                if not ln.get(l, "").strip(): errs.append(f"scene {i} line {j}: empty {l}")
            ar = ln.get("ar", "").strip().strip(PUNCT).strip()
            if ar and (LATIN_OR_DIGIT.match(ar[0]) or LATIN_OR_DIGIT.match(ar[-1])):
                errs.append(f"scene {i} line {j}: Arabic edge Latin/digit: {ar[:20]}")
            if NEEDS_TTS.search(ln.get("de", "")) and not ln.get("tts"):
                errs.append(f"scene {i} line {j}: missing tts: {ln['de'][:40]}")
            words += len(ln.get("tts", ln.get("de", "")).split())
    if not 4 <= len(d.get("quiz", [])) <= 5: errs.append("quiz should have 4-5 questions")
    return errs, words

if __name__ == "__main__":
    bad = 0
    for p in sys.argv[1:]:
        r = check(p)
        if isinstance(r, list): errs, words = r, 0
        else: errs, words = r
        print(f"{p}: {len(errs)} issues, ~{words} words")
        for e in errs: print("  -", e)
        bad += bool(errs)
    sys.exit(1 if bad else 0)
