# آزمایشگاه متن (text_lab)

برنامه‌ی `text_lab.py` یک جمله را می‌گیرد و چند آمار از آن درمی‌آورد:
کاراکتر (با و بدون فاصله)، کلمه، حروف بزرگ، برعکس، تعداد `a`، Slug،
اولین و آخرین کلمه و وجود `python`.

اجرا:

```bash
uv run python text_lab.py
```

## مشاهدات

- اول `strip()` فاصله‌های اول و آخر را پاک می‌کند، برای همین همه‌ی آمارها روی متن تمیز حساب می‌شوند.
- `split()` بدون ورودی چند فاصله‌ی پشت‌سرهم را مثل یکی حساب می‌کند، برای همین Slug فقط یک `_` بین کلمه‌ها دارد.
- برای جمله‌ی انگلیسی همه‌ی آمارها درست حساب شدند.
- برنامه با جمله‌ی فارسی Crash نکرد.
- `upper()` روی فارسی تغییری نداد، چون فارسی حرف بزرگ و کوچک ندارد.
- `count('a')` روی فارسی `0` شد و `'python' in text` شد `False`، چون متن فارسی است.
- `[::-1]` رشته‌ی فارسی را حرف‌به‌حرف برعکس کرد.

## خروجی واقعی

```
--- English ---
Characters (with spaces): 36
Characters (no spaces): 30
Words: 7
Upper: PYTHON IS THE LANGUAGE OF AGENTIC AI
Reversed: IA citnegA fo egaugnaL eht si nohtyP
Count of 'a': 4
Slug: python_is_the_language_of_agentic_ai
First word: Python
Last word: AI
Has 'python': True

--- Persian ---
Characters (with spaces): 30
Characters (no spaces): 25
Words: 6
Upper: سلام دنیا من پایتون یاد میگیرم
Reversed: مریگیم دای نوتیاپ نم ایند مالس
Count of 'a': 0
Slug: سلام_دنیا_من_پایتون_یاد_میگیرم
First word: سلام
Last word: میگیرم
Has 'python': False
