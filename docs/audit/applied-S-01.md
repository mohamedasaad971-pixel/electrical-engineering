# Applied audit findings S-01 (scripts/E/01-eplan.json)

Source: docs/audit/facts-S-01-06.json (16) and docs/audit/language-S-01-06.json (22), filtered to S-01. Result: 24 applied, 12 modified, 2 rejected. validate.py: 0 issues.

## Facts / legal
| Finding | Result | Reason |
|---|---|---|
| 1.3 leaked note in AR | modified | Removed note; used language variant "هنا ... بالاسم فقط"; EPLAN spelling + tts "E-Plan" |
| 10.1 "den Schütz" | applied | "das Schütz" |
| 0 next garbled | modified | Clean AR sentence naming real S-02 title; no Latin edges |
| 2.7 "Hauptgrund" | applied | "wichtiger Grund" in DE/AR/EN |
| 5.2 "Viele Programme" | modified | "Manche Programme ... wie in der Hilfe eines Herstellers beschrieben"; AR "الجوانب"; tts matches |
| 12.7 "immer aktuell" | applied | After regenerating, lists match the data |
| 12.0 unsourced report table | modified | Table: Stückliste, Klemmenplan, "Weitere | je nach Programm"; lines 12.5/12.6 deleted; 15.3 reworded to "Auswertungen"; glossary Kabelliste removed |
| 18.1 "teures" | applied | "kostenpflichtig" / commercial |
| 18.6 unsupported comparison | applied | Scope differs by program; check yourself |
| 18.3 QET 0.7 manual | modified | "Laut einem älteren Handbuch ... Stückliste (Nomenklatur) ... Umfang prüfen" |
| 4.9 Fachmedium | applied | Line deleted (low-confidence source), moved to "dropped" |
| 7.6 title-block output | applied | "Manche Programme ... prüfen Sie das" |
| 1.6 "fast jedem Programm gleich" | applied | "vielen Programmen ähnlich" |
| 9.6 absolute opinion | applied | "sehr wichtig" |
| 17.4 safety text | rejected | Suggested fix "none"; text already correct and complete, five rules untouched |
| 14.3 Verdrahter AR | applied | Neutral wording |

## Language
| Finding | Result | Reason |
|---|---|---|
| 1.3 meta text AR | modified | See above (same fix) |
| 10.1 gender | applied | Same as fact finding |
| next AR | modified | See above |
| EPLAN spelling / tts | applied | EPLAN in title, lines, slides, stand; tts "E-Plan" in 1.3 and 3.2 |
| 5.2 AR "زوايا النظر" | modified | Merged with fact softening |
| 7.4 AR fragment | modified | AR fixed; also internal ID "E-F06" removed from DE/AR/EN/tts (TERMS S rule), now "Video über Schaltpläne, Symbole und Kennzeichnung" |
| 4.9 weak logic | applied | Deleted |
| 6.1 AR | applied | Suggested wording |
| 6.7 DE "es" | applied | "sie"; EN plural adjusted |
| 15.3 EN | modified | Reworded with the report softening (missing from the reports) in DE/AR/EN |
| 15.5 AR الترميز | applied | Consistent term |
| 16.4 Klemmenliste | applied | Klemmenplan / مخطط الأطراف / terminal diagram |
| 18.4 AR "و KiCad" | applied | "وبرنامج KiCad" |
| 18.8 AR | modified | Softened DE/AR/EN to "können ausreichen" (no "völlig") |
| 19.3 AR | applied | Suggested wording |
| 14.7 AR | applied | "التشغيل الأولي" |
| 1.1 series name | applied | "سلسلة البرمجيات" |
| 1.2 AR | applied | "للوحات التوزيع" |
| 12.6 EN wording | rejected | Moot: line 12.6 deleted (see fact finding 12.0) |
| Glossary معدات | applied | "معدّة كهربائية" (glossary and slide terms of scene 5) |
| Quiz distractors | modified | Q1, Q2, Q3, Q5 options replaced (no price/throw-away wording); answers now 0,1,2,1,0, one correct each; Q3 correct option no longer clearly longest |
| Title AR | applied | "المخططات الكهربائية بالحاسوب: برنامج EPLAN مثالًا" |

## Own checks
`next` points to the real S-02 title; quote slide in scene 21 changed to bullets (3 items); table rows <=50 chars; no internal IDs in spoken text (the "S-01" kicker on slide 1 is unchanged); research file: 9 entries added to "dropped"; `stand` extended with the softened claims.
