# Applied audit findings: S-06 (scripts/E/06-autocad-electrical.json)

Legend: A = applied, M = modified (corrected variant), R = rejected. S = scene, L = line (numbers refer to the audited version). F = facts finding, G = language finding.
Extra instruction applied: S-06 no longer re-teaches the Eplan lesson ("Elektro-CAD: Schaltpläne am Beispiel Eplan"). Scenes 2, 5, 8, 9, 11, 16, 17 are shortened to pointers by title; unsourced comparative claims removed. Script is now ~1658 spoken words (validate.py), 21 scenes.

| Finding | Result | Reason |
|---|---|---|
| F S16 duplicates S-01 (QET, scenes 2/8/9/11) | A | S2, S8, S9, S11, S16, S17 reduced to short recaps and pointers by title. S16/S17 now QElectroTech pointer plus LibreCAD only |
| F S15.3 pure control projects favour standalone system | A | Replaced by "depends on task, customer, team; no general ranking"; slide items and old lines 15.2/15.4 removed |
| F S14.7 central project database | A | "Systems built for electrical planning from the start"; slide rows without database claim |
| F S5.2 block/attributes for every tool | M | Limited to CAD-based solutions, "other systems store the same data differently"; slide item adjusted |
| F S11.6 "gilt für jedes Werkzeug" | M | Deleted; replaced by "can be kept as an attribute on the block" |
| F S8.10 lists change automatically | A | "regenerate and check the lists" |
| F S1.6/1.7 incoherent line and spoken IDs | M | 1.6 deleted; new line names the Eplan video by title, no IDs, no tts "Es null ..." |
| F S10.5 DIN EN 60617 naming | A | Hedge: "usually called ... check status in standards catalogue" |
| F S12.5 LoC dated | A | "US-Kongressbibliothek (Stand etwa 2020)"; AR/EN equivalent |
| F S13.5 free converters / AR محوّلات | A | AR "أدوات تحويل", licence hint directly after (13.6) |
| F S0 TTS Käd vs Ze-A-De, AR E-CAD | M | AR "برنامج الرسم الكهربائي" applied. TTS "Käd" REJECTED: TERMS.md (binding) fixes CAD as "Ze-A-De" in all scripts; Auto-/Libre-Ze-A-De kept consistent |
| F S16.6 "guter Weg" | A | "eine Möglichkeit, Grundlagen kostenlos zu üben"; slide item "Konzepte kostenlos üben" |
| F S2.7 motor start with Schutzschalter | A | "Sicherung, Schütz und Motor" in S2, S7, (AR منصهر/كونتاكتور) |
| G S0.5 quiz 5 Latin edges | M | AR question "ما الذي ينطبق على برنامج LibreCAD الحر وأمثاله؟" (name inside, Arabic edges), option 1 AR starts Arabic |
| G S11.8 AR "من هذه السلسلة" for E-F06 | M | Pointer by title "Schaltpläne, Symbole und Kennzeichnung" (no ID), AR "ضمن مسار الأساسيات" |
| G S12.4 EN "own format of Autodesk" | A | "Autodesk's own format" |
| G S1.7 spoken IDs | M | See F S1.6; the audit's replacement ("eigenständiges Elektro-CAD ... allgemeines CAD") not used, to avoid classifying S-01 |
| G S14.1 spoken ID S-01 | M | Title of Eplan video, no ID, no tts |
| G S8.3 duplicates S-01 | A | Scene 8 compressed to 4 pointer lines |
| G S0 TTS Käd | R | See F S0: TERMS.md binding |
| G S14.14 name AutoCAD Electrical | A | 14.4 "bekannt als AutoCAD Electrical"; AR ends in Arabic; tts Auto-Ze-A-De Elektrikal |
| G S0 EN UK spelling | A | colour, catalogue, practise, licence, summarise, standardised |
| G S1.2 / S2.3 etc. AR "E-CAD" | A | "برنامج الرسم الكهربائي" everywhere (lines, quiz) |
| G S3.2 layer "Ebene" in AR/EN | A | AR "ويسمى بالألمانية Ebene، أي الطبقة"; EN "in German 'Ebene'" |
| G S4.9 repeats 4.7 | A | Deleted (kept as short "Die Daten sind trotzdem da.") |
| G S6.2 Artikel/صنف, EN "himself" | A | "صنفًا", "item", "themselves" |
| G S7.2 / 7.4 / 5.4 AR Leitung vs Linie | A | الموصل / ترقيم الموصلات / ينتهي عندها الموصل |
| G S7.0 term Querverweis not used | A | Term replaced by Anschlusspunkt |
| G S8.3 AR / EN "Evaluations" | A | "reports"; AR reworded in pointer line |
| G S9.0 row word order | A | "Das Programm kennt Ihre Vorgaben nicht" |
| G S9.8 non sequitur | A | "Ein Werkzeug allein sichert keine Qualität, entscheidend ist die Arbeitsweise" |
| G S10.3 digits in de vs words | A | de digits "2 bis 13", "1900"; tts words |
| G S10.7 AR grammar | A | اسألوا عن الإصدار الذي يطلبه عميلكم |
| G S11.3 / 11.2 AR | A | الترميز المرجعي; "في معيار DIN EN 61082-1 الألماني" |
| G S12.2 AR padded | A | "لذلك توجد صيغتان معروفتان هما DXF وDWG للرسومات" |
| G S12.0 row ambiguous | A | "Autodesk veröffentlicht keine Spezifikation" (49 chars) |
| G S12.5 tts Library of Congress | A | DE "US-Kongressbibliothek", tts "U-Es-Kongressbibliothek" |
| G S13.3 clumsy | A | "Nur wenn die Attribute erhalten bleiben, behält das Symbol seine Daten" |
| G S13.8 order | A | Licence line moved directly after the converter line |
| G S14.0 row 51 chars | A | Row replaced ("Ausgangspunkt und Arbeitsweise") |
| G S16.8 order / S17 pointer | A | Order fixed; QET reduced to pointer |
| G S17.8 AR awkward | A | أما مطابقة الرموز لمعياركم فتتحققون منها بأنفسكم |
| G S18.7 / S15.5 EN gendered | A | Neutral wording ("is expected", "the customer specifies") |
| G S20.0 quote layout | A | Layout changed to bullets, items "Aktuelle Ausgaben selbst prüfen", "Allgemeine Information, keine Beratung", "Produkte nur als Beispiele" |
| G S21.3 AR "نظرة الدورة العامة" and next | A | "صفحة الدورة الرئيسية" in line, `next`, slide item; DE/EN "Kursseite"/"course page" |
| G S0 quiz 1 and 4 | A | Q1 options reworked (one correct), Q4 "laut diesem Video"; answers 1,0,2,1,2 |
| G S0 glossary رخصة / Betriebsmittel | A | ترخيص; "das Betriebsmittel" = معدّة كهربائية (also term slide S5) |
| F S0 / G S0 other | A | Slide limits respected, all validate.py checks pass (0 issues) |

Additional edits: S3 deepened with ByLayer (research fact 0), S4 attribute modes (fact 2), S10 symbol export formats and edition differences (fact 14), S12 group code, text/binary DXF and reverse-engineered DWG spec by the Open Design Alliance (facts 3-5), S13 ODA converter batch/audit (fact 6), S14 toolset features, project file, designation format parameters and catalogue database (facts 21-23), S17 LibreCAD (facts 7-9). Removed unsourced "saves time at purchasing/production" (S6.8).
Research file: six claims added to "dropped" (comparative ranking, "every tool" generalisation, database claim for other systems, purchasing/automatic-update claims, "good way to practise", QET details moved to pointer). `stand` updated with the softened items.

Rejected: only the TTS "Käd" suggestions (two entries, same reason: TERMS.md binding "Ze-A-De").
