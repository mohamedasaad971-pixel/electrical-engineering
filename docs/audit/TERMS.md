# Verbindliche Terminologie E-F01..07 (DE → AR) und TTS-Regeln

Alle Skripte müssen diese Wahl verwenden. Arabische Zeilen dürfen nicht mit lateinischen Buchstaben/Ziffern beginnen oder enden (Kennung in Klammern in die Mitte setzen oder Satz umstellen).

| DE | AR |
|---|---|
| Elektrofachkraft | الكهربائي المؤهَّل (Elektrofachkraft) – nie «فني» |
| EFKffT | الكهربائي المؤهَّل لأعمال محددة |
| Elektrotechnisch unterwiesene Person | شخص مُلقَّن كهروتقنيًا |
| Laie | شخص غير مؤهَّل |
| Haftung | المسؤولية القانونية |
| Gewährleistung | الضمان |
| Auftraggeber | الجهة المُشغِّلة للمشروع (صاحب المشروع) |
| Unternehmer (Arbeitsschutz) | صاحب المنشأة |
| Auftragnehmer | المقاول |
| Sicherung | المنصهر |
| Leitungsschutzschalter | القاطع الآلي |
| Stromkreis | دارة كهربائية |
| Schaltschrank | خزانة التوزيع والتحكم |
| Netzanschluss | التوصيل بالشبكة |
| Netzbetreiber | مشغّل الشبكة |
| Unterweisung | التوجيه والتعليمات (Unterweisung) |
| Prüfprotokoll | محضر الفحص |
| Schaltplan | مخطط الدارات |
| Normen | المعايير |
| Vorschrift | لائحة |
| DGUV Vorschrift 3 | لائحة الوقاية من الحوادث رقم ٣ (DGUV V3) – Kennung nie am Satzrand |

TTS: Abkürzungen als Buchstabennamen: DIN «Din», VDE «Fau-De-E», IEC «I-E-Ze» (nicht I-E-Zett), EN «E-En», ISO «I-So», DGUV «De-Ge-U-Fau», DKE «De-Ka-E», EnWG «E-En-We-Ge», ProdSG «Prod-Es-Ge», CE «Ze-E», HwO «Ha-We-O», NAV «En-A-Fau», DVGW «De-Fau-Ge-We». Zahlen ausgeschrieben, tts muss denselben Inhalt/dieselbe Reihenfolge wie die de-Zeile haben.

Nächstes-Video-Kette: E-F01→E-F02→E-F03→E-F04→E-F05→E-F06→E-F07→E-A01 (Energienetze).

## Ergänzung (Pfad E-A, verbindlich)
| DE | AR |
|---|---|
| Wechselrichter | العاكس (المحوّل الشمسي إلى تيار متناوب) – nie «المحوّل» |
| Transformator | المحوّل (الكهربائي) |
| Marktstammdatenregister (MaStR) | السجل الرئيسي لبيانات سوق الطاقة |
| Schütz | الكونتاكتور (nicht «الملامس») |
| Neutralleiter | موصل التعادل |
| Schutzleiter | موصل الحماية |
| Blindleistung | القدرة غير الفعالة |
| Wirkleistung | القدرة الفعالة |
| Scheinleistung | القدرة الظاهرية |
| Impedanz | المعاوقة |
| Redispatch | إعادة جدولة التوليد (Redispatch) |
| Anschluss (ans Netz) | التوصيل بالشبكة |
| Anmeldung beim Netzbetreiber | التسجيل لدى مشغّل الشبكة |
| Kondensatorbatterie | بنك مكثفات |
| Übertragungsnetzbetreiber (ÜNB) | مشغّل شبكة النقل |
| Verteilnetzbetreiber (VNB) | مشغّل شبكة التوزيع |
| Anschlussnehmer | صاحب الاتصال بالشبكة (المنتفع بالتوصيل) |
| Regelung | التنظيم/الضبط (nicht «المراقبة») |

Regeln: Das deutsche Feld `de` enthält die geschriebene Abkürzung (z. B. «VDE-AR-N 4105»), die Buchstabierung steht nur im Feld `tts`. Kein Zitat-Slide (quote) mit nur einer Zeile; Tabellenzeilen ≤ 50 Zeichen. Freischalten ist nur der erste von fünf Schritten: jede Aussage zu Arbeitsschritten verweist auf die fünf Sicherheitsregeln (E-F05) und enthält keine verkürzte Reihenfolge. Validator: tools/validate.py prüft jetzt auch Satzzeichen am Rand.

## Ergänzung (Pfad E-B, verbindlich)
| DE | AR |
|---|---|
| Potentialausgleich | الربط المتساوي الجهد |
| Schutzpotentialausgleich | الربط الوقائي المتساوي الجهد |
| Kabel | كابل (nicht «كبل») |
| Freischalten (Regel 1) | فصل الجهد (wie E-F05) |
| gegen Wiederinbetriebnahme sichern (Regel 2) | تأمينها ضد إعادة التشغيل |
| allpolig (Regel 3) | «كل الأقطاب» – Regel 3 immer mit «allpolig» |
| Abdecken/Abschranken (Regel 5) | إحاطتها بحواجز (wie E-F05) |
| Notbeleuchtung/Sicherheitsbeleuchtung | إضاءة الطوارئ |
| Funktionserhalt | استمرار الوظيفة (Funktionserhalt) |
| HLS (Heizung, Lüftung, Sanitär) | التدفئة والتهوية والصرف الصحي |
| Leistungsphase (HOAI) | مرحلة خدمة (wie im Zivilkurs) |
| Kurzschluss | القصر الكهربائي |
| RCD (tts) | Er-Ze-De |
| Blitzschutzzone 0A (tts) | Null A, nie «صفر ألف» |

