# Applied audit findings: E-B01 (scripts/E/01-din-vde-0100.json)

Legend: A = applied, M = modified (corrected variant), R = rejected. S = scene, L = line (original numbering). F = facts finding, G = language finding. Rejected findings: none.

| Finding | Result | Reason |
|---|---|---|
| F S18.4 rule 3 without "allpolig" | A | DE/AR/EN now say allpolig / جميع الأقطاب (E-F05 wording). Not in research facts, flagged for primary-source check |
| F S18.0 slide item 3 | A | "3. Spannungsfreiheit allpolig feststellen" |
| F S20.6 absolute "nur eine Elektrofachkraft" | A | Elektrofachkraft or under its direction and supervision, per the five safety rules |
| F S4.3 / S4 title / S19.2 groups 100-700 | M | Group 800 added (research fact on DIN VDE 0100-801); slide heading, table row, S19 line and summary item adjusted; tts added |
| F S7.4 AR Schutzpotentialausgleich | M | TERMS form الربط الوقائي المتساوي الجهد; DE rephrased as "Erdung und Schutzleiter, dazu gehört auch der Schutzpotentialausgleich" |
| F S3.7 DKE as national standards body | A | DKE = Fachstelle, supported by DIN and VDE; slide row and tts fixed |
| F S19.6 "Errichten dürfen ..." | A | "erfolgt durch Elektrofachkräfte oder unter ihrer Leitung und Aufsicht" (DE/AR/EN) |
| F S16.7 / S16.6 / S16.8 unsupported laiman/absolute claims | M | L7 softened (no "Näheres", L16.9 already links to the video), L6 and L8 deleted; slide heading changed to "Wer errichtet und ändert Anlagen?", L1 and S1.5 no longer "darf" |
| F S17.2 NAV not spelled out | A | "Niederspannungsanschlussverordnung, kurz NAV", tts En-A-Fau; wording of § 13 NAV still to be checked against the primary source |
| F S15.4 / S15.2 unsupported report content | A | L2 limited to results of inspecting/testing/measuring, L4 deleted, slide items replaced, term Stromkreis replaced by Prüfbericht |
| F S18.8 reverse order when switching on | A | Line deleted (not in facts) |
| F S2.7 / S2.8 / S11.9 / S2.2 Schutzgüter | M | No source in research, so claim removed instead of adding a fact: general "Schutz vor Gefahren", L7/L8 deleted, S11.9 reworded, slide items changed; moved to "dropped" |
| F S13.8 basic protection still needed | A | Line deleted, moved to "dropped" |
| F S7.4 title of Part 540 | M | Not quoted as a title; "behandelt Erdung und Schutzleiter" (see above) |
| F S9.9 series covers modern systems | M | Line deleted instead of rewritten (Part 712 already in S9.5) |
| G title.ar ends with digits | A | Ends with "الألمانية" |
| G next.ar ends with (RCD) | M | Latin in the middle: "وجهاز (RCD) الحماية من تيار العطل" (E-B02 term, same in S7.6 and S20.7) |
| G glossary Elektrofachkraft AR | A | الكهربائي المؤهَّل |
| G quiz Q1/Q5 AR digits | M | Eastern digits plus "من السلسلة" so the option ends in Arabic |
| G quiz Q3 AR digits | A | "في معيار ... نفسه" |
| G quiz Q4 AR "هيئة DKE" | A | "هيئة DKE للتقييس" |
| G S7.6 tts Er-Ce-De | A | Er-Ze-De |
| G S20.7 tts Er-Ce-De | A | Er-Ze-De |
| G quiz Q5 wording | A | "besondere Bereiche", إضافةً إلى |
| G RCD AR variant | A | جهاز (RCD) الحماية من تيار العطل in next, S7.6, S20.7 |
| G S1.2 AR منشآت | A | Done |
| G S3.2 AR | A | Done |
| G S4.5 object fronting | A | DE and tts reworded |
| G S7.4 AR | A | See F S7.4 |
| G S11.5-11.8 order | A | Name plus explanation per level (DE/AR/EN) |
| G S12.8 grammar | A | DE/AR/EN |
| G S13.9 / S13.11 redundancy | A | S13.11 deleted, S13.9 reworded |
| G S16.3 EN | A | "This means erecting, modifying and maintaining." |
| G S16.7 AR Bezugsnomen | M | "والشخص غير المؤهَّل (Laie)" within the softened sentence |
| G "also" filler | M | Removed in S2.6, S10.8; S2.7/2.8, S9.9 deleted; other occurrences left |
| G S4.9 recap position | A | Recap moved to end of scene 4 |
| G S17.4 tts ZVEH | A | Zett-Fau-E-Ha |
| G S17.5 "verantwortliche" | A | Lowercase |

Further changes: TERMS.md applied (Prüfbericht as محضر الفحص in glossary and scenes 8/15, Elektrofachkraft in S8.7 softened to "oder unter deren Leitung und Aufsicht"), S12 table row shortened to 50 characters, quiz answers varied (2, 0, 1, 2, 1) with Q4/Q5 options reordered, `stand` extended, removed claims added to "dropped" in docs/research/E-B01.json.

Needs a primary-source check: "allpolig" in rule 3 (DIN VDE 0105-100), wording of § 13 NAV, group 800 / DIN VDE 0100-801, DKE role.
