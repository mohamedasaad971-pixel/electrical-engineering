# Applied audit findings: E-A02 (scripts/E/02-netzanschluss.json)

Legend: A = applied, M = modified (corrected variant), R = rejected. S = scene, L = line (1-based; line 0 = slide level). "F" = facts finding, "G" = language finding.

| Finding | Result | Reason |
|---|---|---|
| F S4.3 publisher name | M | Full name "Forum Netztechnik und Netzbetrieb im VDE" used (DE/AR/EN/tts). Name added to research facts as medium; primary check on vde.com |
| F S8.1 "keine bloße Empfehlung" | A | Replaced by "keine Gesetze, aber in der Praxis verlangt" (DE/AR/EN) |
| F S12.7 "Erst dann wird errichtet" | A | "In der Regel wird erst nach der Rückmeldung gebaut" |
| F S12.10 "Bauen Sie nicht, bevor..." | A | "Klären Sie mit dem Netzbetreiber, ab wann gebaut werden darf" |
| F S3.0 cards "besitzt"/"Auftraggeber" | A | Items changed as suggested; Anschlussnehmer AR/EN terms changed (see G rows) |
| F S11.0 heading "Wer haftet wofür?" | A | "Wer ist wofür verantwortlich?"; NAV § 13 rental sentence added to research facts (medium, primary check) |
| F S17.5 Installateur "meldet an" | M | "unterstützt bei der Anmeldung" (DE/EN as suggested); AR uses TERMS term "التسجيل لدى مشغّل الشبكة" instead of "الإبلاغ"; slide row 3 changed |
| F S0 MaStR terminology | M | TERMS.md is binding: AR "السجل الرئيسي لبيانات سوق الطاقة", EN "core energy market data register (MaStR)" (audit AR variant not used); glossary, slide 16 term, S16.6 |
| F S5.11, S15.9, S9.10, S8 item 4 | A | S5.11 and S15.9 deleted; S9.10 deleted entirely (stronger than dropping "oft"); S8 item 4 -> "Netzbetreiber-Bedingungen beachten" |
| F S5.9 Zählerplatz typisches Thema | A | Deleted (not in facts, same note) |
| F S14.9 "kostet wenig Zeit" | A | Deleted (unsupported) |
| F S16.3 protocol content | M | Replaced by neutral "Darin hält er die Inbetriebsetzung der Anlage fest" (no new claim) |
| F S16.10 MaStR duty "Sache des Betreibers" | M | Not flagged by audit, deleted as unsupported (who registers is not in facts) |
| F S6.7 "ersetzt 2018-11" | A (kept) | Kept as suggested; in stand for re-verification on vde.com |
| F S8.5 presumption rebuttable | A | DE/AR/EN/tts extended; note added to research fact. Not in this research file's facts originally, so flagged |
| F S8.2 tts "kurz E-En-We-Ge" | A | tts equals de now; AR "قانون الطاقة الألماني" |
| F S12.4 AR "التسجيل" ambiguity | M | TERMS.md keeps "التسجيل لدى مشغّل الشبكة" for Anmeldung (binding), so "الإبلاغ" rejected; Registrierung (MaStR) now "الإدراج في السجل (الرئيسي)" in S12.8/S16.6; S1.3 rewritten as suggested |
| F S16.0 dropped-list check | A | No action; new dropped items added to research |
| G Q1 options | A | Options rewritten (DE/AR/EN), answer stays 2 |
| G S4.2 TAR | A | DE TAR, tts Tar, AR Latin moved off edge, EN TAR |
| G S4.3 FNN | A | DE FNN, phonetic only in tts |
| G S4.5, S4.6, S4.7 | A | AR edge digits fixed |
| G S5.4, S6.6, S6.7 | M | Edge digits fixed; "ميلاديًا" not used (edition date is not a calendar label), "كما يظهر في عنوانه" instead; S6.7 as suggested |
| G S7.4 | A | AR edge fixed |
| G S8.4 | A | "من القانون" |
| G S9.2 TAB | A | DE TAB, tts Tab, AR "تاب" hint; other de lines S9.7, 9.8, S18.3, S19.4 now TAB |
| G S9.4 | A | AR "رابطة VDE الألمانية" |
| G S10.2 NAV | A | DE NAV, tts En-A-Fau |
| G S15.4 gender | M | "تذهب الكهرباء المولَّدة إلى الشبكة" ("كلها" omitted to match DE) |
| G S19.2, S19.3 | A | AR edge fixed |
| G glossary NAV + MaStR | A | Two entries added (20 total) |
| G EN he/his | A | Replaced by neutral forms in S11.4, S12.6, S15.5, S16.5, S17.4, S17.6, S19.4, Q3 |
| G S3.7 AR agreement | A | "وتقوم بالأعمال شركة تركيب كهربائي" |
| G S8.2 AR | A | "قانون الطاقة الألماني" |
| G S10.9 DE | A | "Es gewährt das Recht..." (AR/EN adjusted) |
| G S11.0 heading | A | Same as facts row |
| G S12.4 AR التسجيل | M | See F S12.4 row; TERMS governs |
| G S14.4 AR | A | "حماية الشبكة والمنشأة" |
| G Q5 option 3 | A | "Nur nach Gefühl entscheiden" (DE/AR/EN) |
| G S9.10 tts note | A | de lines now read TAB |
| G S14.2 AR "تضر" | A | "لا تُحدث اضطرابًا" |

## Additional changes (brief)
- Anschlussnehmer: AR "صاحب الاتصال بالشبكة" per TERMS (glossary with "(المنتفع بالتوصيل)"), EN "connection customer" (E-A03 still says "connection owner"); slide S10 row "Anschlussnehmer | Auftraggeber" -> "lässt anschließen".
- Quote slides S2 and S20 (one-line quotes) -> bullets with real content from the scene.
- `next` -> E-A03 (rechtlicher Rahmen); S20.7 matches. Quiz answers 2,0,1,2,1 each with exactly one correct option.
- Research: stand updated; two facts added (NAV § 13 rental, publisher name), six claims moved to "dropped".

Rejected: none outright (two audit variants replaced by TERMS-conform wording, see M rows).

Primary-source check needed: VDE FNN full name, widerlegbare Vermutung (§ 49 EnWG), NAV § 13 rental sentence, ersetzte Ausgabe 2018-11 of VDE-AR-N 4105.