Regeln für Aussagen zur Arbeitsberechtigung: nie «nur eine Elektrofachkraft darf …» absolut; immer «Elektrofachkraft oder unter Leitung und Aufsicht einer Elektrofachkraft» im Sinn von E-F04/DGUV V3. Die fünf Sicherheitsregeln immer vollständig (mit «allpolig»).

## Ergänzung (Pfad E-C, verbindlich)
| DE | AR |
|---|---|
| SPS (speicherprogrammierbare Steuerung) | المتحكم المنطقي القابل للبرمجة |
| Sensor | المستشعر |
| Aktor | المُنفِّذ |
| Funktionale Sicherheit | الأمان الوظيفي (nicht «السلامة الوظيفية») |
| Sicherheitsfunktion | وظيفة الأمان |
| Not-Halt | إيقاف الطوارئ |
| Not-Aus | فصل الطوارئ |
| Schutzeinrichtung | وسيلة حماية |
| Netzwerk-Switch | المبدّل الشبكي (nie «المحوّل») |
| IT-/OT-Sicherheit (Cybersecurity) | الأمن السيبراني (Sicherheit im Sinn von security) |
| Maschinensicherheit (safety) | أمان الآلات |
| Maschinenverordnung | لائحة الآلات الأوروبية |
| Risikobeurteilung | تقييم المخاطر |
| Prozessabbild der Eingänge / Ausgänge | صورة المدخلات / صورة المخرجات (PAE / PAA) |
| EMV | التوافق الكهرومغناطيسي (EMC) |

Strukturregeln: `glossary` ist ein Array von Objekten {de, ar, en} (nie Tripel-Arrays). Datums-tts grammatisch korrekt (z. B. «am sechsten Dezember», «am zwanzigsten Januar»). Exakte Rechtsdaten im Arabischen ohne «تقريبًا». Titel, `next`, Glossar- und Quiz-Einträge ohne Latein/Ziffer am arabischen Rand; Bezeichner in die Mitte oder mit arabischem Wort abschließen.

## Ergänzung (Pfad E-D, verbindlich)
| DE | AR |
|---|---|
| Kurzschließen (Sicherheitsregel 4: Erden und Kurzschließen) | التأريض والتقصير (التقصير = Kurzschließen der Leiter) |
| Kurzschluss (Fehlerfall) | القصر الكهربائي |
| Besteller / Auftraggeber | الجهة الطالبة للعمل (صاحب المشروع) |
| Schnittstelle | الواجهة التنسيقية |
| Schacht / Schächte | مجرى / مجاري التمديدات (nie «المناور») |
| Elektrofachkraft (EN) | qualified electrician (nie «electrically skilled person») |
| RCD (AR) | قاطع التيار المتبقي (RCD) – im Satzinneren, wie E-B02 |
| Rufbereitschaft | الجاهزية عند الطلب (Aufenthaltsort frei, aber einsatzbereit) |

Regeln: Arabische Quizfragen/-optionen, Folienbegriffe und Glossar enden nicht mit lateinischen Buchstaben; die deutsche Klammer gehört in die Mitte oder entfällt. Sicherheitsregeln auf Folien immer vollständig (nie «5 Abdecken»). Rechtsfolgen von Abnahme/Gewährleistung: «ergeben sich aus dem Gesetz (BGB) und/oder VOB/B, falls vereinbart, sowie dem Vertrag», nie «regelt der Vertrag» allein.

## Ergänzung (Softwareserie S, verbindlich)
| DE | AR / Regel |
|---|---|
| CAD (tts) | Ze-A-De (in allen Skripten gleich) |
| GmbH (tts) | Ge-Em-Be-Ha |
| Freeware / kostenlos | «مجاني (حسب الشركة المصنّعة)» – nie «مفتوح المصدر» für Freeware wie LTspice; «مفتوح المصدر» nur für belegte Open-Source-Lizenz (z. B. pandapower, OpenPLC-Runtime) |
| Beleuchtungsplanung / Lichtplanung | تخطيط الإضاءة (ein Begriff in allen Titeln und next-Zeilen) |
| Notbeleuchtung | إضاءة الطوارئ (nie «إضاءة الأمان») |
| Elektrofachkraft (EN) | qualified electrician |
| Schütz | الكونتاكتور (maskulin im Arabischen: هذا الكونتاكتور; deutsch: das Schütz) |

Regeln: Videos werden mit Titel genannt, nie mit internen IDs («S-05», «E-C01») im gesprochenen Text oder in tts. `next` nennt den tatsächlichen Titel des nächsten Videos (Reihenfolge S-01 EPLAN → S-02 SPS-Umgebungen → S-03 Netzberechnung → S-04 Simulation → S-05 Lichtplanung → S-06 CAD für Steuerungsplanung → Serienende). Keine Werbe-/Wertungsaussagen («teuer», «bekanntes Beispiel in Deutschland»). Rechtsaussagen zu Technischen Regeln: «Vermutungswirkung»/«in der Regel», nie «wer die Regel einhält, erfüllt die Verordnung». LTspice, DIALux, OpenPLC usw. nur mit belegten Lizenz-/Einschränkungsangaben aus der Recherche. IEC 61131-3: aktueller Stand wie in der SPS-Grundlagen-Folge (Ausgabe 2025 ohne AWL, nach Quellenlage), 2013 nur als historischer Stand.
