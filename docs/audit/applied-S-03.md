# Applied audit findings: S-03 (scripts/E/03-netzberechnung.json)

Legend: A = applied, M = modified (corrected variant), R = rejected. S = scene, L = line. "F" = facts finding, "G" = language finding.

| Finding | Result | Reason |
|---|---|---|
| F S3.9 AR gender "هذه الفحص" | A | "هذا الفحص فحص «ن ناقص واحد»" |
| F S19 slide feature list / 19.2 "bekannte" | M | Slide item "Laut Hersteller: ähnliche Aufgaben"; 19.2 "Zwei Beispiele sind ..."; AR ends in Arabic (G suggestion), no Latin edge |
| F S3.11 "Rechnen kostet wenig" | M | Line deleted (3.3 already covers danger; the suggested "sehr teuer" replacement would duplicate it) |
| F S9.3 inverter contribution | A | "hängt vom Modell ab" DE/AR/EN; slide row "Einspeisebeitrag, modellabhängig"; claim moved to dropped |
| F S12 row "Einstellwerte als Vorschlag" | A | "Bild der Staffelung zur Bewertung" |
| F S4.8 Netzanschluss vs. external grid | A | "externes Netz / Bezugsknoten" in 4.8, 4.10, 4.11, 7.4, 17.4, slide rows (S4, S7, S17), glossary (replaced "Netzanschluss"); dropped list updated |
| F S17 / 17.7 IEC 60909 "nach" | A | "Laut Dokumentation ... mit Einschränkungen"; slide row "laut Doku" (kept ≤50 chars); tts adapted |
| F S19.2 DIgSILENT note | R | Suggested fix is "none" |
| F S15 slide "nur mit Qualifikation" | M | Two items: "Arbeit an Anlagen: Elektrofachkraft" + "... oder unter deren Leitung und Aufsicht" (full sentence does not fit 50 chars); five items total |
| F S16.6 / 20.8 / 20.2 evaluations | A | 16.6 reduced to "kann ein Einstieg sein" (the "Lehre, Forschung" usage removed as unsourced); 20.8 "kann genügen"; 20.2 "in vielen Programmen ähnlich" |
| F S18.4 AR "محوّلات" | A | "أدوات تحويل" |
| F S16.3 pandapower licence | R | Suggested fix is "none"; sentence already hedged |
| F S12.7 "jede Koordination wertlos" | A | "nicht belastbar" DE/AR/EN |
| G S3.9 AR | A | See F S3.9; also DE `de` now "(n-1)-Prüfung", tts "En-minus-eins-Prüfung" |
| G quiz 5 AR Latin end | M | "أي عبارة بشأن pandapower صحيحة؟" (ends in Arabic) |
| G S15.5 rule 3 AR | A | "التحقق من انعدام الجهد في كل الأقطاب" |
| G S4.9 order | A | Detailgrad line moved to end of scene |
| G S8.5 AR poles/phases | M | AR "ثلاثي الطور / أحادي الطور مع الأرض" (meaning of dreipolig/einpolig); DE/EN keep the standard terms |
| G S9.6/10.3/quiz 2 "أجهزة التوصيل" | A | "أجهزة القطع والوصل" |
| G S11.3 AR ambiguity | A | Applied |
| G S11.7 Staffelplan | A | Glossary entry "der Staffelplan / مخطط التدريج / grading plan" added; 11.7 AR |
| G S12.9 repeats 11.8 | A | 12.9 deleted |
| G S12.0 row 51 chars | A | "Passt die Kennlinie zum Fehlerstrom?" |
| G S17.0 row 52 chars | M | "Schritt 3 | Lasten, Erzeuger, externes Netz" (replaces Netzanschluss as above) |
| G S13.8 EN | A | "misleading" |
| G S4.2 EN | A | "simplified representation" |
| G S7.10 / 20.7 EN | A | "grid operator" |
| G S15.3 | A | DE and AR as suggested ("إدارته وإشرافه"); EN "carried out by" |
| G S18.4 AR | A | See F S18.4 |
| G S19.2 AR padding "معًا" | A | Removed (merged with F S19.2) |
| G S19.7 AR | A | "ولا نقدّم عمدًا أي معلومات عن الأسعار أو الانتشار." |
| G S22.6 AR padding / tts | M | Line and `next` now name the real next video title (Simulation in der Elektrotechnik: Modell, Solver, Ergebnisse prüfen) instead of MATLAB/Simulink/LTspice, which are not in the title of that video; no tool names, so no tts needed |
| G next format | M | Full sentence naming the real title, no Latin edges, no internal ID |
| G glossary "quelloffen" | A | "die Quelloffenheit / المصدر المفتوح"; slide term adapted; "المنحنى المميِّز" at first mention (12.1/12.2) |
| G quiz distractors | M | Q1 "Lebensdauer der Leitungen", Q2 "Spannung am Leitungsende", Q3 "Nur das Gerät am Anfang des Netzes schaltet ab", Q4 "Rechengeschwindigkeit" / "Anzahl der Leitungen"; answer indexes unchanged (1,2,0,1,2), one correct each |
| G S2 / S22 duplicate disclaimer, slide 22 bullet | A | Slide 22 third bullet "Normen und Software ändern sich"; scene 2 disclaimer left (repeat is intentional framing) |
| G S1.6 tts Paiton (+16.2, 16.7) | A | "Püton" |
| Own: S1 slide kicker "S-03 · Software" | A | Internal ID removed ("Software-Reihe") |
| Own: research file | A | `dropped` extended, `stand` updated in docs/research/S-03.json and in the script |

Rejected: F S19.2 DIgSILENT note (no fix), F S16.3 licence note (no fix).

Primary-source checks needed: pandapower BSD licence file and version-specific short-circuit fault types; IEC 60909-0 edition/draft status; ETAP/DIgSILENT company facts; "Bezugsknoten" as textbook term for external grid.
