# Applied audit findings: E-C03 (scripts/E/03-maschinensicherheit.json)

Legend: A = applied, M = modified (corrected variant), R = rejected. S = scene, L = line (1-based, original numbering). F = facts finding, G = language finding.

| Finding | Result | Reason |
|---|---|---|
| F S5.2 AR "تقريبًا" on exact date | A | Removed; also names DGUV as accident insurance body (G S5.2) |
| F S11.7 illuminated Not-Halt | A | Line deleted (dropped list) |
| F S14.7 presses / fixed guards | A | Line deleted (no fact) |
| F S16.10 authority says no rigid criteria | A | Line deleted |
| F S16.3 "Sie gelten als Hersteller" | A | Company is the manufacturer; DE/AR/EN and slide row changed |
| F S17.0 "Gesamtanlage" slide item | M | Replaced by "Einbauerklärung: Teil der technischen Unterlagen" (fact F23) instead of a duplicate "neue Regeln prüfen" |
| F S12.4 Category 0 via safe drive switch-off | A | Line deleted |
| F S5.6 earlier placed machines | A | Replaced by "check the current official text" (DE/AR/EN) |
| F S4.1 Stand note | A | "Stand Oktober 2026" added, tts spelled |
| F S4.3 ProdSG only | A | "und eine zugehörige Verordnung" (F4: 9. ProdSV, not named) |
| F S13.2 EN "Fixed" guards | A | Fixed in EN, AR aligned |
| F S13.0 "Scanner" | M | Item "Berührungslos: Lichtvorhang u. a."; scanner moved to dropped |
| F S11.1 superlative | A | "ein bekanntes Bedienelement" in DE/AR/EN |
| F S15.3 AR rule wording | A | Combined with G S15.3, see below |
| F S15.1 "Fehlersuche" | A | Now "Wartung" only |
| F S10.1 Not-Halt AR term vs E-C02 | R | TERMS.md is binding: إيقاف الطوارئ (Not-Halt), فصل الطوارئ (Not-Aus). Not-Aus AR changed from "فصل الطاقة في الطوارئ" to TERMS form (S10 terms, lines, glossary) |
| G S0 title AR ends with digits | M | Reworded to end in Arabic ("للتجهيزات الكهربائية"); "الكهرباء والميكانيك" instead of "الربط مع الميكانيك" |
| G S0 next | A | Normal Arabic sentence, no code; chain target E-D01 is not named in text. E-C04 title not touched (other video) |
| G S0 glossary CE | A | "علامة CE الأوروبية" |
| G S0 quiz Q2/Q4 AR | A | Both end in Arabic |
| G S4.4 grammar | A | DE/AR/EN: directive replaced by regulation |
| G S6.4 CE on machine | A | AR fixed, DE/EN say "at the machine", tts updated |
| G S15.3 TERMS / split | M | Split in two lines; titled "first three of the five rules" and "rules four and five" so the full order is kept; AR "تأمينها ضد إعادة التشغيل", "كل الأقطاب", "إحاطتها بحواجز" |
| G S13.2 EN | A | See F S13.2 |
| G Q3 quiz | M | Applied; option 1 without Arabic in the DE field; answer 1 (answers now 0,2,1,2,0) |
| G S15.7 AR/EN | M | "إدارته وإشرافه"; EN "qualified electrician (Elektrofachkraft)" |
| G S13.1, 3.1, 14.7, 20.7 "أجهزة الحماية" | R | TERMS.md: Schutzeinrichtung = وسيلة حماية; AR kept as "وسائل الحماية" and made consistent (3.1, 13.2, 13.5 changed from أجهزة/الحماية). 14.7 deleted |
| G S3.2 duplicated التحكم | A | "خزانة التوزيع والتحكم ونظام التحكم" |
| G S3.6, 6.2, 6.3, 6.4 EN "He" | A | "It" |
| G S17.2 EN | A | "Partly completed machinery" |
| G S20.6 EN | A | "for their current status" |
| G S10.7 BG RCI | M | Spelled out in DE/AR/EN/tts; EN expansion is a translation of the name, not a new claim; AR ends in Arabic |
| G S16.0 row 51 chars | A | "Folge \| Herstellerpflichten, neue Beurteilung" |
| G S1 title slide 2 items | A | Third item added |
| G S1.4 repeated "Heute" | A | Reworded in DE/AR/EN |
| G S19.0 terms | A | "Normen" replaced by Konformitätsvermutung |
| G S19.3 style | A | Simpler wording DE/AR/EN |
| G S0 glossary additions | A | Hersteller, Betreiber, Gefährdungsbeurteilung, Konformitätsvermutung added |
| G S7.2, 10.7, 10.8, 14.8, 13.8, 13.9, 11.2 AR filler | M | "المعروف" replaced by purposeful phrases ("الخاص بتقييم المخاطر", "الخاص بتصميمه", "المخصص لذلك" etc.) |
| G S8.6/8.7 "also" | A | Filler removed in DE/AR/EN |
| G S3.0 Hersteller / Ausrüstung terms | R | Existing المصنِّع and التجهيزات الكهربائية kept; no TERMS.md entry requires a change (other videos to align) |

Also: stand extended in the script; seven claims moved to "dropped" in docs/research/E-C03.json. Validator: 0 issues; custom check for Arabic Latin edges, slide limits, tts presence: clean.

Needs primary-source check: Stichtag 20.01.2027 and absence of a transition phase (DGUV, medium confidence); expansion of BG RCI; edition status of EN 60204-1, EN ISO 13850, EN ISO 12100.
