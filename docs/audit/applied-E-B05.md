# Applied audit findings: E-B05 (scripts/E/05-brandschutz-notbeleuchtung.json)

Legend: A = applied, M = modified (corrected variant), R = rejected. S = scene, L = line (1-based, original numbering). F = facts finding, G = language finding.

| Finding | Result | Reason |
|---|---|---|
| F S14.5 DIN 14675 has two parts | A | Line now "Der Teil zwei der DIN 14675", slide row "DIN 14675-2", quiz Q4 "Teil 2" (DE/AR/EN) |
| F S5.1 Rettungswege too narrow | A | "Zu den Rettungswegen gehören notwendige Flure und Treppenräume" |
| F S11.2 Notbeleuchtung vs Sicherheitsbeleuchtung | A | Sicherheitsbeleuchtung is part of Notbeleuchtung; elsewhere AR uses إضاءة الطوارئ (TERMS), only S11.2, S11 term and glossary keep إضاءة الأمان to show the distinction |
| F S15 slide rows (concrete behaviour) | A | Rows now "wird angesteuert", "Art \| laut Brandschutzkonzept", 6 rows; behaviours moved to dropped |
| F S16.5 inspection by recognised experts absolute | A | "je nach Land"; slide item "Je nach Land: Prüfsachverständige" |
| F S17.7 only Elektrofachkräfte | A | "Elektrofachkraft oder unter deren Leitung und Aufsicht" (TERMS), AR/EN equal |
| F S17 Z6 safety power source keeps feeding | M | Unsupported; replaced by general "Beachten Sie auch die Sicherheitsstromversorgung der Anlage" (new line 7); claim to dropped |
| F S12.8 "Norm allein macht keine Pflicht" | A | Replaced by "hängt zum Beispiel vom Baurecht und vom Vertrag ab" |
| F S14.7 Kompetenznachweis | A | "Die Anforderungen an die Fachfirma regelt der Teil zwei der Norm" |
| F S13 detectors incomplete | A | "zum Beispiel Rauch oder Wärme" in L2 and slide item |
| F S10.2 power supply absolute | A | "Sie soll auch bei Netzausfall weiter versorgen" |
| F S5.3 slide "Leitungen erhöhen die Brandlast" | A | "können ... erhöhen" |
| F S8.2 Funktionserhalt without duration | A | "für die geforderte Dauer"; slide item 1 and quiz Q1 option adjusted too |
| F S18 slide "Abnahme und Prüfung" | A | "Prüfsachverständige: Prüfung" |
| G S4 terms with Latin parentheses | A | All trailing Latin parentheticals removed from slide terms (all scenes) |
| G Quiz Q4 AR ends with DIN 14675 | M | Suggested fix still ended Latin; AR now "ما الذي ينظمه الجزء الثاني من معيار DIN 14675 بالتحديد؟" |
| G S4.7 ووصوفاتكم | A | Applied as suggested |
| G S5.5 AR syntax | A | Applied as suggested |
| G S12.2-12.4 TTS numbers | A | Digit-wise tts, "Strich" |
| G S14.2 TTS 0833 | A | Spelled out |
| G S17.3 line too long | M | Split into two lines (new 17.3 and 17.4), each ≤20 words; the order wording is unchanged |
| G general النسخة | A | All "نسخة/النسخة" became "صيغة/الصيغة" (Fassung); الإصدار kept for Ausgabe |
| G quiz Q3 / Q2 | A | Q3 question and options as suggested; Q2 "Nie" removed. Answers now 2,0,3,1,2 (one correct each); Q1 options reordered |
| G S2.4 AR | A | "تشريعات البناء من اختصاص الولايات." |
| G S2.9 order | A | Moved behind 2.6 |
| G S5.11 abplanen | A | "Stimmen Sie ... ab" |
| G S6.1 Richtlinie term | A | "التوجيه" used (6.1, 6.6, 7.1, 3.4, 20.2) |
| G S8.6 TTS DIN 4102-12 | A | Digit-wise |
| G S9.6 AR | A | Applied; wording adapted to TERMS (استمرار الوظيفة) |
| G S9.8 المركِّب | A | Applied |
| G S10.4 TTS and AR | A | Applied |
| G S13.5, 13.10, 18.4, term Aufschaltung | A | فرقة الإطفاء |
| G S14.3 TTS | A | Applied |
| G S14.5 TTS | A | Digit-wise, with "Der Teil zwei der" |
| G S15.3 AR | A | شفط الدخان والحرارة |
| G S16.1 الأمنية | M | Also softened DE/EN to "often" (state law decides, see 16.2) |
| G S16.2 AR | A | Applied |
| G S17.2 internal code | A | DE/AR/EN refer to "Video über elektrische Sicherheit"; tts removed (equals de) |
| G S19.6 closing line | A | Reworded and moved to the end |
| G S1.7 EN functional endurance | A | Kept "functional endurance" (B06 12.4/12.5 needs adjusting there) |
| G S8.6 / 5.7 Fluchtweg | A | 5.7 DE/AR now Rettungsweg/مسار إخلاء; 12.6 "Flucht- und Rettungswege" kept (ASR wording, F11) |
| G S14.4 year | M | Digits in de/en, AR "في عام ٢٠٢٢" moved inside the sentence (no digit at edge); tts spelled out |
| G S17.0 title / Q5 | A | Heading "Die fünf Sicherheitsregeln", Q5 option without code |
| G S10.4/ S12 etc. AR مصطلحات | A | TERMS applied: إضاءة الطوارئ, استمرار الوظيفة, الكهربائي المؤهَّل, كل الأقطاب, glossary updated |
| G S1.1 G "functional endurance" B06 | R (partly) | B06 not changed here (other video) |

Rejected: none outright. Next pointer already E-B06 (HOAI) with a normal Arabic sentence; unchanged. Research file: 8 entries added to "dropped"; `stand` extended.

Concerns for primary-source check: DIN 14675 Teil 2 scope (F14), year 2022 of VDE 0833-2 (F13), exact AR/DE wording of rule 5 ("benachbarte, unter Spannung stehende Teile"), TERMS conflict: TERMS maps Notbeleuchtung and Sicherheitsbeleuchtung both to إضاءة الطوارئ, but the hierarchy requires two terms, so إضاءة الأمان is used for Sicherheitsbeleuchtung where the distinction matters.
