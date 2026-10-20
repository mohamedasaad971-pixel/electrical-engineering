# خط إنتاج الفيديو

منقول من خط الدورة المدنية (`build_video.py`): شرائح HTML متحركة تُصوَّر في Chromium، صوت ElevenLabs (Eleonore، سرعة 0.92)، ترجمة عربي فوق إنجليزي داخل شريط فاتح سفلي، انتقال ثلاثي الألوان بين المشاهد، وظهور تدريجي للعناصر مع الجملة المنطوقة. الوصف التصميمي في `pipeline/STYLE.md`.

## التشغيل على GitHub Actions
عدّل `pipeline/run.json` وادفعه: `{"action":"build","video":["scripts/E/01-berufsbilder.json"],"synthesize":true,"burn":true,"rev":1}` (حتى 4 فيديوهات، كل فيديو مهمة مستقلة بمتغير `VIDEO_INDEX`). `synthesize:false` = تجربة صامتة (علامة DRY RUN). السر `ELEVENLABS_API_KEY` يضيفه المالك فقط. الإعدادات في `pipeline/config.json`.

## تشغيل محلي صامت
`python pipeline/build_video.py --script scripts/E/01-berufsbilder.json --no-synthesize --burn` (يلزم ffmpeg وplaywright chromium وخطوط Noto؛ نحو 15 دقيقة لفيديو 15 دقيقة).

## المخرجات `out/<ID>/` (Artifact باسم `<ID>-rev<N>`)
`<ID>.ar-en.mp4` (مع الترجمة) و`<ID>.clean.mp4` (بلا ترجمة)، `subtitles/<ID>.{ar,en,de}.{srt,vtt}`، `contact-sheet.png`، لقطات فحص (`frame*.png`, `motion*.png`, `bidi*.png`, `intro*.png`, `finals/`)، `report.json` (المدة، الترجمة، مشاكل DOM، تحذيرات)، و`audio_check.json` للبناء الحقيقي.
المشاهد بلا `id/name` تأخذ تلقائيًا الرقم والعنوان؛ التخطيطات: title/quote ← hook، bullets، summary ← recap، cards، table (الأسطر `مفتاح: قيمة`). حدود العدد في `docs/PLAN.md`.
