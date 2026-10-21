# Applied audit findings: E-C05 (scripts/E/05-ot-security.json)

Legend: A = applied, M = modified (corrected variant), R = rejected. S = scene, L = line. "F" = facts finding, "G" = language finding. Script: /tmp/claude-0/apply-E-C05/apply.py.

| Finding | Result | Reason |
|---|---|---|
| F S19.7/2/4 date TTS grammar | A | zwanzigste / fünften / sechsten, also AR dates exact |
| F S9.1 "drei Rollen" | A | "unter anderem diese drei Rollen" DE/AR/EN |
| F S8.0 "Vier Gruppen von Teilen" | M | Scene rewritten from research facts only (Teile 2-1, 2-4, 3-2, 3-3, 4-1, 4-2 by role/topic); four-group claim moved to dropped |
| F S6.6 Schutzversprechen | A | "kann ... noch bremsen" |
| F S11.7 more zones | A | "können mehr Schutz bringen" |
| F S21.0 / S3.6 Verfügbarkeit zuerst | A | "oft vorn" on summary slide; S3.6 "oft hohe Priorität, neben der Sicherheit" |
| F S3.0 table Updates/Lebensdauer | M | Updates row "meist geplant"; Lebensdauer row and line 3.8 removed (unsupported) |
| F S15.1 Einfallstor/Protokollierung | A | "mögliches Einfallstor"; line 15.6 deleted; 15.8 no longer claims every access is documented |
| F S17.0 typische Fehler | M | Kicker/heading/line 17.1 "mögliche Schwächen" (with G S17.1); 17.6 "können helfen" |
| F S5.7 Büronetz/alte Systeme | A | "kann reichen"; slide item "oft ohne Updates" |
| F S4.1 classic goals | M | Labelled "klassische Schutzziele der IT-Sicherheit"; no new fact added; needs primary-source check (BSI/ISO 27000) |
| F S8.3 misplaced line | A | Moved behind the part lines in the rewritten scene |
| F S10.5 contract regulation | A | "sollten klar geregelt sein" |
| F S10.1 "nur, wenn" | A | Absolute removed |
| F S16.8 role split | A | Line deleted |
| F S12.0 SPS term | M | Term removed from slide (not spoken, G S12 too); TERMS.md term would be المتحكم المنطقي القابل للبرمجة if reintroduced |
| F S20.6 IEC 62443 vs NIS2 | A | "Manche Betriebe ziehen ... als fachliche Orientierung heran" |
| G S0 glossary lists/Latin | A | Converted to {de,ar,en}; Latin removed from AR; added Defense in Depth, Schutzniveau, BSI, Härtung |
| G S0 quiz Latin edges | A | Q1 and Q5 AR reworded, no Latin edges |
| G S19.2 / 19.4 / 19.7 TTS dates | A | Same as F S19 |
| G S18.4 TTS NIS | A | En-I-Es |
| G S4.9 السلامة الوظيفية | A | الأمان الوظيفي |
| G S9.2 المحوّلات الشبكية | A | المبدّلات الشبكية (TERMS: المبدّل الشبكي) |
| G S17.1 "Zum Schluss" duplicate | M | "Jetzt einige mögliche Schwächen" (softened as in F S17) |
| G S0 quiz DE grammar/Q1 distractors | A | "vom VDE", Q1 rewritten; answers reordered to 0,1,2,0,1 |
| G S4.5 BSI explained | A | Spelled out at first use (DE/AR/EN/tts) |
| G S12.0 SPS term | A | Removed |
| G S2.0 Stand der Technik term | A | Moved to S20; AR المستوى الراهن للتقنية, also 20.4 |
| G S22.1 grammar | A | "ein wichtiger Hinweis" |
| G S2.5 Rechtsbereich | A | Rechtsabteilung |
| G S6.9 AR grammar/order | A | Reworded, moved before 6.8 |
| G S11.2 AR | A | احتياجات الحماية المتشابهة |
| G S13.4 order | A | Moved behind 13.6 |
| G S7.5 order | A | Moved behind 7.9 |
| G S17.3 / 17.4 AR | A | التشغيل الأولي; منافذ وصول |
| G S21.5 grammar | A | "brauchen einen Plan" |
| G S11.0 terms Latin parentheses | A | Stripped from all slide terms AR (all scenes) |
| G S3/S7/S12/S19 table rows >50 | A | All table rows <=50 |
| G S1.0 title slide items | A | 3 items |
| G S1.1 "in diesem Pfad" | A | Reworded DE/AR/EN |
| G S4.4, S20.7, S21.1 British EN | A | authorised, organisation, summarise ("defense in depth" kept as the term) |
| G S1.3, 3.2, 3.3, 7.1, 7.3, 8.7, 12.4, 15.2, 18.1-4, 18.7, 19.2, 19.4-7, 19.9, 20.5 AR | A | Suggested rewrites; final full stops added to every AR line |
| TERMS (own check) | A | المستشعرات; وسائل حماية (Schutzeinrichtung); next pointer kept (EMV, normal Arabic sentence); S16.3/16.4 softened to "oft/meist" per research fact |
| G S3.3 suggested "الحسّاسات" | M | TERMS.md term المستشعرات used |
| G S12.0 suggested SPS AR "وحدة التحكم المبرمجة" (F S12.0) | R | Term deleted; TERMS.md is binding (المتحكم المنطقي القابل للبرمجة) |

Rejected: only the two SPS-wording suggestions above (no SPS term remains on the slide). Research file: three entries added to "dropped"; script `stand` extended.
Needs primary-source check: classic protection goals and danger-to-people statements (S3/S4, general knowledge, not in research), Teil 2-4 role wording, NIS2UmsuCG/BSIG current status.
