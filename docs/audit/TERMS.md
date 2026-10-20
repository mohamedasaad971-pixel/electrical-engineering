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
