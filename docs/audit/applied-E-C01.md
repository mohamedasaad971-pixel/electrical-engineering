# Applied audit findings: E-C01 (scripts/E/01-sps-grundlagen.json)

Legend: A = applied, M = modified (corrected variant), R = rejected. S = scene, L = line (1-based, numbers refer to the original script). F = facts finding, G = language finding.

| Finding | Result | Reason |
|---|---|---|
| F S11.5 "Dieses heißt PAA" | A | Now "Prozessabbild der Ausgänge heißt kurz PAA" (DE/AR/EN/tts); G duplicate same |
| F S7.0 "der Schütz" | A | "das Schütz" |
| F S17.7 planning recommendation | A | Replaced by edition/project-requirements statement (DE/AR/EN/tts); slide item likewise |
| F S21.5 "Die Norm nennt fünf" | M | "Ausgabe 2013 ... nennt fünf Sprachen" (DE/AR/EN/tts); AR keeps "كما رأينا" so it does not end in Latin |
| F S14.6 "ausdrücklich" | A | "Sinngemäß ..." DE/AR/EN; wording claim moved to dropped |
| F S7.7 bus system claim | A | Line deleted (G variant "CPU reaches module via bus" not adopted: delete is safer) |
| F S16.9 unfulfilled promise | A | Line deleted; G variant (new transition line) rejected as redundant with S17.1 |
| F S15.0 "Neue Ausgabe seit 2025" | M | "Neue Ausgabe laut Katalogen (2025)" (G variant, within 50 chars) |
| F S6.0 / S6.6 operating system | A | Slide item replaced by "CPU entscheidet, bewegt aber selbst nichts" (from line 6.7); line deleted |
| F S5.6 "nie die Maschine" | A | Softened DE/AR/EN/tts; AR "وحدة SPS" (no "فـ" before Latin) |
| F S13.9 conveyor example | A | Marked as made up and simplified; safety functions not shown |
| F S18.0 Mechatroniker "Einstieg" | A | "in Stellenanzeigen genannt" |
| F S20.3/20.0 rule 5 | M | "benachbarte, unter Spannung stehende Teile" in L6 (DE/AR/EN); slide item shortened to 50 chars; AR "إدارته وإشرافه" kept (path-wide form). Wording not in research file: check against DIN VDE 0105-100 |
| G S0 title AR ends with digits | M | Title ends with "للغات البرمجة"; SPS term per TERMS.md (المتحكم المنطقي القابل للبرمجة) instead of suggested "وحدة التحكم المبرمجة" |
| G S0 quiz Q3 | A | Question and option 4 nominative; answer stays 1 |
| G S0 glossary AR Latin edges | A | Latin tags dropped from AR glossary (kept in de) |
| G S0 next + S21.7 "السلامة الوظيفية" | A | "الأمان الوظيفي" (TERMS.md E-C) |
| G S1.4, S2.2, S15.2, S15.3, S21.5 TTS | A | Norm numbers read digit by digit (Din E-En / I-E-Ze sechs eins eins drei eins) |
| G Sensor "مستشعر" -> "حسّاس" (S1.5, 2.9, 5.2, 5.8, 8.0/8.1/8.3/8.7/8.8, 9.4, 13.3, 19.2, 21.4, glossary) | R | TERMS.md (binding) fixes: Sensor = المستشعر. Path-wide inconsistency with other E-C videos should be resolved in TERMS.md, not here |
| G S12.10 off-topic line | A | Deleted (not re-inserted) |
| G S12.5 dangling thought | M | Line deleted instead of completing it (completion would add a derived claim not in the research file) |
| G S4.2 Zentralbaugruppe | A | "Zentraleinheit" DE/EN (AR already "وحدة مركزية") |
| G S4.7 الدخل/الخرج | A | "المداخل ثم وحدة CPU ثم المخارج" |
| G S4.1 AR filler | M | "والآن إلى بنية المتحكم المنطقي القابل للبرمجة." (TERMS.md term) |
| G S5.6 "فـ" | A | Reworded (see F S5.6) |
| G S7.7 vague bus | M | Line deleted (see F) |
| G S10.5 AR | A | "تُخرج القيم المحسوبة إلى المخارج" |
| G S9.6 AR | A | "يشغّله كونتاكتور" |
| G S2.5 AR Steuerung | A | German word kept in AR line |
| G S2.8 AR + S2.8 EN | A | AR and EN as suggested |
| G S15.0 item | A | See F S15.0 |
| G S15.5 AR الفهارس | A | "كتالوجات المعايير" |
| G S17.4 Primärbeleg | A | "Primärquelle", AR/EN kept |
| G S17.1, S17.8 AR | A | Fillers removed |
| G S18.0 table rows > 50 | A | Two rows shortened |
| G S18.3 AR | A | "التدريب المهني ... ونصفًا" |
| G S18.5 AR | A | "كفني ميكاترونيكس" |
| G S0 quiz Q4 | A | Reworded DE/AR/EN; answer stays 3 |
| G S0 quiz Q5 | A | Question "Wer darf ...", plausible distractors, answer stays 2 |
| G S2.0, S3.0, S4.0, S16.0, S17.0, S20.0 term AR Latin tags | A | Dropped; S2 term uses TERMS.md term |
| G S15.6 EN | A | "always check again" |
| G S2.8 EN note | A | See above |
| G S1.2 (own check) | M | SPS in AR lines uses TERMS.md term; Latin SPS only in the middle |

Own checks: no quote slides; quiz answers 2,0,1,3,2 (one correct each); `next` chain E-C01 -> E-C02 (functional safety) kept; tts equals de in content/order; validate.py 0 issues. Research file: 6 claims added to "dropped".

Need primary-source check: IEC 61131-3 edition 4 (2025) dropping AWL and DIN adoption status; rule 5 wording "unter Spannung stehende Teile" (DIN VDE 0105-100); DIN EN 61131-1 definition (only in essence).
