# Applied audit findings: E-A04 (scripts/E/04-speicher-wechselrichter-laden.json)

Legend: A = applied, M = modified (corrected variant), R = rejected. S = scene, L = line. "F" = facts finding, "G" = language finding. Validator: 0 issues.

| Finding | Result | Reason |
|---|---|---|
| F S0 Wechselrichter AR "المحوّل" | A | "العاكس" throughout (title, lines, slide terms, glossary, quiz); no "محوّل" left |
| F S1.2 | A | AR/DE with Wechselrichter and العاكسات |
| F S14.3 wrong party | M | Anschlussnehmer with TERMS wording "صاحب الاتصال بالشبكة"; slide card 1 adjusted |
| F S15.2 / 2.3 vs 15.6 contradiction | A | 2.3 now "no calculation examples and only a few numbers"; 15.6 reworded as threshold above 12 kVA, roughly 11 kW |
| F S9.7 central NA-Schutz | A | Line deleted (unsupported) |
| F S7.10 shortened rule one | A | Replaced: does not replace the five safety rules, isolating is only the first step |
| F S17.9 EV-RCM | M | Term replaced by RDC-DD (named in research F23 with IEC 62955); tts Er-De-Ze-De-De; check against the standard |
| F S17.2 absolute RCD statement | A | "Nach DIN VDE 0100-722 wird ... gefordert"; note added in the research file; check against the standard text |
| F S2.4 absolute liability | A | Neutral wording; S14.2 also changed to safety/responsibility; S14 heading "Rollen und Verantwortung" |
| F S16 slide item "nicht verzögert" | A | "Keine Verzögerung wegen lokaler Überlast"; 16.6 also limited to refusal/delay due to possible local overload |
| F S12.9 "gemeinsame Fassung" | A | "gemeinsamer Hinweis"; de keeps 2025, tts spelled |
| F S20.7 / next teaser | A | E-A05 = Schutztechnik in Netzen und Anlagen (matches E-A05 title) in 20.7 and in `next` |
| F S3 add check to 12.7 | A | New line after 12.7: check that the note matches the valid edition |
| F S0 Installateurverzeichnis AR | A | "سجل المُركِّبين المعتمدين" in slide term, 14.5, glossary; Errichter = المُركِّب |
| F S4.11 / 9.3 unsupported claims | A | 4.11 and 9.3 deleted; 11.5 and 11.8 (fernsteuerung / Inbetriebnahme-Einstellung) and 16.9 (EMS) also deleted for the same reason, slide 11 item 3 replaced by "Einstellungen laut Anschlussregel" |
| F S2.5 Netzanschluss work | M | NAV-based wording (Netzbetreiber or registered company with Elektrofachkraft); AR rewritten so it does not end in Latin |
| F S14.4 NAV | M | Suggested "Hausanschlusssicherung/Verantwortung" is not in the research file; kept to research F21: section 13 NAV for Errichtung and Änderung der Kundenanlage (check wording) |
| F S13.3 Schaltplan | A | Removed from the Anmeldung list |
| F S8.6 TTS unify | A | "Fau-De-E A-Er-En" in 8.6, 12.2, 12.4; 10.6 de written as IEC 62116; 16.1/16.4 EN "Energy Industry Act" |
| G S0 next | M | Full-sentence format like other videos, content as F S20.7 (not the shorter suggestion) |
| G S2.5, 5.8, 14.6 Latin at AR line end | M | Reworded so the line ends in Arabic ("... (Elektrofachkraft) مختص") |
| G S0/S4 inverter terminology (all lines) | A | See F S0 |
| G S8.1 garbled AR | A | Applied |
| G S10.1 | A | Applied |
| G S10.6 | A | de written, tts spelled |
| G S17.4 | A | de "RCD", tts Er-Ze-De |
| G S17.9 | M | See F S17.9 |
| G Marktstammdatenregister AR | M | TERMS.md wording "السجل الرئيسي لبيانات سوق الطاقة" (binding) instead of the suggestion |
| G Installateurverzeichnis AR | A | See F S0 |
| G Anschluss/Anmeldung AR | M | Anschluss -> التوصيل (1.4, 11.6, 12.2, slide 12 term, 19.8) applied; Anmeldung -> الإبلاغ rejected: TERMS.md fixes التسجيل لدى مشغّل الشبكة |
| G glossary Errichter | A | "der Errichter" added; المُركِّب in 12.8, 13.5, 14.7, 18.8 |
| G S2 quote slide | M | Replaced by bullets with three items; Elektrofachkraft term moved to slide 14; slide 20 likewise turned into bullets with four items |
| G S3.9 plural | A | Applied |
| G S4.3 order | A | 4.3 before 4.2, reworded |
| G S8.6 tts | A | See F S8.6 |
| G S9.7 order | R | Moot, line deleted (F S9.7) |
| G S10.3 | A | Applied |
| G S10.8 | A | Applied |
| G S10.11 | A | Applied with tts |
| G S15.1 Wallbox AR | A | "وحدة الشحن الجدارية" in 15.1, 16.6, glossary |
| G S15.6 AR | R | Superseded by F S15.2 wording of 15.6 |
| G S16.5 | A | "Tauschgeschäft" |
| G S16.7 EN | A | "it may" |
| G Quiz Q3 distractors | M | Replaced by "Die Netzfrequenz steigt über den Sollwert" and "Eine Batterie wird tiefentladen"; the suggested "inverter disconnected from the grid" is not used because it could be read as correct (exactly one correct answer) |
| G S5.2 Merkhilfe | A | Applied |
| G S6.1 Speicher AR | A | "المخزن" in 6.1, 6.5, 6.6, 13.6, 19.3 |
| G S6.4 redundant tts | A | tts removed where identical to de and not needed (1.1, 6.4, 16.1, others) |
| G S6.9 duplicate | A | Deleted |
| G S16.3 order | A | Moved after 16.7 |

Extra: slide 4 row "Umrichter" -> "Wechselrichter"; slide 15 last row without "Frist"; `stand` and research file (EV-RCM removed from F23, dropped list extended) updated. Quiz answers: 1, 0, 2, 1, 2.

Primary-source check needed: DIN VDE 0100-722 RCD requirements; RDC-DD / IEC 62955; NAV section 13 wording; BNetzA threshold 12 kVA / about 11 kW; current editions VDE-AR-N 4100/4105 and the FNN note of October 2025.
