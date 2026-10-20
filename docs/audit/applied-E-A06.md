# Applied audit findings: E-A06 (scripts/E/06-netzqualitaet.json)

Legend: A = applied, M = modified (corrected variant), R = rejected. S = scene, L = line (original numbering). F = facts finding, G = language finding.

| Finding | Result | Reason |
|---|---|---|
| F S20.9 "Grenzwerte nur dort" | A | Suggested wording in DE/AR/EN/tts; `stand` softened too |
| F S2.4 "nur in der aktuellen Norm" | A | "in den aktuellen Normen" |
| F S8.8/8.9 Wirkleistung / "vor allem thermisch" | M | 8.8 deleted; 8.9 replaced by the suggested "zusätzlich belasten, z. B. durch Erwärmung" (matches facts) |
| F S18.9 capacitor maintenance | A | Deleted (not in facts, unsafe for lay reader) |
| F S16.4 spoken math | A | "Wurzel aus der Summe von 3600 und 6400", DE/EN/tts |
| F S4 card 4 "Verfügbarkeit" | A | Card now "Einbrüche und Unterbrechungen"; flicker not added (cards limit 4, curve shape covers distortion) |
| F S15.8 Verzerrungsblindleistung | A | Deleted; claim moved to "dropped" |
| F S19.4 / 19.7 billing permission | M | 19.4 per suggestion; 19.3, 19.6 and slide item 3 softened to "je Vertrag/Preisblatt"; 19.7 ("Kompensationsanlage kann verlangt werden") deleted |
| F S0 cross-video AR terms | M | Impedanz = المعاوقة, Neutralleiter = موصل التعادل applied. Reactive power: TERMS.md is binding (القدرة غير الفعالة), not the suggested القدرة الردية; applied in this video, E-A04/E-A03 not touched (outside this task). EN Netzrückwirkungen = "grid feedback effects" (matches G S9.5, "disturbances" is used for Störungen). EN 21.5 unified to "engineering advice" (DE Ingenieurberatung, AR استشارة هندسية), as in other videos |
| F S5 research F2 outdated | M | Script already names no edition (kept); research note corrected |
| G quiz Q4 AR ends in Latin | A | Question reworded with Scheinleistung/القدرة الظاهرية in DE/AR/EN; answer index 2 unchanged and still unique |
| G S7.5 ممانعة | A | المعاوقة |
| G S10.7 case error | A | المقداران المميِّزان |
| G S14.4/14.5/20.6 AR Latin edge | M | 14.4 as suggested; 14.5 and 20.6 reworded (suggested "عمليًا"/"في علاقة واحدة" added meaning) |
| G S18.9 بنوك المكثفات | R | Line deleted (F S18.9) |
| G S0.0 جودة الطاقة / terms | M | جودة الطاقة everywhere (glossary, term, lines); القدرة الفعالة / غير الفعالة per TERMS.md instead of the suggested forms; E-A03/E-A04 not touched |
| G S2.0 quote slide, term | A | Layout changed to bullets, three items, term AR "المعيار" |
| G S5.7 reorder | A | Order 1,2,3,7,8,4,5,9,10,11,6; 5.1 AR also reworded (no Latin edge, removed "in Germany" not in DE) |
| G S8.5 Neutralleiter | A | موصل التعادل (lines, term, glossary) |
| G S9.5 EN | A | "grid feedback effects" |
| G S9.7 fragment | A | Full sentence DE/AR/EN |
| G S10.10 Regelwerke | A | مجموعات لوائح أخرى |
| G S11.4/11.6 | A | حالات القصر; الكونتاكتورات (TERMS.md) |
| G S12 table row | A | "Verzerrte Spannung \| Strom an Impedanz" plus new line after 12.4 in DE/AR/EN |
| G S14.4 tts P/Q/S | A | tts for 13.2, 13.3, 13.5, 14.4, 14.5, 17.7, 20.6 (Pe, Ku, Es) |
| G S16.7 order | A | Moved between 16.2 and 16.3 |
| G S16.8 | A | Suggested wording with 100 kVA / 60 kW incl. tts |
| G S18.4 AR | M | "خط التغذية" applied; "تيار ردي" replaced by "تيار غير فعال" (TERMS) |
| G S0.0 tts 9.4 | A | tts with pauses for 9.4 (and the same for 9.6); `next` shortened to avoid unspelled DIN VDE 0100 |
| G S8.8 "kaum Wirkleistung" | R | Replacement claim not in research facts; line deleted instead (see F S8.8) |
| G S10.12 | A | Deleted (duplicate) |
| G S17.2/17.7/17.8 | A | ظل الزاوية |
| G S18.7 | A | Deleted (duplicate of 18.10) |
| G S21.8 + `next` | A | "Im nächsten Video geht es um Niederspannungsinstallationen"; chain E-A06 → E-B01 |

Additional: القدرة الفعّالة -> القدرة الفعالة, القدرة الردية -> القدرة غير الفعالة, الملامسات -> الكونتاكتورات throughout (quiz, glossary, lines). Research: five claims added to "dropped", F2 note corrected. `stand` softened. Validator: 0 issues.
