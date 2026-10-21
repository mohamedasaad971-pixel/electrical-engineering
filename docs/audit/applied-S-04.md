# Applied audit findings: S-04 (scripts/E/04-simulation.json)

Legend: A = applied, M = modified (corrected variant), R = rejected. S = scene, L = line. "F" = facts finding, "G" = language finding. Scene numbers refer to the original script numbering.

| Finding | Result | Reason |
|---|---|---|
| F S1.6 "nur wenige Minuten" | A | Replaced by "Das Thema ist wichtig, denn ..." (merged with 1.7, 1.7 deleted), DE/AR/EN |
| F S12.4 nonsense sentence | A | Fact-audit wording ("trainiert Ihr Verständnis der Rechenabläufe") used instead of the language-audit variant |
| F S10.5 SPICE core claim | M | "arbeitet nach dem SPICE-Prinzip; SPICE ist ein Programm der Universität Berkeley aus den siebziger Jahren"; slide card "Arbeitsweise nach dem SPICE-Prinzip"; moved to dropped and stand |
| F S1.5 / S20.5 / slide 20 frei vs kostenlos | A | "kostenlose und freie Werkzeuge", LTspice "laut Hersteller kostenlos" (AR per TERMS: مجاني حسب الشركة المصنّعة), Octave "freie Software"; summary slide and 20.5 adjusted, slide 1 item adjusted |
| F S10.1 / S12.3 / S13.8 / S18.9 "bekannt/الشهير/المعروف" | A | Removed in 10.1, 12.3, 13.8 (18.9 contained none); no popularity claims remain |
| F S10.7 help explains commands well | A | Line deleted |
| F S19.8 measuring / Elektrofachkraft | M | Applied with TERMS wording (Elektrofachkraft oder unter Leitung und Aufsicht) and a pointer to the five safety rules (not shortened); AR with الكهربائي المؤهَّل; slide item "Im Zweifel prüfen und fragen". "mit den fünf Sicherheitsregeln" is not in the research file: check |
| F S0 next "خطوة بخطوة" | A | Removed; next now names the S-05 title, no ID |
| F S19.7 / S20.7 Germany generalisations | A | 19.7 rewritten ("So bleibt Ihre Arbeit nachvollziehbar"), 20.7 deleted |
| F S12.7 / S13.8 / S13.5 | A | 12.7 clarified (Grundideen dieser Sprachen); 13.8 qualified with compatibility limits and moved before 13.5 |
| F S4.6 order | A | See G S4.5 (same move) |
| F S15.5 AR gender | A | يصل الجهد |
| F S16.8 "ist alles plausibel" | A | "spricht das für ein plausibles Ergebnis", DE/AR/EN |
| F S18.4 non-sequitur | A | "Dazu kommen Einflüsse von Wärme, Alterung und mechanischer Belastung" (AR/EN equivalent) |
| F S12.9 licences hold (note, no fix) | A | No change needed; stand keeps primary-source check |
| G S15.5 AR gender | A | Same as above |
| G S4.5 order | A | Lines now 4.4, 4.6, 4.5, 4.7 |
| G S0 glossary / S7 term Solver AR | M | "المحلِّل العددي" in glossary, slide terms, title, lines 1.4, 4.5, 7.1-7.9, 8.3, 11.6, 20.3 and quiz 1; "(Solver)" kept mid-sentence in 1.4 and 7.1 |
| G S0 quiz 4 Latin edges | A | Question and options 1 and 3 ended in Arabic (شركة ... المصنّعة) |
| G S11.9 كلاهما منتجان | A | "كلاهما من منتجات شركة MathWorks، وكلاهما يحتاج إلى ترخيص" |
| G S0 next pointer | M | Next names "Lichtplanung am Rechner mit DIALux" (title of S-05) with TERMS term تخطيط الإضاءة (instead of the suggested تخطيط الإنارة); AR ends with Arabic word; line 21.8 aligned |
| G S1.6 duration | A | See F S1.6 |
| G S1.5 frei vs kostenlos | A | See F S1.5 |
| G S4.9 etc. Regelkreis = حلقة التحكم | A | "حلقة/حلقات التنظيم" in 4.9, 7.5, 11.4, quiz 4 |
| G S6.6 معامل vs عامل | A | خطأ بعامل ألف |
| G S9.4 order | A | 9.4 moved after 9.6 (before 9.7) |
| G S10 kicker / card | A | Kicker "Kostenloses Werkzeug"; card "Arbeitsweise nach dem SPICE-Prinzip" (not "SPICE-Rechenkern", see F S10.5) |
| G S10.5 double "aus" | A | Fixed in the rewritten line |
| G S11.3 repeated verb | A | "Dort erstellen Sie ein Modell aus Blöcken" |
| G S12.3 stilted | A | "Seine Sprache ähnelt der von MATLAB weitgehend"; AR rewritten so it does not end with a Latin word |
| G S12.4 non sequitur | A | See F S12.4 |
| G S12.8 AR grammar / S12.9 order | A | "اسألوا عن الملفات ..."; order 12.6, 12.9, 12.7, 12.8 |
| G S13.8 order | A | Moved before 13.5 |
| G S14.2 مُختلقة | A | "أمثلة افتراضية من وضعنا"; slide item "Alle Werte sind Beispielwerte" |
| G S14.4 digits in de | A | Digits and units in de (14.4, 14.5, 15.3, 15.5, 15.6, 15.9, 16.8, slide 14) with spelled tts; quiz text left in words (no tts field) |
| G S17.5 order | M | 17.5 moved before 17.9; additionally 17.8 moved to the end so "Danach testen Sie Grenzfälle" follows 17.7 naturally |
| G S18.4 non sequitur | A | See F S18.4 |
| G S21.7 order | A | Quiz call to action now after the next-video line |
| G S21.8 tts DIALux | A | "Di-A-Lux" (S-05 not edited here) |
| G S11.3 etc. product tts | A | Simu-Link, Mäth-Wörks, Sai-Läb, Iks-Kos, Änalog Dewaisis; tts derived from de in content and order |
| G S4 table duplicate keys | A | Rows: Schaltung / System / Beispiel Schaltung / Beispiel System, each ≤50 chars |
| G S0 quiz distractors | A | Q1 "Er wählt die Bauteile aus", Q3 "Länge der Leitung im Modell", Q5 "Etwa die Hälfte des Endwerts"; exactly one correct each, answers 2,0,1,2,0 |
| G S2.8 الجهة المصنِّعة | A | الشركة المصنّعة (also 10.2, 10.3) |
| G S15.7 order | A | Moved to the end of scene 15 |
| G S16.5 AR subject | A | وإذا كانت الخطوة صغيرة جدًا |
| G S0 glossary Sprungantwort unused | A | New line 15.x "Diesen Verlauf nennt man Sprungantwort." (DE/AR/EN) |

Rejected: none.

Further changes: slide 1 kicker "S-04 · Software" (internal ID) changed to "Software-Reihe, Video 4"; slide 1 item "Kostenlose, freie, kommerzielle Werkzeuge"; `stand` extended; seven claims added to "dropped" in docs/research/S-04.json (plus `stand_note`).

Validator: tools/validate.py scripts/E/04-simulation.json reports 0 issues.
