# Applied audit findings: E-C06 (scripts/E/06-emv-messtechnik.json)

Legend: A = applied, M = modified (corrected variant), R = rejected. S = scene, L = line (original numbering). F = facts finding, G = language finding.

| Finding | Result | Reason |
|---|---|---|
| F S4.7/4.8 frequency assignment capacitive/inductive | A | Both lines deleted (not in research, technically doubtful) |
| F S2.6 "immer die fünf Sicherheitsregeln" | M | Reworded: rules apply to de-energised installations, measuring under voltage is a special case; slide item adjusted |
| F S17.9 mains voltage + five rules | M | Manufacturer's instructions and company rules; work by Elektrofachkraft or under her direction and supervision (TERMS), not "only" |
| F S13.10 / G S13.10 absolute Elektrofachkraft | A | DE now "oder von Personen unter deren Leitung und Aufsicht"; AR/EN aligned |
| F S13.8 five-conductor TN-S | A | Deleted; moved to dropped |
| F S9.2 "harmonisierte Normen" | A | Removed from line, tts and slide item ("EMV-Normen") |
| F S8.9 / G S8.9 documentation duty | M | Phrased as a recommendation ("Dokumentieren Sie, nach welchen Regeln ...") |
| F S12.1 shield and magnetic fields | A | Electric fields only; "kann"; S10 item and S10.3 aligned |
| F S9.7/9.8 planner/operator | A | Deleted; moved to dropped |
| F S18.5 / G S18.5 resistance vs impedance | A | "Impedanz der Strombahn"; AR المعاوقة |
| F S5 slide row leitungsgebunden | M | Row "Drei Kopplungsarten \| oft leitungsgebunden gezählt" (50 chars) |
| F S6.8 / G S6.3 order and referent | A | Moved to follow 6.5, named "Die Prüfpegel" |
| F S11.7/11.9 cost, planning | A | Deleted |
| F S15 slide device vs tester | A | Row "Installationstester \| Schleifenimpedanz u. a." |
| F S19.9 certificate contains uncertainty | A | Deleted |
| F S17.5 antenna reason | M | Replaced by "Die Masseleitung des Tastkopfs hält man möglichst kurz"; 17.6 deleted |
| F S7.4 EMVG title / Betriebsmittel | M | Neither is a research fact: title line 7.4 and definition line 7.7 deleted, moved to dropped (not added as new fact) |
| F S2.4 + others AR Leitung/Aufsicht | A | "إدارته وإشرافه" in S2, S13, S17, S18, S21, Q5 |
| G next (Latin edge, wording) | A | next DE/AR/EN to E-D01 title; S22.7 synchronised |
| G Quiz Q1 option 3 Latin edge | A | المتأثر بالاضطراب |
| G Glossary capitalisation + additions | A | "elektromagnetische"; added Fachgrundnorm, Schirm, Rückführbarkeit, Elektrofachkraft |
| G S15.5 مختبر التركيبات | A | جهاز اختبار التركيبات |
| G S16.2 CAT spelled in de | A | de written, tts spelled, digits one by one |
| G S17.7 AR agreement | A | يناسب عرض الحزمة الترددية |
| G S19.5 tts / الدولي | A | tts digit by digit; AR "الخاص بالمختبرات" |
| G Quiz distractors, Q3 AR, answers | A | New distractors, Q3 grammar, answers varied (2,0,1,2,0), one correct each |
| G terms AR Latin tag (S3,5,6,7,8,9,12,13,15,16,17) | A | Latin tags removed from terms |
| G S9 Fachgrundnorm term, S9.3 | A | المعيار العام للمجال / المعايير العامة للمجال; slide item "Wohn- und Industriebereich" |
| G S15/S18 table rows 52/51 chars | A | "Isolationsmessgerät \| Gleichspannung, vom Netz", "Isolationsmessung \| Gleichspannung, vom Netz" |
| G S2 term Messprotokoll | A | terms emptied |
| G S1.6 order | A | Housekeeping line moved last |
| G S1.1 "im Pfad" | A | "sechsten und letzten Video über Automatisierung und Steuerung" |
| G S2.8 referent | A | Moved after 2.6, "Die fünf Regeln ..." |
| G S5.2 AR tautology | A | الاضطرابات الموصولة تنتقل ... |
| G S5.3 pedagogical inconsistency | M | Suggested "meist zwischen benachbarten Leitungen" is not in research; replaced by "auch wenn bei den letzten beiden Felder wirken" |
| G S6.3 AR term | A | النبضات العابرة السريعة |
| G S6.2 tts, S16.2 tts, S9.2 tts | A | Digit by digit |
| G S7.5 AR digits | A | Western digits, ميلاديًا kept |
| G S7.6 tts URL | A | "gesetze-im-internet Punkt De" |
| G S8.7 Behörde | A | Bundesnetzagentur named |
| G S13.9 AR "يُقال" | A | تسري القاعدة |
| G S16.3 AR | A | Reworded |
| G S17.5 AR "كابل الأرضي" | M | "سلك الأرضي" in the shortened line |
| G S17.9 | M | See F S17.9 (keeps "oder unter Leitung und Aufsicht") |
| G S18.9 | A | Full sentence, "oder von Personen unter deren Leitung und Aufsicht" |
| G S19.4 Normale | A | AR/EN "measurement standards" |
| G S21.8 | A | Full sentence with five safety rules |
| G S21 recap legal part | A | Line inserted after 21.4 (tts E-Em-Fau-Ge) |
| G S4.7 note | A | Via deletion (F S4.7) |
| G S15.7 اقرؤوا, S21.1 لنلخّص | A | Spelling |
| G S2.4 note | A | See F S2.4 |

Rejected: none.

Research file: 11 entries added to "dropped"; script `stand` extended. Concerns for primary-source check: classification of capacitive/inductive coupling as conducted; CAT III/IV rule of thumb (medium confidence); EMVG/Directive current version; EN 61000-6 and DIN VDE 0100-444/-600 editions.
