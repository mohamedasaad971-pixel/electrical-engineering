# Applied audit findings: E-F05 (scripts/E/05-sicherheit.json)

Legend: A = applied, M = modified (corrected variant), R = rejected. S = scene, L = line. "F" = facts finding, "G" = language finding.

| Finding | Result | Reason |
|---|---|---|
| F S5.10 AR lost norm name | A | AR now names DIN VDE 0105-100 |
| F S7.2 AR lost norm number | A | AR names the norm, section and edition |
| F S14.2 AR lost AuS | A | "بالرمز AuS في الألمانية" |
| F S14.10 AR lost DGUV Regel 103-011 | A | Identifier restored (not at line edge) |
| F S17.1 AR lost PSA | A | PSA named |
| F S17.4 AR lost DGUV Information 203-077 | A | Identifier restored |
| F S19.1 AR lost BG ETEM | A | Named |
| F S5.4 (+13.3, 15.1, 22.3) "اللائحة الثالثة" | M | TERMS.md form used: لائحة الوقاية من الحوادث رقم ٣ (DGUV V3), also in title |
| F S7.2 Normstand/draft | M | Draft-edition claim is not in the research file, so it is not stated. Script says "Ausgabe 2015, Abschnitt 6.2; check current version". Draft moved to dropped and to stand |
| F S8.10 sign alone not enough | A | Applied, slide item 4 adjusted |
| F S9.3 "allpolig" | A | Added to heading, line, items, S7 list. Not in research facts, so flagged for primary-source check |
| F S9.4 qualified person / tester | M | "befähigte" not used (it is a legal term); "ausgebildete Person", "Spannungsprüfer"; multimeter/EN 61243-3 claim not adopted (dropped) |
| F S11/S12 who releases | M | No person named in slide items or lines S10.6/S12.4 (unsupported); S11 item replaced by "Vorher prüfen: niemand arbeitet mehr" |
| F S18.5 high voltage distance | A | Applied (consistent with the "Selbstschutz" fact); flagged for check |
| F S19.6 BG overgeneralised | A | Replaced by sector-dependence statement |
| F S1.4 Elektrofachkraft AR | M | TERMS.md term الكهربائي المؤهَّل (not "فني"/"فنيين") with (Elektrofachkraft); also S13, S15.9, S18.5, glossary |
| F S3.11 arc fault EN | A | "fault arc (arc flash)", also term, glossary, S17.2 |
| F S4.5 higher voltage | A | Line deleted (G suggestion to rewrite would add an unsupported claim) |
| F S6.4 TTS Ce-E | A | Ze-E |
| F S8.2 allseitig | A | In line; AR/EN equivalent |
| F S13 "Unterweisung regelmäßig erneuern" | A | "Unterweisung im Betrieb" |
| F S14.7 selten und gut vorbereitet | A | Replaced by "Regeln gelten bis 1 kV Wechselspannung" (in research) |
| F S15.2 employer / صاحب العمل | M | EN "employer" applied; AR keeps صاحب المنشأة (TERMS.md: Unternehmer) |
| F S15.6 EN "and fires" | A | Removed |
| F S16.6 braucht | A | "kann ... brauchen" |
| G S1.4 AR Latin edge | M | TERMS term, Latin in middle, line ends in Arabic |
| G S2.0 Unterweisung term | M | التوجيه والتعليمات (Unterweisung) per TERMS.md (not إرشاد) |
| G S5.4 TTS "Die" / S15.1 TTS | A | Fixed |
| G S5.4 AR DGUV rendering | M | TERMS.md form |
| G S5.10 AR المذكور | A | Fixed (also S7.2, S14.2, S14.10, S17.4) |
| G S7.2 AR | M | Fixed with edition and section; digits in middle |
| G S7.3 logic | A | "spannungsfrei gemacht werden" DE/AR/EN |
| G S12.6 AR grammar | A | يُعاد |
| G S13.4 AR Latin edge | M | Reworded, ends in Arabic |
| G S13.6 previous video | A | DE/AR/EN: "im vorigen Video" (F04 covers EFK) |
| G S14.1 plural | A | "Arbeiten ... sind", S14.3 plural |
| G S14.2 AR AuS | A | See F |
| G S14.10 AR | A | See F |
| G S15.2 AR صاحب العمل | R | Contradicts binding TERMS.md (Unternehmer = صاحب المنشأة) |
| G S15.2 EN employer | A | See F |
| G S15.6 EN | A | See F |
| G S17.1 AR PSA | A | See F |
| G S17.4 DE dative | A | "Bei der richtigen Auswahl hilft die DGUV Information 203-077", TTS/AR/EN aligned |
| G S17.8 TTS | A | Same order as de |
| G S19.1 AR BG ETEM | A | See F |
| G S20.0 term مخطط كهربائي | M | TERMS.md: مخطط الدارات |
| G S20.2 logic | A | Both requirements, DE/AR/EN |
| G S0 title DGUV | M | TERMS.md form |
| G S0 glossary articles | A | Articles added (das/die/der); AuS and PSA in brackets |
| G S2.4 AR Unterweisung | M | TERMS.md term |
| G S3.11 order | M | Line moved to after the burns line (new position 7) |
| G S4.5 rewrite | R | Rewrite adds an unsupported claim; line deleted instead (F finding) |
| G S5.10 TTS "null-einhundertfünf, Teil einhundert" | A | With DIN as "Din"; DE now "DIN VDE 0105-100" (S5 item too) |
| G S6.2 EN he/they | A | "the employer derives" |
| G S6.4 TTS | A | Ze-E |
| G S6.6 AR | A | نسأل |
| G S7.7 list rules | A | Rules listed aloud (with allpolig) |
| G S8.0 Schutzschalter | A | "Leitungsschutzschalter" |
| G S8.2 AR قاطع حماية الخط | M | TERMS.md: القاطع الآلي |
| G S8.4 AR | A | تأمين ... ضد |
| G S13.0 / 13.2 / 13.3 / S15.1 / S15.9 / S18.5 AR Elektrofachkraft | M | TERMS.md: الكهربائي المؤهَّل (Elektrofachkraft) instead of شخص مؤهَّل كهربائيًا |
| G S17.4 AR | A | See F |
| G S18.8 AR defibrillator | A | جهاز إزالة الرجفان (الصادم الكهربائي) |
| G S18.11 delete | A | Deleted |
| G S20.2 AR موسومة | A | معلَّمة |
| G S21.6 AR | A | Applied |
| G S22.3 / S22.7 AR | M | TERMS.md DGUV V3 and التوجيه والتعليمات (Unterweisung) |
| G S1.1 Folge to Video | A | Also kicker "E-F05 · Grundlagen" and next pointer |
| G S2.9 / S2.5 shorten | M | S2.9 deleted; S2.5 (current rules) kept as a distinct disclaimer, S22.5 kept |

Other changes: quiz answers varied (1,2,0,1,2) by reordering options; `next` points to E-F06 (Schaltpläne, Symbole und Kennzeichnung); unqualified AR terms normalised to TERMS.md (القاطع الآلي, المنصهرات, المعايير, دارة كهربائية); `stand` updated; six claims added to `dropped` in docs/research/E-F05.json.
