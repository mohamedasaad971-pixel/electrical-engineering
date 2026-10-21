# Applied audit findings: S-02 (scripts/E/02-tia-codesys.json)

Legend: F = facts finding, G = language finding; S = scene, L = line (1-based; S9 lines after L6 shifted by +1 because of the new rules line). A = applied, M = modified, R = rejected.

| Finding | Result | Reason |
|---|---|---|
| F S4.3 "wie im ersten Video" (+6.8, 17.8) | M | TERMS: no internal IDs in speech. 4.3 names the video by title (Grundlagen der Automatisierung und SPS, DE/AR/EN/tts). 6.8 and 17.8 do not point to E-C01: it does not cover comments or exercises. 6.8 now a standalone maintenance line, 17.8 "Aufgaben mit eigenen Beispielen und Zahlen" |
| F S7.6 IEC 61131-3 edition 2013 vs 2025 | A | Fact copied from E-C01 research; "laut Quellen", tools may still support AWL; slide row "gilt als veraltet" |
| F S11.0 table marketing rows | M | Vorteil row deleted, "Geräte" row neutral ("Je nach Produkt"); summary items replaced by "Zwei Ansätze, gleiche Aufgabe" (one item) |
| F S11.3 "DIE Engineering-Umgebung" | A | "eine Engineering-Umgebung" DE/AR/EN |
| F S14.6 TIA multi-user / VCI | A | "laut Fachquellen", check scope and licence |
| F S9.6 five rules not listed | A | New line 9.7 with all five rules incl. allpolig (DE/AR/EN) |
| F S2.1 absolute | A | "meist" DE/AR/EN/tts |
| F S14.5 CODESYS SVN | A | "gibt es eine Anbindung", scope and licence to check |
| F S1.4 "in allen Werkzeugen" | A | "in vielen" DE/AR/EN |
| F S10.2 simulation extra software | A | Added "kann zusätzliche Software nötig sein" DE/AR/EN/tts |
| F S16.2 OpenPLC | M | "laut Fachquellen ... auf Basis von" (source is a secondary 2022 article, not the project page); slide item "Zum Üben gedacht, Einsatz prüfen" |
| F S9.5 EN Elektrofachkraft / AR DGUV | A | "qualified electrician"; AR with TERMS form (رقم ٣) |
| F S0 NEXT/19.7 TTS ETAP | A | "E-Täp", also "Dig-Sailent", "Pandapauer" as in S-03 |
| F S17.6 grammar | A | "beachten Sie die Lizenzbedingungen" |
| F S7.3 AR Funktionsplan | A | مخطط الكتل الوظيفية |
| G S5.8 AR gender | A | وهذا هو الجسر |
| G S0.4 quiz 4 Latin edge | A | CODESYS moved to the middle |
| G S0 EN Elektrofachkraft (9.5, 9.8) | A | qualified electrician |
| G S4.3 wrong cross-reference | M | See F S4.3 (title instead of ID) |
| G S0 title | A | AR/EN titles as suggested (no ranking, no Latin edge) |
| G S1.2/1.7/2.1 SPS in AR/EN | A | AR uses TERMS term; EN "PLC" (1.2 adds "called SPS in Germany") |
| G S1.5 padded AR | A | "نذكر هنا برنامجي ... كمثالين" |
| G S6.5, 11.5, 16.2 filler "للغات" | A | Removed, sentences end in Arabic |
| G S11.3 convoluted AR | A | Rewritten (combined with the fact fix) |
| G S7.2/7.3/7.5 AR terms | A | مخطط مسار التيار, الكتل الوظيفية, النص المنظَّم |
| G S6.3 function block AR | A | كتلة وظيفية (glossary, slide term, 6.3) |
| G S5.2 symbolic naming AR | A | التسمية الرمزية (glossary, term, 5.2, quiz 2) |
| G S9.5 AR DGUV/Leitung | A | رقم ٣, إدارته وإشرافه (TERMS binds the Arabic-Indic digit) |
| G S9.6 AR safety rules | A | قواعد السلامة الخمس |
| G S12.7 AR grammar | A | اسألوا عن الأداة المقرّرة |
| G S17.6 DE syntax | A | See F S17.6 |
| G S18.7 AR colloquial | A | أشخاص مؤهَّلين |
| G S19.7 AR omitted tool names / next.ar | A | Tool names added mid-sentence, ends in Arabic; next also names the real title of S-03 (Netzberechnung am Rechner) |
| G S19.7 tts ETAP/DIgSILENT | A | See F |
| G S0 EN US vs UK spelling | A | fulfils, authorisation (line + quiz), Practise, licence(s), summarise |
| G S16.5 Raspberry Pi tts | A | "Raspberri Pai" |
| G S7 slide rows >50 | A | Rows shortened ("wie Hochsprache", "gilt als veraltet") |
| G S11 row 53 chars | A | Row deleted (see F S11.0) |
| G S0 glossary herstellerunabhängig | A | die Herstellerunabhängigkeit / الاستقلال عن الشركة المصنّعة, also slide term |
| G S0 glossary Baugruppe AR | A | الوحدة العتادية (also 3.2, 4.2, S4 term) |
| G S0 quiz 1 and 4 | A | Option "Schutzeinstellungen für ein Netz berechnen"; Q4 correct option reworded; answers [1,0,2,1,2], one correct each |
| G S1.1 Serie vs Reihe | A | Software-Reihe (line and kicker) |
| G S0 digits mix | R | Western digits kept for years/standards; only the TERMS-fixed "رقم ٣" uses Arabic-Indic |
| G S5.1 redundant tts | A | Removed everywhere tts equals de |

Other: next pointer chain (S-02 to S-03, real title) fixed. research S-02.json: 5 claims moved to "dropped", IEC 2025 fact added (copied from E-C01); `stand` updated. validate.py: 0 issues.
