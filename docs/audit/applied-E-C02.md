# Applied audit findings: E-C02 (scripts/E/02-funktionale-sicherheit.json)

Legend: A = applied, M = modified (corrected variant), R = rejected. S = scene, L = line (numbers refer to the original script). F = facts finding, G = language finding.

| Finding | Result | Reason |
|---|---|---|
| F S10.9 wrong referent (EN 954-1) | A | Line moved directly after the EN ISO 13849-1 line, subject named; DE/AR/EN/tts equivalent |
| F S9.8 "SIL nie für ein Gerät allein" | A | Replaced by "bezieht sich auf die ganze Sicherheitsfunktion"; absolute claim moved to dropped |
| F S11.8 level vs hazard | A | "Erforderlicher Level folgt aus der Risikoabschätzung, erreichter Level beschreibt die Güte" |
| F S13.4 Machinery Directive only | M | "ab 2027" not in research facts, so not stated; hedged: "nach älteren Quellen", new Maschinenverordnung "kann das ändern", check current status |
| F S18.9 "tabu" absolute | A | "ändern Sie nur mit Freigabe"; AR uses وصلات التجاوز (G S18.9) |
| F S18.7 unclear sentence | A | Deleted (G rewrite "häufige Fehlerquelle" would add an unsupported claim) |
| F S18.2 motive "schneller arbeiten" | A | "Bediener umgehen Schutztüren manchmal." |
| F S6.1 "wichtigste Grundnorm" | M | "Die Grundnorm heißt IEC 61508."; AR rewritten so it does not end with Latin |
| F S6.8 empty sentence | A | Deleted |
| F S4.9 "in vielen Fabriken" | A | "Dieses vereinfachte Beispiel zeigt nur das Prinzip." |
| F S5 slide "sicherer Stopp" | A | Item "Im Fehlerfall: sicherer Zustand" |
| F S12.4 AR "وحده" | M | Exclusivity removed; AR rephrased to end in Arabic (finding text ends with a digit) |
| F S17.10 channel fault noticed | M | "Zwei Kanäle ermöglichen es, Fehler zu erkennen"; moved directly after the two-channel line (17.6); AR gender problem gone |
| F S20.5 "immer" | A | "Am Anfang steht die Risikobeurteilung." |
| F S19.8 AR Leitung | A | "إدارته وإشرافه" |
| F S17.3 AR Not-Halt term | A | إيقاف الطوارئ (also glossary, per TERMS.md) |
| G title AR ends with PL | A | Title AR reworded |
| G glossary AR Latin edges | A | SIL / PL / PLr entries without Latin parentheses |
| G quiz Q2 AR options | A | Arabic edge fixed (المعيار ... الأوروبي / الدولي) |
| G quiz Q3 | A | Question and options rewritten, distractor "Zykluszeit"; answer stays 2 |
| G quiz Q1 | A | Options balanced; answer 0 |
| G quiz Q5 | A | Option 2 shortened ("Ich ändere nichts ohne Freigabe"); answer 2 |
| G S6.6 spelled year in de/en | A | de/en "2010", tts unchanged |
| G S4.6 / S5.8 AR Sensor/Aktor | M | Suggested "حسّاس" replaced by the binding TERMS.md term المستشعر; المُنفِّذ as suggested |
| G S17.3 / glossary Not-Halt | A | See F S17.3 |
| G S9.4 AR أربعة | A | Applied |
| G S15.3 AR passive | A | يُحاوَل |
| G S17.10 AR gender | A | Moot after rewrite (see F S17.10) |
| G S1.7, S17.4, S20.6, S17 term, glossary SPS | M | Suggested "وحدة التحكم المبرمجة" conflicts with TERMS.md (E-C supplement); used المتحكم المنطقي القابل للبرمجة (للأمان) |
| G S19.8 | A | See F S19.8 |
| G S10.9 move | A | See F S10.9 |
| G S11.5 tts letters | A | "A, Be, Ze, De und E" |
| G S11.6 / S16.4 tts Pe-El-r | A | "Pe-El-Er" |
| G S5.9 article | A | "ein ausfallsicheres Prinzip" |
| G S14.2 / S13.5 AR مواصفة | A | معيار / اشتراط ملزم |
| G S15.9 third step order | A | New line after 15.6; documentation as separate last line |
| G S18.7 rewrite | R | Replacement claim "häufige Fehlerquelle" not in research; line deleted instead |
| G S18.9 AR | A | Merged with F S18.9 |
| G S7 table row >50 | A | "Lebenszyklus \| Konzept bis Außerbetriebnahme" |
| G S19 table row 5 | M | "5 \| Unter Spannung stehende Nachbarteile abdecken" (47 chars); keeps "unter Spannung"; spoken rule 5 (19.6) unchanged, so the five rules are not shortened |
| G S13 slide item | A | "Beide laut Quellen harmonisiert" |
| G S3 terms without articles | A | Articles added to all slide terms (S3-S6, S9, S11, S14, S15, S17); S4 term AR aligned with glossary |
| G S3.8/3.9 repetition | A | Both deleted (3.9 would lose its antecedent) |
| G NEXT format | A | "Im nächsten Video geht es um Maschinensicherheit." / AR / EN (E-C03) |
| G Intro S1.2-1.3 merge | A | Merged |
| F S6 fixed hedging items kept | - | Ausgabe-year remains hedged "nach unseren Quellen" |

No finding was rejected outright except the G S18.7 rewrite (replaced by deletion).

Research file docs/research/E-C02.json: seven claims moved to "dropped", note on the harmonisation fact updated. `stand` in the script extended.

Concerns for a primary-source check: harmonisation status and presumption of conformity of EN ISO 13849-1 / EN 62061 (source from 2012, Machinery Regulation transition); year of the second edition of IEC 61508 (2010); current editions of the named standards; E-C01 `next` (outside this video) still uses "السلامة الوظيفية", which conflicts with TERMS.md.
