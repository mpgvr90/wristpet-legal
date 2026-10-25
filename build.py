"""Builds the WRISTPET legal pages (EN at the root, UK under uk/).

Run: python build.py
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).parent
OWNER = "Tetiana Lahotska"
EMAIL = "codexxdev77@gmail.com"
UPDATED = {"en": "25 October 2026", "uk": "25 жовтня 2026"}
MAIL = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
APPLE_EULA = "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"

CSS = """
:root { --bg:#f3faf6; --card:#ffffff; --text:#10261e; --muted:#53695f; --accent:#23795a; --line:#d5e9de; }
@media (prefers-color-scheme: dark) { :root { --bg:#0b1a16; --card:#132a23; --text:#eef8f3; --muted:#a3bcb1; --accent:#85c9ab; --line:#21443a; } }
* { box-sizing:border-box; }
body { margin:0; background:var(--bg); color:var(--text); font:16px/1.6 -apple-system, "Segoe UI", Roboto, sans-serif; }
main { max-width:760px; margin:0 auto; padding:32px 16px 64px; }
header { display:flex; justify-content:space-between; align-items:center; gap:12px; flex-wrap:wrap; margin-bottom:24px; }
.brand { font-weight:800; font-size:22px; letter-spacing:3px; color:var(--accent); text-decoration:none; }
nav a { color:var(--accent); margin-left:12px; }
h1 { font-size:32px; margin:8px 0 4px; }
h2 { font-size:19px; margin:24px 0 8px; }
.updated { color:var(--muted); margin:0 0 20px; }
section { background:var(--card); border:1px solid var(--line); border-radius:16px; padding:4px 20px 16px; margin:14px 0; }
ul, ol { padding-left:20px; }
a { color:var(--accent); }
footer { color:var(--muted); font-size:14px; margin-top:32px; }
""".strip()

T = {
    "en": {
        "privacy": "Privacy Policy",
        "terms": "Terms of Use",
        "delete": "Delete your data",
        "updated": "Last updated",
        "other": ("Українська", "uk"),
        "tagline": "WRISTPET is a calm walking companion for Apple Watch and iPhone: a little creature that grows with your steps.",
        "footer": f"WRISTPET · {OWNER} · {MAIL}",
    },
    "uk": {
        "privacy": "Політика конфіденційності",
        "terms": "Умови використання",
        "delete": "Видалення даних",
        "updated": "Оновлено",
        "other": ("English", "en"),
        "tagline": "WRISTPET - спокійний супутник для прогулянок на Apple Watch та iPhone: маленька істота, що зростає разом із вашими кроками.",
        "footer": f"WRISTPET · {OWNER} · {MAIL}",
    },
}

PRIVACY = {
    "en": [
        ("Who we are", f"""
<p>WRISTPET is a walking companion for Apple Watch and iPhone. It is published by {OWNER} ("we", "us"). Contact: {MAIL}.</p>
<p>This policy explains what data the app handles, where it stays and what choices you have.</p>"""),
        ("In short", """
<ul>
<li>Everything the app uses stays on your iPhone and Apple Watch. We never receive it.</li>
<li>There is no account, no registration and no server of ours. The app makes no network requests of its own.</li>
<li>Apple Health data is read only with your permission, is never written back, and is never used for advertising or shared with anyone.</li>
<li>WRISTPET is a one-time paid download from the App Store. There are no subscriptions and no in-app purchases.</li>
<li>No advertising, no analytics, no tracking. We do not sell data.</li>
</ul>"""),
        ("Apple Health", """
<p>With your permission, WRISTPET reads from Apple Health:</p>
<ul>
<li>today's step count and number of workouts;</li>
<li>daily step totals for the previous 14 complete days, at most once a day, for the weekly rhythm and an optional goal suggestion.</li>
</ul>
<p>When new steps are recorded, the app may also read today's total in the background, about once an hour at most, so your watch face and widgets stay current without opening the app.</p>
<p>WRISTPET reads only daily totals, not individual samples, heart rate or location, and it does not write anything to Apple Health. If you do not grant access, you can still care for your companion; automatic step progress is simply unavailable. The optional walk timer never adds steps.</p>"""),
        ("Data stored only on your devices", """
<p>The app stores on your devices: your companion and its progress, goals, care moments, settings, walk memories (date, duration, an optional feeling and the walk idea), story postcards and up to 35 days of daily step totals.</p>
<p>Widgets and watch complications read this data on the same device. If you use both an iPhone and an Apple Watch, the two devices exchange it directly through Apple's WatchConnectivity; it does not pass through any server of ours.</p>
<p>Story "routes" are imagined. The app does not use your location.</p>"""),
        ("Notifications", """
<p>If you allow notifications, the app schedules one local notification on your device when a walk timer ends. Permission is asked the first time you start a walk. The notification is created on the device and is not sent through any server.</p>"""),
        ("Payment: the App Store", """
<p>WRISTPET is bought once through the Apple App Store under Apple's terms and privacy policy. We never receive your card details, your name or your Apple Account email; we only see the aggregated sales reports Apple provides to developers.</p>"""),
        ("Permissions", """
<ul>
<li><strong>Apple Health</strong> - read-only access to steps and workouts, requested when you tap "Enable step access".</li>
<li><strong>Notifications</strong> - for the end of a walk, requested when you start your first walk.</li>
</ul>
<p>The app does not use location, contacts, camera, microphone or photos.</p>"""),
        ("Why we process data (legal bases)", """
<p>Where the EU or UK GDPR applies: we do not collect or receive personal data. The data described above is processed by the app on your own devices, at your request, to provide the features you use.</p>"""),
        ("Retention", """
<p>Data stays on your devices until you use <em>Settings › Start fresh</em> or delete the app. Start fresh on one device also clears the progress on your paired iPhone or Apple Watch the next time they exchange data. Deleting the app removes only the copy on that device. If you back up your iPhone with iCloud or a computer, Apple's backup may include the app's data according to your backup settings.</p>"""),
        ("Your choices and rights", f"""
<ul>
<li>Erase your progress with <em>Settings › Start fresh</em>; deleting the app also removes its data from that device.</li>
<li>Change or revoke Apple Health access at any time in the Health app or in your device's Settings. Revoking access stops new readings; to remove progress already stored, use Start fresh.</li>
<li>Turn notifications off in your device's Settings.</li>
<li>Depending on where you live, you may have rights to access, correct or delete personal data and to complain to a data protection authority. Because we hold no data about you, there is nothing for us to export or delete, but you can write to {MAIL} with any question. See also <a href="delete-data.html">Delete your data</a>.</li>
</ul>"""),
        ("Children", """
<p>WRISTPET is suitable for all ages. We do not collect personal information from anyone, including children under 13.</p>"""),
        ("Changes", """
<p>If this policy changes materially, for example if a future version adds purchases, sync or any outside service, we will update this page before that version is released and mention it in the update notes.</p>"""),
        ("Contact", f"""
<p>Privacy questions: {MAIL}.</p>"""),
    ],
    "uk": [
        ("Хто ми", f"""
<p>WRISTPET - супутник для прогулянок на Apple Watch та iPhone. Видавець - {OWNER} («ми»). Контакт: {MAIL}.</p>
<p>Ця політика пояснює, які дані використовує застосунок, де вони зберігаються і що ви можете з ними зробити.</p>"""),
        ("Коротко", """
<ul>
<li>Усе, що використовує застосунок, залишається на вашому iPhone та Apple Watch. Ми цих даних не отримуємо.</li>
<li>Немає облікового запису, реєстрації та наших серверів. Застосунок сам не виконує мережевих запитів.</li>
<li>Дані Apple Health читаються лише з вашого дозволу, ніколи не записуються назад, не використовуються для реклами й нікому не передаються.</li>
<li>WRISTPET - платний застосунок з разовою оплатою в App Store. Підписок і вбудованих покупок немає.</li>
<li>Без реклами, аналітики й трекінгу. Ми не продаємо дані.</li>
</ul>"""),
        ("Apple Health", """
<p>З вашого дозволу WRISTPET читає з Apple Health:</p>
<ul>
<li>кількість кроків і тренувань за сьогодні;</li>
<li>денні підсумки кроків за попередні 14 повних днів, не частіше одного разу на день, для тижневого ритму та необов'язкової підказки щодо цілі.</li>
</ul>
<p>Коли записуються нові кроки, застосунок може також читати сьогоднішній підсумок у фоні, не частіше приблизно одного разу на годину, щоб циферблат і віджети були актуальними без відкриття застосунку.</p>
<p>WRISTPET читає лише денні підсумки, а не окремі записи, пульс чи геолокацію, і нічого не записує в Apple Health. Якщо ви не надасте доступ, ви все одно зможете піклуватися про свого друга; лише автоматичний прогрес за кроками буде недоступний. Необов'язковий таймер прогулянки ніколи не додає кроків.</p>"""),
        ("Дані, що зберігаються лише на ваших пристроях", """
<p>Застосунок зберігає на ваших пристроях: вашого друга та його прогрес, цілі, моменти турботи, налаштування, спогади про прогулянки (дату, тривалість, необов'язкове самопочуття та ідею прогулянки), листівки з історії та до 35 днів денних підсумків кроків.</p>
<p>Віджети й ускладнення циферблата читають ці дані на тому самому пристрої. Якщо ви користуєтеся і iPhone, і Apple Watch, пристрої обмінюються даними напряму через Apple WatchConnectivity; дані не проходять через жоден наш сервер.</p>
<p>«Маршрути» в історії уявні. Застосунок не використовує вашу геолокацію.</p>"""),
        ("Сповіщення", """
<p>Якщо ви дозволите сповіщення, застосунок запланує одне локальне сповіщення на вашому пристрої, коли закінчиться таймер прогулянки. Дозвіл запитується, коли ви вперше починаєте прогулянку. Сповіщення створюється на пристрої й не надсилається через жоден сервер.</p>"""),
        ("Оплата: App Store", """
<p>WRISTPET купується один раз через Apple App Store за умовами й політикою конфіденційності Apple. Ми ніколи не отримуємо дані вашої картки, ім'я чи пошту облікового запису Apple; нам доступні лише узагальнені звіти про продажі, які Apple надає розробникам.</p>"""),
        ("Дозволи", """
<ul>
<li><strong>Apple Health</strong> - лише читання кроків і тренувань; запитується, коли ви натискаєте «Надати доступ до кроків».</li>
<li><strong>Сповіщення</strong> - про завершення прогулянки; запитуються, коли ви починаєте першу прогулянку.</li>
</ul>
<p>Застосунок не використовує геолокацію, контакти, камеру, мікрофон чи фото.</p>"""),
        ("Правові підстави обробки", """
<p>Якщо застосовується GDPR ЄС або Великої Британії: ми не збираємо й не отримуємо персональних даних. Описані вище дані обробляє сам застосунок на ваших пристроях, за вашою командою, щоб надати функції, якими ви користуєтеся.</p>"""),
        ("Зберігання", """
<p>Дані залишаються на ваших пристроях, доки ви не скористаєтеся пунктом <em>Налаштування › Почати заново</em> або не видалите застосунок. «Почати заново» на одному пристрої також стирає прогрес на пов'язаному iPhone чи Apple Watch під час наступного обміну даними. Видалення застосунку стирає лише копію на цьому пристрої. Якщо ви створюєте резервні копії iPhone в iCloud або на комп'ютері, копія Apple може містити дані застосунку відповідно до ваших налаштувань.</p>"""),
        ("Ваш вибір і права", f"""
<ul>
<li>Стерти прогрес: <em>Налаштування › Почати заново</em>; видалення застосунку також стирає його дані з пристрою.</li>
<li>Змінити чи відкликати доступ до Apple Health можна будь-коли в застосунку «Здоров'я» або в Параметрах пристрою. Після відкликання нові дані не читаються; щоб стерти вже збережений прогрес, скористайтеся «Почати заново».</li>
<li>Вимкнути сповіщення можна в Параметрах пристрою.</li>
<li>Залежно від країни проживання ви можете мати право на доступ до персональних даних, їх виправлення чи видалення та на скаргу до органу захисту даних. Оскільки ми не маємо жодних ваших даних, нам нічого експортувати чи видаляти, але ви можете написати на {MAIL} з будь-яким питанням. Див. також <a href="delete-data.html">Видалення даних</a>.</li>
</ul>"""),
        ("Діти", """
<p>WRISTPET підходить для будь-якого віку. Ми не збираємо персональної інформації ні від кого, зокрема від дітей молодше 13 років.</p>"""),
        ("Зміни", """
<p>Якщо ця політика суттєво зміниться, наприклад, якщо майбутня версія додасть покупки, синхронізацію чи сторонній сервіс, ми оновимо цю сторінку до випуску такої версії та згадаємо про це в описі оновлення.</p>"""),
        ("Контакти", f"""
<p>З питань конфіденційності: {MAIL}.</p>"""),
    ],
}

TERMS = {
    "en": [
        ("Agreement", f"""
<p>These terms apply to the WRISTPET app published by {OWNER} ("we", "us"). By using the app you accept them. Apple's <a href="{APPLE_EULA}">Standard End User License Agreement</a> also applies.</p>"""),
        ("What WRISTPET is", """
<p>WRISTPET is a light-hearted game and walking companion. It is not a medical device and does not give medical, fitness or health advice. Step counts come from Apple Health and may differ from other devices. Talk to a doctor before starting a new activity if you have any health concerns.</p>
<p>Walk at your own pace and stay aware of your surroundings; do not look at the screen while crossing roads or in traffic.</p>"""),
        ("Price", """
<ul>
<li>WRISTPET is a one-time paid download. The price is shown on the App Store before you buy and is charged to your Apple Account.</li>
<li>This version has no subscriptions, no in-app purchases and no ads. Every creature, story and feature is included.</li>
<li>Refunds are handled by Apple under its policies (reportaproblem.apple.com).</li>
</ul>"""),
        ("Your data", """
<p>Your progress is stored on your devices only; we keep no copy. Deleting the app from both your iPhone and Apple Watch, or using Start fresh, removes your progress and we cannot recover it.</p>"""),
        ("Licence and acceptable use", """
<p>We grant you a personal, non-transferable licence to use the app on Apple devices you own or control, as allowed by the App Store terms. Do not copy, resell, reverse engineer or misuse the app, except where the law allows it.</p>"""),
        ("Limitation of liability", """
<p>The app is provided "as is". We work to keep it reliable, but we do not guarantee that step counts, notifications or widget updates are always accurate or on time; they depend on Apple Health, device settings and battery limits. To the extent the law allows, we are not liable for indirect losses arising from use of the app.</p>"""),
        ("Changes", """
<p>We may update these terms. The current version is always on this page; material changes will be mentioned in the app update notes.</p>"""),
        ("Contact", f"""
<p>{MAIL}</p>"""),
    ],
    "uk": [
        ("Угода", f"""
<p>Ці умови застосовуються до застосунку WRISTPET, який публікує {OWNER} («ми»). Користуючись застосунком, ви їх приймаєте. Також діє <a href="{APPLE_EULA}">Стандартна ліцензійна угода Apple</a>.</p>"""),
        ("Що таке WRISTPET", """
<p>WRISTPET - легка гра й супутник для прогулянок. Це не медичний пристрій, і він не дає медичних, фітнес- чи оздоровчих порад. Кількість кроків надходить з Apple Health і може відрізнятися від інших пристроїв. Якщо маєте питання щодо здоров'я, порадьтеся з лікарем, перш ніж починати нову активність.</p>
<p>Рухайтеся у власному темпі й стежте за довкіллям; не дивіться на екран, переходячи дорогу чи поблизу транспорту.</p>"""),
        ("Ціна", """
<ul>
<li>WRISTPET - платний застосунок з разовою оплатою. Ціну App Store показує до покупки, оплата списується з облікового запису Apple.</li>
<li>У цій версії немає підписок, вбудованих покупок і реклами. Усі істоти, історії та функції включено.</li>
<li>Повернення коштів здійснює Apple за своїми правилами (reportaproblem.apple.com).</li>
</ul>"""),
        ("Ваші дані", """
<p>Ваш прогрес зберігається лише на ваших пристроях; ми не маємо його копії. Якщо видалити застосунок і з iPhone, і з Apple Watch або скористатися «Почати заново», прогрес буде стерто, і ми не зможемо його відновити.</p>"""),
        ("Ліцензія та використання", """
<p>Ми надаємо вам особисту ліцензію без права передачі на використання застосунку на пристроях Apple, якими ви володієте чи керуєте, відповідно до умов App Store. Не копіюйте, не перепродавайте, не здійснюйте зворотну розробку й не використовуйте застосунок неналежно, крім випадків, дозволених законом.</p>"""),
        ("Обмеження відповідальності", """
<p>Застосунок надається «як є». Ми дбаємо про його надійність, але не гарантуємо, що кількість кроків, сповіщення чи оновлення віджетів завжди точні й своєчасні: вони залежать від Apple Health, налаштувань пристрою та обмежень батареї. У межах, дозволених законом, ми не відповідаємо за непрямі збитки, пов'язані з використанням застосунку.</p>"""),
        ("Зміни", """
<p>Ми можемо оновлювати ці умови. Чинна версія завжди на цій сторінці; про суттєві зміни буде згадано в описі оновлення застосунку.</p>"""),
        ("Контакти", f"""
<p>{MAIL}</p>"""),
    ],
}

DELETE = {
    "en": [
        ("Data in the app", """
<p>WRISTPET has no accounts, so there is nothing to sign out of or close. Your companion, progress and walk memories are stored on your iPhone and Apple Watch.</p>
<ol>
<li>Open WRISTPET › <strong>Settings</strong>.</li>
<li>Tap <strong>Start fresh</strong> and confirm.</li>
</ol>
<p>Start fresh also clears the progress on your paired iPhone or Apple Watch the next time they exchange data. Deleting the app removes its data from that device only, so delete it on both devices to remove everything. Device backups you made in iCloud or on a computer are managed in your backup settings.</p>"""),
        ("Apple Health", """
<p>WRISTPET never writes to Apple Health, so deleting its data does not change your Health records. To stop the app reading steps, turn its access off in the Health app or in your device's Settings.</p>"""),
        ("Data we hold", f"""
<p>None. We do not receive or store any data about you. Questions: {MAIL}.</p>"""),
    ],
    "uk": [
        ("Дані в застосунку", """
<p>У WRISTPET немає облікових записів, тому виходити чи щось закривати не потрібно. Ваш друг, прогрес і спогади про прогулянки зберігаються на вашому iPhone та Apple Watch.</p>
<ol>
<li>Відкрийте WRISTPET › <strong>Налаштування</strong>.</li>
<li>Натисніть <strong>Почати заново</strong> й підтвердьте.</li>
</ol>
<p>«Почати заново» також стирає прогрес на пов'язаному iPhone чи Apple Watch під час наступного обміну даними. Видалення застосунку стирає його дані лише з цього пристрою, тож, щоб прибрати все, видаліть його з обох пристроїв. Резервними копіями в iCloud чи на комп'ютері керують налаштування резервного копіювання.</p>"""),
        ("Apple Health", """
<p>WRISTPET ніколи не записує дані в Apple Health, тож видалення його даних не змінює ваших записів у «Здоров'ї». Щоб застосунок більше не читав кроки, вимкніть йому доступ у застосунку «Здоров'я» або в Параметрах пристрою.</p>"""),
        ("Дані, які маємо ми", f"""
<p>Жодних. Ми не отримуємо й не зберігаємо даних про вас. Питання: {MAIL}.</p>"""),
    ],
}


def page(lang: str, slug: str, title: str, body: str) -> str:
    t = T[lang]
    other_label, other_lang = t["other"]
    other_href = (f"uk/{slug}" if lang == "en" else f"../{slug}")
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · WRISTPET</title>
<link rel="alternate" hreflang="{other_lang}" href="{other_href}">
<style>
{CSS}
</style>
</head>
<body>
<main>
<header>
  <a class="brand" href="./">WRISTPET</a>
  <nav><a href="{other_href}" hreflang="{other_lang}">{other_label}</a></nav>
</header>
{body}
<footer>{t["footer"]}</footer>
</main>
</body>
</html>
"""


def doc(lang: str, title: str, sections: list[tuple[str, str]]) -> str:
    parts = [f"<h1>{title}</h1>", f'<p class="updated">{T[lang]["updated"]}: {UPDATED[lang]}</p>']
    parts += [f"<section><h2>{h}</h2>{b.rstrip()}\n</section>" for h, b in sections]
    return "\n".join(parts)


def index(lang: str) -> str:
    t = T[lang]
    links = "\n".join(f'<li><a href="{s}">{t[k]}</a></li>'
                      for s, k in (("privacy.html", "privacy"), ("terms.html", "terms"), ("delete-data.html", "delete")))
    return f"<h1>WRISTPET</h1>\n<section><p>{t['tagline']}</p>\n<ul>\n{links}\n</ul>\n<p>{MAIL}</p>\n</section>"


def main() -> None:
    for lang in ("en", "uk"):
        out = ROOT if lang == "en" else ROOT / "uk"
        out.mkdir(exist_ok=True)
        t = T[lang]
        pages = {
            "index.html": ("WRISTPET", index(lang)),
            "privacy.html": (t["privacy"], doc(lang, t["privacy"], PRIVACY[lang])),
            "terms.html": (t["terms"], doc(lang, t["terms"], TERMS[lang])),
            "delete-data.html": (t["delete"], doc(lang, t["delete"], DELETE[lang])),
        }
        for slug, (title, body) in pages.items():
            (out / slug).write_text(page(lang, slug, title, body), encoding="utf-8", newline="\n")
    (ROOT / ".nojekyll").write_text("")
    print("built")


if __name__ == "__main__":
    main()
