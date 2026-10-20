# Applied findings E-F06 (scripts/E/06-schaltplaene.json)

Legend: A = applied, M = modified variant, R = rejected. Fact = facts-E-F01-07.json, Lang = language-E-F01-07.json. Scene.line, 1-based, line numbers as in the original script.

| Finding | Result | Reason |
|---|---|---|
| Fact 16.3 DIN EN 81346-2 -> DIN EN IEC | A | Fixed in DE/AR/EN/TTS, matches slide and F11 |
| Fact 2.5 plan = contract | M | Replaced by "often part of delivered documents, shows what was built" (Lang variant "Nachweis" not used, to avoid a new claim) |
| Fact 7.4 Lageplan | A | Anordnungsplan in line, slide heading and item, AR "مخطط الترتيب" |
| Fact 9.3 IEC DB paid | A | "kostenpflichtig ... mit Suche", "Filtern" removed; Q4 option now "offiziellen" database |
| Fact 10.1 IEC 61082 overclaim | A | Rephrased to IEC 61082-1 general rules; old line 10.2 deleted as duplicate |
| Fact 10.5 worldwide readable | A | "international abgestimmt", 10.7 softened, slide item changed |
| Fact 14.6 unsourced quote | A | Line deleted |
| Fact 15.4 60445 attribution | A | General rules only, numbers per data sheet; slide items "Häufig ...", "Allgemein: 60445" |
| Fact 1.4 | A | Via Lang 1.4 (learning goal sentence) |
| Fact 2.6 | A | Now "oft mit Plänen arbeiten" |
| Fact 4.2 / 4.7 | A | "meist einpolig", "oft"; slide item also softened |
| Fact 5.4 / 8.7 superlatives | A | "zentrales Dokument", "oft gebraucht" |
| Fact 5.5 | A | "wird gezeichnet" |
| Fact 6.3 EN/AR terms | A | Unified "combined/split presentation"; AR allpolig = متعدد الخطوط (Lang), see Lang 5 |
| Fact 8.4 Anschlussplan | A | Sentence reduced to "terms are not always the same" |
| Fact 9.2 DIN EN 60617 status | M | "in Deutschland als DIN EN 60617 übernommen. Prüfen Sie den Stand." (dropped list + stand updated) |
| Fact 11.1 | A | "sollte"; 11.5 (independent of manufacturer) deleted |
| Fact 13.2 simplification | A | Added note on further parts / two-letter subclasses |
| Fact 17.7 / 17.6 | A | "Ein Plan ohne Datum ist unbrauchbar" (Lang variant), "erwarten" |
| Fact 18.3 regularly updated | A | "prüfen Sie deren aktuellen Stand" |
| Fact 19 slide item | A | Four plan types incl. Klemmen |
| Lang quiz answers all 0 | A | Answers now [2,1,2,1,0], options and AR/EN reordered in step |
| Lang quiz Q3 AR edges | M | "الرقمان 13 و14 تحديدًا" etc. (ends in Arabic, avoids suggested phrase ending in Latin) |
| Lang quiz Q4 AR digits | M | "من قاعدة بيانات المعيار IEC 60617 الرسمية"; DE/EN got "offiziellen/official" |
| Lang 2.5 Vertrag | M | See Fact 2.5 |
| Lang 5 slide term + 5.2 allpolig | A | متعدد الخطوط / multi-line (all-pole) |
| Lang 5.5 | A | Stromweg gezeichnet |
| Lang 6 term exploded | A | "split representation" |
| Lang 6.4 | A | Steuerstromkreis / Laststromkreis, AR gender fixed |
| Lang 9.2 AR edge + TTS 60617 | M | AR reworded to end in Arabic; TTS "sechzig-sechshundertsiebzehn" |
| Lang 10.1 / 10.4 / 11.2 / 13.3 / 14.4 / 15.2 / 15.3 / 15.4 / 16.3 / 17.2 / 19.2 / 19.3 AR edges | A/M | Reworded so no AR line starts/ends with Latin/digit; extra edge cases (18.4, 13.4) fixed too |
| Lang 13.3 AR "المصهر" | R | TERMS.md (binding) says Sicherung = المنصهر; kept المنصهر |
| Lang quiz Q2 option "مصهر" and 12.3 "المصهرات" | R | Same reason (TERMS.md: المنصهر) |
| Lang quiz Q1/Q5 wording | A | Reworded as suggested |
| Lang glossary articles | A | der/die/das added to all 15 entries |
| Lang glossary Betriebsmittel plural | A | معدات كهربائية / electrical equipment |
| Lang 1.4 | A | New learning-goal sentence with TTS |
| Lang 4.3 AR Hausanschluss | A | التوصيل المنزلي |
| Lang 5 EN circuit diagram -> schematic (3.5, 5.1, 6.1, 7.8, glossary, term) | A | |
| Lang 6.6 Wirkschaltplan in AR | A | Latin term added mid-line |
| Lang 7.6 / 7.7 | A | Monteur / المُركِّب; "zählt" |
| Lang 8 التسليك, 8.2, 8.3 | A | مخطط توصيل الأسلاك; مُجمِّع خزائن التوزيع والتحكم (TERMS Schaltschrank) |
| Lang 9.5 AR grammar | A | |
| Lang 11.6 إصدار | A | |
| Lang 11.7 stamp -> serial number | A | |
| Lang 12.1 الكائنات -> العناصر | A | |
| Lang 12.3 AR | R (partly) | Only the المصهر part rejected; line stays with المنصهرات |
| Lang 13.7 delete | A | Line removed |
| Lang 15.6 Klemmenbezeichnungen | A | EN "terminal designations" |
| Lang 15.7 السكون | A | |
| Lang 17.5 Sie | A | |
| Lang 17.7 | A | See Fact 17.7 |
| Lang 18.2 / 18.5 AR | A | إصدار, ساريًا |
| Lang 19.5 AR | A | |

Not in findings but done: TERMS.md applied throughout (TTS "I-E-Ze" instead of "I-E-Zett"; Schaltplan AR = مخطط الدارات; Schaltschrank/Stromkreis terms; Vorschrift = لائحة in 13.6); old-letter claim in 12.8 softened; 6.x slide item "Aufgelöst ist übersichtlicher" replaced; 1.2 "aller" removed; next pointer reworded to E-F07 Fachsprache; stand updated; ten claims added to research "dropped".

Rejected: Lang 13.3 "المصهر", Lang quiz Q2 "مصهر", Lang 12.3 "المصهرات" (all conflict with binding TERMS.md). Fact 2.5 and Fact 9.2 / Lang 2.5 were taken as modified variants.
