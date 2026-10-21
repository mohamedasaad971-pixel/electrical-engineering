# Applied audit findings: E-C04 (scripts/E/04-industrienetzwerke.json)

Legend: A = applied, M = modified (corrected variant), R = rejected. S = scene, L = line. F = facts finding, G = language finding.

| Finding | Result | Reason |
|---|---|---|
| F S5 slide "serieller Vorgänger"/"Weiterentwicklung" | A | Heading "der klassische Feldbus", item "Zeitlich früher als PROFINET" |
| F S6.9 "offen, weil Spezifikation verfügbar" | A | Deleted; moved to dropped |
| F S15 slide "kein Entweder-oder" | M | "Beides \| oft ergänzend (Companion Specification)" (row ≤50 chars) |
| F S17 slide geschirmtes Kabel / RJ45 typisch | M | Slide and lines 17.2-17.4 softened (no "geschirmt", "robust", "häufig"); M12 item reworded |
| F S3.4 gemeinsame Verbindung | M | Suggested sentence applied; 3.3 and 3.5 (unsupported past/saving/fault claims) and 3.7 deleted; slide items reworded |
| F S12.4 Cloud | A | Deleted |
| F S6.8 name derivation | A | Deleted |
| F S10.1 Ring as instruction | A | "kann man einen Ring nutzen" in DE/AR/EN |
| F S14.9 order | A | Moved behind 14.5 |
| F S15.8/15.9 gateway, maintenance plans | A | Deleted |
| F S5.7 Modernisierungen | M | Suggested "Bestandsanlagen" sentence applied; 5.8 deleted, 5.9 reworded to Bestandsanlagen |
| F S20.6 "immer" | A | Absolute wording removed |
| F S4 slide "eigene Kabel" | M | Replaced by "Feldbus \| Klassisch, z. B. PROFIBUS DP" (research fact 8); rows ≤50 chars |
| F S16.5 OT priorities | A | "oft hohe Priorität" in DE/AR/EN |
| F S12.8 duplicate | A | Deleted |
| G glossary AR Latin edges | A | Five entries fixed; Switch uses TERMS form المبدّل الشبكي; Elektrofachkraft without Latin |
| G Quiz Q3 | M | DE/EN as suggested; AR "بروتوكول تكرار الوسيط" (no Latin edge) |
| G S3 term SPS | M | TERMS.md binding form المتحكم المنطقي القابل للبرمجة instead of E-C01 variant |
| G S2.4 "أولًا" | A | Applied |
| G S14.6/14.10/slide Sicherheit vs security | A | IT-Sicherheit / الأمن السيبراني; heading and item changed; TTS "I-Te-Sicherheit" |
| G title DE | A | "Industrielle Netzwerke: ... (Konzepte)"; slide-1 term aligned |
| G next | A | Normal sentence in DE/AR/EN |
| G glossary core terms missing | A | PROFINET, OPC UA, MRP, Ring added; "deterministisch" became "der Determinismus" (article rule) |
| G quiz distractors / longest-correct | M | Suggested changes applied; correct options also shortened in Q1, Q2, Q3, Q5; one correct answer each, answers 1,2,0,1,2 |
| G slide terms AR (S2, S3, S8, S16, S17, S18) | A | Latin tags removed |
| G S4 table rows >50 | A | Applied |
| G S7 row 52 chars | A | "schnell ≠ Echtzeit" |
| G S2 quote slide thin | M | Layout bullets, four items; S21 also bullets with four items |
| G S2.7 double adverb | A | Applied |
| G S6.6 TTS numbers | A | Digit by digit |
| G S12.7 TTS numbers | A | Digit by digit |
| G S6.8/6.9 reorder | R | Moot, both lines deleted for fact reasons |
| G S11.3/11.5 DCP, LLDP | A | Expanded in DE/AR/EN/TTS |
| G S13.5 comma | A | Applied |
| G S14.7 Integrität | A | "للنزاهة" |
| G S14.9 order | A | See F S14.9 |
| G S15.5 Companion Specification | A | Applied in DE/AR/EN/TTS |
| G S17.1/17.3/17.4 "الموصل" | M | "وصلة/وصلات" used; wording of 17.3/17.4 also softened (see F S17) |
| G S18.8 pronoun | A | Third person in DE/AR/EN |
| G S18 EN "he" (6 lines) | A | Gender-neutral "they" |
| G S16.8 teaser | A | Deleted |

Also done: TERMS.md terms (المستشعر for Sensor in 3.2/4.3, الكهربائي المؤهَّل in 2.5/19.2, slide terms); `stand` extended; nine claims added to "dropped" in docs/research/E-C04.json. Rejected findings: one (reorder, moot).
Concerns for primary-source check: line 8.4 and slide S8 "RT umgeht TCP/IP-Schichten" (not in research facts, left unchanged); 5.2 "RS-485" TTS style; safety rules wording (secondary source).
