# Applied audit findings: E-A05 (scripts/E/05-schutztechnik.json)

Legend: A = applied, M = modified (corrected variant), R = rejected. S = scene, L = line. "F" = facts finding, "G" = language finding. Line numbers are those of the original script; deleted lines shift later numbers.

| Finding | Result | Reason |
|---|---|---|
| F S13.9 incomplete work sequence | M | Replaced by pointer to the five safety rules (first step only); EN/AR equivalent |
| F S13.10 | M | "Further steps known from the electrical safety video" (E-F05) |
| F S4 slide "Millisekunden" | A | "Tritt fast augenblicklich auf" |
| F S6.1 "älteste" | A | "klassisches Schutzorgan" |
| F S7.8 operating instruction | A | "lässt sich wieder einschalten"; 7.10 caution stays |
| F S21.3 absolute | A | "wichtige Schutzorgane"; slide item adjusted |
| F S10.6 EN back-up vs reserve | M | 10.6 EN "upstream fuse or back-up protection" (no "cascading": not in research); Reserveschutz EN is now "reserve protection" (S19 lines, slide, S21.7, glossary) |
| F S13.3 stronger than F10 | A | "soll ... anzeigen" |
| F S21.2 absolute | A | "üblicherweise verzögert" |
| F S12.9 / S17.8 / S18.9 / S8.7 unsupported | A | Lines 12.9, 17.8, 18.9, 8.7 and 6.8 deleted; slide 8 item 3 made general ("Für größere Anlagen und Netze") |
| G title AR | A | New AR title with Schutztechnik; E-A04 `next` must be adjusted in the E-A04 file (outside this task) |
| G quiz Q2 | A | DE/AR corrected, answer 0 unchanged. Answers now 1,0,2,1,2 (one correct each) |
| G Schütz AR (S1.6, 14, 15, 21, glossary, term) | A | الكونتاكتور everywhere |
| G S16.9 gender | A | تعمل كل حلقة |
| G slides 2, 10, 22 one-item quote | M | Replaced by bullets with 3 items; S10 item 1 shortened to 45 chars (suggestion had 62) |
| G S2.3 grammar | A | "Die Auslegung des Schutzes" |
| G S3 Kurzschluss AR | A | القصر (قصر الدارة) in term and glossary |
| G S5/S15/S9 table rows | A | Rows shortened (all ≤50); S9 rows 1 and 3 also shortened |
| G S5.4 AR | A | يمكن للحماية هنا أن تتأخر قليلًا في الفصل |
| G S6.7, 6.9 Leitung AR | A | الخطوط الكهربائية; EN 6.7/6.9 "lines" |
| G S7.2/7.3/7.6/8.5/20.4 Auslöser AR | A | عنصر الفصل; glossary entries Auslöser and Impedanz added |
| G S10.6 Vorsicherung | M | AR/EN/tts as suggested, EN without "cascading" |
| G S13.2 Freischalten AR | A | فصل الجهد; terms مفتاح العزل (المفصل) / مفتاح فصل الحمل (مفصل الحمل), also in glossary |
| G S17.8 AR | R | Moot: line deleted (F finding, unsupported) |
| G S19.3 | A | شبكة النقل |
| G S19.8 | A | DE/AR with object |
| G S19.9 | A | Sicherheitsnetz unter dem Drahtseil (DE/AR/EN) |
| G glossary note (Auslöser, Impedanz) | A | Both added |
| G tts note | M | tts added for 10.6 only; no other line needs tts (validator 0 issues) |
| G S6.4, 7.9 Sicherungseinsatz AR | A | خرطوشة المنصهر |
| G S6.8 "رخيص" | R | Moot: line deleted (unsupported claim) |
| G S12.5/12.6 upstream/downstream | A | جهة المنبع / جهة المصب |
| G EN UK spelling | A | summarise (S9.1, S21.1), recognises (S17.4) |

Rejected: none outright; two language findings (17.8, 6.8) are moot because the facts finding deleted the lines.

Also: `next` pointer already E-A06 (Netzqualität), unchanged. `stand` in script extended; claims moved to `dropped` in docs/research/E-A05.json.

Needs primary-source check: DIN EN 60898/60269 statements of Sicherung/LS (research confidence medium), Lasttrenner/Trenner wording against IEC 60947-3, VO (EU) 2017/1485 Art. 36 for Reserveschutz, "Vorsicherung/Back-up" AR term حماية الإسناد.
