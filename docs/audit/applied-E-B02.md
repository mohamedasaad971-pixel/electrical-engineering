# Applied audit findings: E-B02 (scripts/E/02-erdung-rcd.json)

Legend: A = applied, M = modified (corrected variant), R = rejected. S = scene, L = line. "F" = facts finding, "G" = language finding.

| Finding | Result | Reason |
|---|---|---|
| F S9.11 IT deadline "Ermessen des Betreibers" | M | Line 11 deleted; L10 now ends "prüfen Sie die aktuelle Norm" (DE/AR/EN). Claim moved to dropped, research fact F11 corrected |
| F S6.8 fault current "not via ground" | A | "im Wesentlichen über Leiter, nicht hauptsächlich über das Erdreich" |
| F S2.4 only Elektrofachkräfte | A | "oder unter deren Leitung und Aufsicht" (DE/AR/EN) |
| F S18.8 (same issue, milder) | A | Same wording added |
| F S12.8 "gilt für jedes Gebäude" | A | Replaced by "Teil der Schutzmaßnahmen nach der Normenreihe" |
| F S14.11 RCD protects people | M | Softened to "soll ... Gefahr verringern" as suggested; L9 "sehr kleine Fehlerströme" also replaced by "reagiert auf Fehlerströme gegen Erde, nicht auf den Betriebsstrom" (principle already in F18) |
| F S10.5 RCD "oft im TN" | A | Line and slide row now "im TT üblich" |
| F S7.8 who decides the PEN split | A | "richtet sich nach den Anschlussbedingungen des Netzbetreibers" |
| F S12.4 absolute voltage claim | A | "sollen ... auftreten" / "is meant to prevent" |
| F S6.6 "sehr verbreitet" | A | "verbreitet" |
| F S17.1 "Jeder RCD hat Prüftaste" | M | L1 softened ("in der Regel"). L6 (inform an Elektrofachkraft if no trip) kept: safety direction, not a technical claim |
| F S18.10 reverse order | A | Kept; E-F05 research (F19) contains it, source added to F24 in research file |
| F S4.2 source = transformer | A | "zum Beispiel am Transformator" |
| G title.ar ends with RCD | A | Suggested title applied |
| G next.ar Latin edge / German word | A | AR "نتناول حساب مقاطع الكابلات"; S20.6 aligned; chain E-B02 -> E-B03 |
| G glossary AR Latin edges | M | RCD entry "جهاز RCD للحماية من تيار العطل" (keeps the abbreviation inside); Elektrofachkraft without Latin |
| G quiz Q1/Q2/Q5 AR edges | A | Rephrased with "تحديدًا"/"نفسه"; DE/EN adjusted ("genau", "selbst") |
| G S2 term Elektrofachkraft | A | Latin removed |
| G S14 term RCD | M | "جهاز RCD للحماية من تيار العطل" (no Latin edge) |
| G S16.1 tts RCDs | A | "Er-Ze-Des" |
| G quiz distractors Q1/Q4 | A | "Die Anzahl der Phasen", "Durch die Spannung am Gehäuse" (DE/AR/EN); answers stay 1,0,2,1,2, one correct each |
| G S2.4 "machen" | M | Covered by the legal fix (F S2.4) |
| G S4.4 etc. single letters tts | M | de keeps letters; tts now spells T/I/N/S/C (Te, I, En, Es, Ze) in 4.4, 4.6, 5.1-5.3, 5.5, 6.2, 6.5, 7.5, 19.2, 19.3, 19.8 |
| G S7.4 "Unversehrtheit" | A | "Darum muss er immer intakt sein." |
| G S8 "المؤرِّض" | A | "قطب التأريض" in term, 8.3, 8.4, 9.4, 10.3, glossary |
| G S8.6 AR wording | A | Applied |
| G S9.11 Ermessen rewrite | R | Line deleted (see F S9.11); the proposed rewrite "ergibt sich aus der Norm und den Betriebsbedingungen" would add an unsupported claim |
| G S12.6 Versorgungssysteme | M | DE "Versorgungsleitungen", EN "supply lines", AR "خطوط التغذية المعدنية" (no "pipes"/water/gas, not in the facts) |
| G S14.8 AR "المُطلِق" | M | "وحدة الفصل في الجهاز" |
| G S15.2 AR short circuit | A | القصر الكهربائي (TERMS) |
| G S15.4 AR line/neutral | A | "موصل الطور وموصل التعادل", القصر الكهربائي; Quiz Q5 option 2 aligned |
| G S15.4 slide item L-N | M | "Kurzschluss Außenleiter-N: kein Differenzstrom" (50 chars max) |
| G S16.4 AR wording | A | Applied |
| G S1.8 redundant | A | Line deleted |
| G S6.9 repeats 6.7 | M | Replaced by "Darum ist der Schutzleiter im TN-System so wichtig." |
| G S18.3-6 match E-F05 | R | Already identical in meaning to E-F05 (allpolig kept, fixed order); no change needed |
| G S19.7 filler | M | "Wer ein Kurzzeichen erklären kann, hat es verstanden." (L8 kept, no duplicate) |

Counts: applied 24, modified 10, rejected 2.

Research file: F11 claim corrected, "Ermessen" claim and the absolute statements moved to dropped, `stand` updated; script `stand` extended.

Primary-source checks needed: TN fault-current path (conductor vs earth share), "Typ AC / Typ F" wording, claim that the RCD is "üblich" in TT, medical IT (DIN VDE 0100-710), reverse order when re-energising (E-F05 source, DIN VDE 0105-100).
