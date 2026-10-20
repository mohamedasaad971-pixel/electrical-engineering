# Applied audit findings: E-A03 (scripts/E/03-erneuerbare.json)

Legend: A = applied, M = modified (corrected variant), R = rejected. S = scene, L = line. "F" = facts finding, "G" = language finding.

| Finding | Result | Reason |
|---|---|---|
| F S7.9 Regelung rendered "المراقبة" | M | TERMS.md binds «التنظيم/الضبط», not G's «التحكم»: "التنظيم والحماية" |
| F S12.3 EEG equipment stated absolutely | A | "je nach Anlage" in DE/AR/EN/tts; slide items 1 and 2 now "Je nach Anlage: ..."; fact claim softened in research |
| F S21.5 "Jede Anlage" in the MaStR | M | Narrowed to "Erzeugungsanlagen". "Speicher" not adopted (only in E-A04 research, not in this file). Same change in S15.2, slide 15, quiz Q3 |
| F S13 slide row Eigenverbrauch / heading "Zwei Wege" | A | Row deleted, heading "Zwei wichtige Wege für den Strom"; claim moved to dropped |
| F S13.2 "zwei Wege" absolute | A | "zwei wichtige Wege" (AR/EN equivalent) |
| F S12.6 Redispatch 2.0 | M | "Redispatch 2.0" in line, slide item, tts ("zwei Punkt null"); date not named (deliberately). AR keeps TERMS form «إعادة جدولة التوليد» (G wanted E-A01 «إعادة الجدولة», but TERMS is binding); glossary "der Redispatch" |
| F S16.5 Bußgeld | A | Replaced by "Weitere Rechtsfolgen regelt das Gesetz."; claim removed from research fact and moved to dropped |
| F S4.9 / S4.6 unsupported | A | 4.9 deleted, 4.6 rewritten to "besonderes Gewicht im Gesetz" |
| F S12.0 slide item Redispatch 2.0 | A | Item changed |
| G S7.9 control/monitoring | M | See F S7.9 |
| G S10.2 gender agreement + الربط | A | "يبقى واجب التوصيل بالشبكة ..." |
| G S11.1 edge Latin | A | Identifier moved to the middle |
| G S13.3 edge Latin | M | Own wording, identifier in the middle, ends in Arabic; EN "the operator" instead of "he" |
| G S14.5 edge Latin + EN | M | AR keeps Bundesnetzagentur in the middle; EN "Federal Network Agency (Bundesnetzagentur)" |
| G S15.2 edge Latin | M | "فيما يسمى بالألمانية Marktstammdatenregister، أي ..."; "Erzeugungsanlagen" (see F S21.5) |
| G S17.3 edge Latin + tts "im VDE" | A | AR identifier in the middle; tts "im Fau-De-E, kurz Fau-De-E Ef-En-En" |
| G S20.7 edge Latin | M | G's "وحده" (alone) is not in DE and was not adopted |
| G glossary Redispatch / EnWG term | M | "der Redispatch" and "قانون الطاقة" (S11.5) applied; AR Redispatch term kept per TERMS (see F S12.6) |
| G glossary MaStR / commissioning | A | MaStR term was already uniform; "التشغيل الأولي" in S14.3 and S15.6 |
| G EN he/his (grid operator) | A | S9.5, 9.7, 9.8, 9.9, 19.2 neutral ("it"); S13.3-13.5 "the operator" |
| G quiz Q4 AR | A | "ما المقصود بعلاوة السوق من حيث المبدأ؟" |
| G quiz Q5 option 2 DE | A | "Sich auf Zahlen aus Videos verlassen." |
| G S8.6 محاورك | A | "جهة الاتصال الأولى لكم" |
| G S9.x الربط -> التوصيل | A | S9.2, 9.3, 9.9, 8.9, 21.3 |
| G S9.10 Betreiber ambiguous | A | "Anlagenbetreiber" / "مشغّل المنشأة" / "plant operator" |
| G S12.6 inconsistent term | M | See F S12.6 |
| G S13.5 edge Latin | M | G's fix kept "(Marktprämie)" at the edge; replaced by "ما يسمى بالألمانية Marktprämie، أي علاوة السوق" |
| G S13.8 Eigenverbrauch sentence | R | Adding it would be a new unsupported claim; the row was deleted instead (F S13) |
| G S14.7 awkward AR | A | Applied |
| G S17.2 tts commas | A | "Fau-De-E A-Er-En vier-eins-null-fünf" |
| G S21.7 AR "بصورة حديثة" | M | "في المصادر الحالية" |
| G title AR extra terms | M | Edge rule: «... وقانون EEG الألماني» (G's wording would end in Latin) |
| G S10.5 Zumutbarkeit | A | "المعقولية الاقتصادية" |
| G S13.10 angemeldet | M | DE now "angemeldet und registriert" (both supported in research), AR "مسجَّلة لدى مشغّل الشبكة وفي السجل" |
| G S17.2 filler المعروفة | A | Removed (word order from G) |

Further changes of my own (TERMS.md, quote slides, validator):
- Quote slides S2, S11, S22 became bullets slides with 3-4 real items from the same scene.
- S12.5 "القدرة الفعالة" (Wirkleistung), S6.7 "محوّلًا كهربائيًا" (Transformator), S16.1/S16.8/quiz Q3 "التسجيل لدى مشغّل الشبكة" (Anmeldung).
- `stand` extended (softened claims); research file: two facts softened, five items added to `dropped`.
- tools/validate.py: 0 issues. Next pointer already correct (E-A04: storage, inverters, charging).

Primary-source check needed: scope of the EEG § 9 equipment duty (size/commissioning date, paragraph number), whether the MaStR duty covers all Erzeugungsanlagen, whether fines for late registration exist (MaStRV/EnWG), "Redispatch 2.0" legal basis.
