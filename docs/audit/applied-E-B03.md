# Applied audit findings: E-B03 (scripts/E/03-leitungsberechnung.json)

Legend: A = applied, M = modified (corrected variant), R = rejected. S = scene, L = line. "F" = facts finding, "G" = language finding. Research file: docs/research/E-B03.json (5 softened claims added to "dropped").

| Finding | Result | Reason |
|---|---|---|
| F S9.7 "alle drei Bedingungen", absolute "geschützt" | A | Replaced by order + timely tripping under overload; S9.8 (now redundant) replaced by "Kurzschlussschutz prüfen wir getrennt" |
| F S19.8 safety rules for planners | A | Suggested wording applied (DE/AR/EN) |
| F S18.8 responsibility statement | M | Suggested wording applied; slide item 4 now "Zuständigkeiten: im Vertrag klären"; term Elektrofachkraft removed from S18 since no longer mentioned |
| F S7.6 / S20.3 / S7 slide "kleiner als Tabellenwert" | A | Qualified to grouping/warm environment; slide items S7, S20 adjusted |
| F S10.11 / G S10.11 "noch mehr tragen" | A | "mindestens den Nennstrom" (DE/AR/EN) |
| F S14.5 / G S14.5 "Energie des Schutzgeräts" | M | Used "Durchlasswert I²t" (matches research fact), not "Durchlassenergie"; tts I-Quadrat-Te, Ka, Es; AR spelled "k تربيع" to avoid Latin edge |
| F S3.1 Gesamtziel Wärme | A | "Ein Hauptziel ...; dazu kommt der Spannungsfall" |
| G S3.6 order | A | L6/L7 swapped |
| F S8.4 DIN VDE 0298-4 edition | A | "gültige Ausgabe müssen Sie prüfen" added (DE/AR/EN/tts) |
| F S11.6 / G S11.6 factor two before formula | M | Line moved to S12 directly after the formula (new 12.5), original wording kept |
| F S17.11 / S15.9 larger cross-section | A | Rephrased to adjust cross-section, protective device, installation/length and recalculate |
| F S6.6 insulated walls risk | A | "kann besonders stark sinken"; S6 slide item 3 adjusted |
| G Q1 AR options Latin edges | A | AR options in words; answer order shuffled |
| G S4.4, 9.2-9.5, 10.8 "I-Z" in de | A | de/en written Ib/In/Iz, tts I-Be/I-En/I-Zett |
| G S16.7 AR genus | A | Suggested wording |
| G S16.9 Unterlage | A | "zu den Unterlagen" |
| G S20.2 AR التحمل | A | السعة التيارية; DE/EN also "Strombelastbarkeit/current-carrying capacity" |
| G AR الكبل -> الكابل | A | Applied throughout (title, glossary, terms, lines, quiz, TERMS.md Kabel = كابل) |
| G أرقام مختلقة -> افتراضية | A | S1.6, 2.4, 10.1, 16.1, 20.5 (EN "hypothetical") |
| G glossary/term "correction factor" | A | Glossary, S7 term, S7.5 EN; DE term "Umrechnungsfaktor" kept (research wording) |
| G quiz distractors Q2/Q3/Q5 | A | Q2, Q3 option 2, Q5 single question; answers now 1,0,2,1,2 |
| G S2.6 "Echte Auslegung machen Sie" | A | Suggested wording |
| G S8.1 تلعب دورًا | A | Suggested wording |
| G S8.2/8.4/8.5/15.7 tts part numbers | A | "null eins null null Strich ..." style as in E-B01 |
| G S8.3/8.6/10.3-10.8/12.2-12.8/16.2-16.7 digits in de | A | de carries digits, tts spelled |
| G S10.10 "Sie merken" | A | "Merken Sie sich" (AR/EN adjusted) |
| G S12.5 unit for 56 | A | "56 Meter pro Ohm und Quadratmillimeter" (matches research γ unit) |
| G S13.7 AR يزعج | A | Suggested wording |
| G S14.5 tts k and S | A | Included in the tts above; also S14.6 and S14.10 tts Ka/Es |
| G S16.2 AR بالنسبة للأرض | A | "بالنسبة إلى الأرض" |
| G S16.10 AR الصانع | A | "الشركة المصنِّعة" |
| G S19.3 E-F05 cross reference | A | Content reference, tts removed (equal to de) |
| G S19.6 EN verb | A | "cover or fence off" |
| G S19.10 pleonasm | M | "Elektrofachkraft oder unter deren Leitung und Aufsicht" per TERMS.md work rule (not the bare suggestion) |
| G S20.6 AR النسخة | A | الصيغة |
| G S7 term/S7.2 AR التجميع | A | "تجميع الكابلات" (term, glossary, line) |
| G S15.3 Impedanz | M | DE/EN changed to Wechselstromwiderstand / AC resistance; AR already uses المعاوقة (no change) |
| Own: AR "القصر" alone | A | Now "القصر الكهربائي" (TERMS.md), also title |
| Own: S8.5 AR line edge | A | Rewritten so it does not end in a Latin identifier |
| Own: `next` chain | A | E-B03 -> E-B04 (lightning/surge), already correct, normal Arabic sentence; AR كابل form used |
| Own: `stand` | A | Softened claims listed |

Rejected findings: none.

Needs primary-source check: DIN VDE 0298-4 current edition; Beiblatt 2 content (equations for maximum length); Durchlasswert I²t < k²S² (secondary ABB source); "Wechselstromwiderstand" wording for loop impedance.
