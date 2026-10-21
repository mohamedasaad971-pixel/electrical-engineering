# Applied audit findings: E-D02 (scripts/E/02-dokumentation-uebergabe.json)

Legend: A = applied, M = modified (corrected variant), R = rejected. S = scene, L = line. "F" = facts finding, "G" = language finding.

| Finding | Result | Reason |
|---|---|---|
| F S14.5 + S14 card "Vertrag: Regelt die Rechtsfolgen" | M | TERMS.md wording: Gesetz (BGB) und/oder VOB/B, falls vereinbart, sowie Vertrag; card "Gesetz und Vertrag: Rechtsfolgen"; tts added; flagged for legal check |
| F S15.5 TTS 82079 / G S15.5 | A | "acht zwei null sieben neun", I-Tripel-E; line now says "allgemeine Grundsätze" (matches research) |
| F S8.6 / G S8.6 order logic | M | New line "Zuerst besichtigen..., dann erproben..., danach Messung" placed before "Am Ende bewerten"; old L6 removed |
| F S8.7/8.8 "spart Zeit und schützt die Geräte" | A | L7 and L8 deleted (unsupported) |
| F S1.3 absolute | A | "in der Regel" |
| F S19.8 absolute | A | "in der Regel ... der Vertrag legt die Details fest" |
| F S14.3 / L10-11 / card Restpunkte | M | L3 softened (contract sets it), L10-L11 deleted, cards "Einweisung: Oft für den Betreiber", "Restpunkte: Offene Punkte notieren"; AR "تدريب" without Latin bracket (edge rule) |
| F S15.8 Betriebsanleitung contents | A | L2 replaced (typically operating hints, contract sets scope), L3, L4, L8, L10 deleted, slide items replaced; L7 softened |
| F S7.2 / L8 | A | L2 reworded, L8 deleted, L9 deleted (duplicate); slide item "Nach Fertigstellung" |
| F S5.5 Revisionsstand Pflicht | A | "Es empfiehlt sich" |
| F S12.11 signature | M | Line deleted (L4 already names Prüfer, Datum, Unterschrift) instead of rephrasing a duplicate |
| F S11.8 multimeter | A | Suitable-instrument wording |
| F S9.8 not every step de-energised | M | Line deleted rather than reworded (any wording on live testing could read as permission); L6 now "unter Spannung stehende" (rule 5), slide item 5 adjusted; all five rules intact |
| F S17.2 fixed number | A | "verbindliche feste Zahl ... nicht"; slide item 1 adjusted |
| F S18.9 + S13 row operator | A | "in der Regel"; row "In der Regel verantwortlich" |
| F S13.11 / S3.9-3.10 legal protection | A | "hilft, Fehler zu vermeiden"; S3.9 merged, S3.10 deleted |
| F S2.5 / S20.6 verantwortliche EFK | A | "eine Elektrofachkraft in Ihrem Betrieb" (AR with الكهربائي المؤهَّل per TERMS) |
| F S10 heading / Prüfstatus | A | "typischerweise", row "Typ und Nummer" |
| F S4 EN Stromlaufplan | A | schematic (term, L3) |
| F S18.4 EN ordinance | A | Industrial Safety Ordinance |
| F S7.5 / S13.2 AR befähigt | M | "befähigt" dropped everywhere (see G); AR كهربائي مؤهَّل |
| F S16.2 TTS | A | De-Ge-U-Fau Vorschrift drei |
| F S1.1 Markt und Praxis | M | Changed to "Praxis" (kicker + L1 DE/AR/EN); conflicts with G suggestion to keep "Markt und Praxis"; E-D03 still says "Berufsalltag" (see concerns) |
| G S0 quiz Q1 Latin edge | A | "ماذا يعني مصطلح As-built في الوثائق؟" |
| G S0 glossary Abnahme AR | A | الاستلام الرسمي |
| G S14 term Abnahme AR | A | الاستلام الرسمي |
| G S2 term Betreiber | A | "der Betreiber", AR without Latin |
| G S5 term As-built | A | "das As-built", AR الوضع المنفَّذ فعليًا |
| G S15.5 TTS | A | See F |
| G S8.6 | M | See F |
| G S17.10 AR | A | يقدّم لكم المختصون المشورة... |
| G S16.4 + row 5 | M | Full "Elektrofachkraft oder Person unter Leitung und Aufsicht"; table split into two rows (≤50 chars each) |
| G S0 quiz Q4 | M | Question "Wie werden ... festgelegt?"; options reordered, answer index 1 |
| G S10.3 AR | A | وتُضاف إلى ذلك مقاومة العزل |
| G S10.4 AR | M | TERMS.md E-D: قواعد "قاطع التيار المتبقي (RCD)" instead of the suggested "جهاز الحماية من تيار العطل" |
| G S0 glossary As-built entry | A | Added; articles already present in glossary; plurals not added |
| G S0 slide terms articles | A | All terms now with articles |
| G S0 quiz distractors | A | Q1/Q2/Q3/Q5 as suggested; answers now 1,2,0,1,2 |
| G S0 next pointer | A | "...Projektarbeit, Verträge und Qualitätsmanagement" in next and 20.8 (DE/AR/EN) |
| G S9.2 fragment, 9.7 "Video fünf" | A | Full sentence; "Video über Elektrosicherheit" |
| G S7.5 / S13.2 / slides befähigt | A | Elektrofachkraft only; items "Durch eine Elektrofachkraft", "Prüfen \| Elektrofachkraft" |
| G S7.8 unclear | A | Line deleted (F finding) |
| G S7.4 AR Teil 600 | A | في جزئها ٦٠٠ (Arabic-Indic digits to avoid digit at line edge) |
| G S4.5, S4.8 AR | A | As suggested |
| G S5.3 TTS As-built | A | "Es-Bilt"; AR line also reworded to have Arabic edges ("بمصطلح As-built") |
| G S6.8 EN/AR | A | As suggested |
| G S9.8 / 12.1 / 19.1 EN British | A | 9.8 deleted; "sums up", "summarise" |
| G S11.3 Normale | A | DE/AR/EN as suggested |
| G S12.2, 12.4 AR | A | As suggested |
| G S14.3 / 14.10 AR Einweisung | M | 14.3 "تدريب" without "(Einweisung)" (Latin edge); 14.10 deleted (F) |
| G S10.7, 10.12 AR | A | As suggested |
| G S8.1 three steps | A | "drei Kernschritte und ein Ergebnis" |
| G S18.4 EN | A | See F |
| G S1.1 section name | M | See F: "Praxis" chosen |
| G S2/S20 disclaimer, 20.4, 19.1, 19.8 AR | A | 20.4 verb, 19.1 لنلخّص, 19.8 with "عادةً" |
| G S16.2, 16.9 AR | A | 16.2 includes (DGUV V3) mid-line per TERMS.md; 16.9 as suggested |
| G S5.3 note (keep As-built) | A | No change beyond edge fixes |

No finding rejected outright. Extra change (not from a finding): S6.5 "Oft legt der Vertrag fest..." (softened).

Other: `stand` extended, 11 claims added to "dropped" in docs/research/E-D02.json; validate.py: 0 issues; quiz/glossary/term Arabic checked for Latin edges separately (validator does not cover them): none left.
