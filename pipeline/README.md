# خط إنتاج الفيديو

يبني فيديو (شرائح فاتحة 1920×1080 + صوت ElevenLabs + ترجمة محروقة عربي فوق إنجليزي) من سكربت JSON.

## التشغيل على GitHub Actions
1. عدّل `pipeline/run.json` وادفعه (أو شغّل `build-video` يدويًا):
   `{"action":"build","video":["scripts/E/01-berufsbilder.json"],"synthesize":true,"burn":true,"rev":1}`
   حتى 4 فيديوهات في المصفوفة (تُبنى بالتوازي).
2. أضف السر `ELEVENLABS_API_KEY` في Settings > Secrets (يضيفه المالك فقط). الصوت: `Eleonore`، النموذج `eleven_multilingual_v2`.
3. اختياري: المتغير `RELEASE_UPLOAD=true` (Settings > Variables) يرفع الملفات إلى إصدار مسودة `build-<ID>-rev<N>`.

## تشغيل محلي بلا مفتاح (اختبار)
`python pipeline/build.py --script scripts/E/01-berufsbilder.json --no-synthesize --silent`
(صمت بمدة مقدّرة = عدد الكلمات / 2.3 في الثانية). يلزم ffmpeg وplaywright chromium وخطوط Noto.

## المخرجات `out/<ID>/`
`<ID>.mp4`، `<ID>.ar.srt`، `<ID>.en.srt`، `<ID>.de.srt`، `contact-sheet.png`، `qa.json`
(المدة، LUFS، سطور ترجمة فوق 20 حرفًا/ث، مشاكل الفيض في الشرائح). الملفات المؤقتة في `work/` (تخزين الصوت مؤقتًا بالتجزئة). كلاهما خارج Git.

## الحدود
- الزمن: 0.35 ث بين الأسطر و0.8 ث بين المشاهد؛ الجهارة -16 LUFS (تُقاس فقط مع صوت حقيقي).
- منطقة الشريحة الآمنة تنتهي عند y=740 (تحتها الترجمة)؛ أي تجاوز يظهر في `overflow_issues`.
- التخطيطات: title, bullets, cards, table, quote, summary. حدود العدد في `docs/PLAN.md`.
- مصطلحات ≤3 للمشهد؛ الشعار `assets/logo-cropped.png` أعلى اليمين.
- بلا مفتاح ومن دون `--silent` يفشل البناء عمدًا؛ الأخطاء المؤقتة لـ ElevenLabs تُعاد 5 مرات.
