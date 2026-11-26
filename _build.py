#!/usr/bin/env python3
# Сайт игры «ШАЙБУ!»: главная и политика конфиденциальности (ru / en).
# Тексты правятся здесь, потом: python3 _build.py — HTML пересоберётся рядом.
# Файлы с «_» в начале GitHub Pages не публикует.
import hashlib
import os

EMAIL = 'rinkrogue.app@gmail.com'   # почта для вопросов и отзывов
BETA = 'https://testflight.apple.com/join/SzEd2gEs'  # публичная ссылка TestFlight
# APK — последний релиз в GitHub (тег beta-N; файл всегда Deck_the_Rink.apk)
APK = 'https://github.com/warlockjohn/rinkrogue-site/releases/latest/download/Deck_the_Rink.apk'
# Статистика посещений: GoatCounter, без cookies (hockeyrogue.goatcounter.com)
GOAT = 'hockeyrogue'
# Чат тестеров в Telegram
TG = 'https://t.me/Deck_the_rink'
BASE = '/rinkrogue-site/'       # сайт живёт в подпапке warlockjohn.github.io/rinkrogue-site
SITE = 'https://warlockjohn.github.io' + BASE
OWNER = 'Yevgeniy Avdonin'
LANGS = ['ru', 'en']
# Скриншоты для главной: файлы в assets/, по порядку. Добавляются сюда — и python3 _build.py
SHOTS = {
    'ru': ['shot_splash.jpg', 'shot_map_ru.jpg', 'shot_match_ru.jpg', 'shot_goal_ru.jpg'],
    'en': ['shot_splash_en.jpg', 'shot_map_en.jpg', 'shot_match.jpg', 'shot_goal.jpg'],
}
LANG_LABEL = {'ru': 'Рус', 'en': 'Eng'}

T = {
    'ru': {
        'name': 'ШАЙБУ!',
        'title': 'ШАЙБУ! — хоккейный карточный рогалик',
        'desc': 'Хоккейный карточный рогалик для iPhone: дворовые команды, колоды-характеры, драки, буллиты и кубки. Комикс в духе 60-х.',
        'h1': 'Выбери команду, собери колоду — выиграй районный кубок',
        'lead': 'Карточный рогалик про дворовый хоккей. Выбери команду — от моржей-пенсионеров до бабок у подъезда — собери колоду и пройди турнир: группа, плей-офф, финал и босс. Пасуй, бросай, толкайся у бортика, а не хватит времени — бей буллиты.',
        'badge': 'iPhone',
        'badge_small': 'бета в TestFlight',
        'apk': 'Android',
        'apk_small': 'APK-файл',
        'tg': 'Чат тестеров в Telegram',
        'tg_small': 'баги, идеи, баланс',
        'apk_hint': 'Android: скачай файл и открой. Телефон спросит разрешение на установку из этого источника — разреши, в Google Play игры пока нет.',
        'soon': 'Бета в TestFlight — по приглашению',
        'note': 'Бесплатно, без рекламы. Русский и английский язык.',
        'shots_h': 'Скриншоты',
        'feat_h': 'Что внутри',
        'feat': [
            ('Шесть команд со своим характером', 'Дворовые, Моржи, Пенные, Шпана, Вожатые и Бабки у подъезда. У каждой своя колода и свой фирменный приём.'),
            ('Матч — это партия в карты', 'Три периода по четыре хода. Каждая карта — действие: пас, бросок, силовой, сейв. На всё сил не хватит, а в концовке можно снять вратаря.'),
            ('Турнир от двора до горы', 'Три акта: двор, лес и снежная вершина, в каждом свой босс. Между матчами — Барахолка, Баня, Тренер и сундуки.'),
            ('Наклейки и кубки', 'Достижения открывают новые карты и талисманы, а за каждый пройденный каток на полку встаёт кубок посолиднее.'),
        ],
        'privacy': 'Конфиденциальность',
        'home': 'Главная',
        'made': 'Сделано в Алматы',
        'p_title': 'Политика конфиденциальности',
        'updated': 'Обновлено: 22 ноября 2026',
        'p_body': [
            ('', '<p class="hi"><b>Коротко:</b> игра не собирает ваши личные данные. Нет регистрации, рекламы и сторонней аналитики. Прогресс хранится только на вашем телефоне.</p>'),
            ('Что хранится на телефоне', '<p>Сохранение карьеры, открытые команды и катки, кубки на полке, настройки звука и языка, просмотренные подсказки. Всё это лежит внутри приложения на вашем iPhone, у разработчика доступа к этому нет.</p>'),
            ('Статистика матчей в тестовых версиях', '<p>Тестовые версии игры могут отправлять разработчику обезличенную статистику сыгранных матчей, чтобы настраивать баланс: время матча, выбранная команда и соперник, этап турнира, счёт, число бросков, удалений и драк, какие карты были сыграны, а также платформу (iOS или Android), язык игры, её версию и случайный номер установки — его игра придумывает сама при первом запуске, чтобы отличать матчи одного игрока от другого. В ней нет имени, почты, номера телефона, рекламного идентификатора, геолокации и других сведений, по которым можно узнать игрока. Данные хранятся в таблице разработчика (Google) и используются только для настройки игры.</p>'),
            ('Интернет и сторонние сервисы', '<p>Игра работает без аккаунта. Через интернет она скачивает обновления игры (сервис Expo) и, в тестовых версиях, отправляет статистику, описанную выше. Рекламы, покупок внутри игры и сторонних SDK для аналитики или трекинга нет.</p>'),
            ('Этот сайт', '<p>Сайт считает посещения через GoatCounter — без cookies и без сбора личных данных: только сколько людей зашло, с какой страницы пришли и нажали ли кнопку скачивания. IP-адреса не сохраняются.</p>'),
            ('Разрешения', '<p>Игра не запрашивает доступ к камере, микрофону, фото, контактам и геолокации. Вибрация используется только для эффектов в матче.</p>'),
            ('Тестирование через TestFlight', '<p>Если вы тестируете бету, Apple может передавать разработчику отчёты о сбоях и ваши отзывы с тем, что вы сами в них укажете. Подробнее — в <a href="https://www.apple.com/legal/privacy/data/en/test-flight/">правилах TestFlight</a>.</p>'),
            ('Дети', '<p>Игра не предназначена для сбора данных о ком-либо, в том числе о детях, и не просит вводить личные сведения.</p>'),
            ('Удаление данных', '<p>Удалите приложение — и весь прогресс будет удалён с телефона. Обезличенную статистику нельзя связать с конкретным игроком, поэтому найти и удалить «свои» записи невозможно; если у вас есть вопросы — напишите нам.</p>'),
            ('Изменения', '<p>Если политика изменится, новая версия появится на этой странице с новой датой.</p>'),
            ('Связь', f'<p>Владелец приложения: {OWNER}.<br>Вопросы: <a href="mailto:{EMAIL}">{EMAIL}</a></p>'),
        ],
    },
    'en': {
        'name': 'Deck the Rink',
        'title': 'Deck the Rink — a hockey card roguelike',
        'desc': 'A hockey card roguelike for iPhone: backyard teams, decks with character, fights, shootouts and trophies. 1960s comic style.',
        'h1': 'Pick a team, build a deck — win the neighborhood cup',
        'lead': 'A card roguelike about backyard hockey. Pick a team — from retired ice-swimmers to the grannies from the porch bench — build your deck and fight through the tournament: group stage, playoffs, final and a boss. Pass, shoot, throw your weight around by the boards, and if time runs out — it\'s a shootout.',
        'badge': 'iPhone',
        'badge_small': 'TestFlight beta',
        'apk': 'Android',
        'apk_small': 'APK file',
        'tg': 'Testers chat on Telegram',
        'tg_small': 'bugs, ideas, balance',
        'apk_hint': 'Android: download the file and open it. Your phone will ask to allow installs from this source — allow it, the game is not on Google Play yet.',
        'soon': 'TestFlight beta — invitation only',
        'note': 'Free, no ads. English and Russian.',
        'shots_h': 'Screenshots',
        'feat_h': 'What\'s inside',
        'feat': [
            ('Six teams, six personalities', 'Backyard Crew, Old Walruses, The Foamers, Street Rats, Scout Leaders and Porch Grannies. Each has its own deck and its own signature move.'),
            ('A match is a game of cards', 'Three periods of four turns. Every card is an action: pass, shot, check, save. You never have the legs for everything — and late on you can pull the goalie.'),
            ('From the yard to the mountain top', 'Three acts: the yard, the forest and a snowy summit, each with its own boss. Between matches — the Flea Market, the Sauna, the Coach and chests.'),
            ('Stickers and trophies', 'Achievements unlock new cards and talismans, and every rink you beat puts a shinier trophy on your shelf.'),
        ],
        'privacy': 'Privacy',
        'home': 'Home',
        'made': 'Made in Almaty',
        'p_title': 'Privacy Policy',
        'updated': 'Updated: November 22, 2026',
        'p_body': [
            ('', '<p class="hi"><b>In short:</b> the game does not collect your personal data. No sign-up, no ads, no third-party analytics. Your progress stays on your phone.</p>'),
            ('What is stored on your phone', '<p>Your career save, unlocked teams and rinks, trophies on the shelf, sound and language settings, and which tips you have seen. All of it lives inside the app on your iPhone; the developer has no access to it.</p>'),
            ('Match statistics in test versions', '<p>Test versions of the game may send the developer anonymous statistics about finished matches to help tune the balance: time of the match, your team and the opponent, tournament stage, score, number of shots, penalties and fights, which cards were played, as well as the platform (iOS or Android), game language, game version and a random install number — the game makes it up on first launch to tell one player\'s matches from another\'s. It contains no name, email, phone number, advertising identifier, location or anything else that could identify a player. The data is kept in the developer\'s spreadsheet (Google) and used only to tune the game.</p>'),
            ('Internet and third-party services', '<p>The game works without an account. It uses the internet to download game updates (Expo) and, in test versions, to send the statistics described above. There are no ads, no in-app purchases and no third-party analytics or tracking SDKs.</p>'),
            ('This website', '<p>The site counts visits with GoatCounter — no cookies and no personal data: only how many people came, which page referred them and whether they clicked a download button. IP addresses are not stored.</p>'),
            ('Permissions', '<p>The game does not ask for access to your camera, microphone, photos, contacts or location. Vibration is used only for in-match effects.</p>'),
            ('TestFlight', '<p>If you test the beta, Apple may share crash reports and your feedback with the developer, including whatever you choose to put in it. See the <a href="https://www.apple.com/legal/privacy/data/en/test-flight/">TestFlight privacy terms</a>.</p>'),
            ('Children', '<p>The game is not designed to collect data about anyone, including children, and never asks for personal information.</p>'),
            ('Deleting data', '<p>Delete the app and all progress is removed from your phone. Anonymous statistics cannot be linked to a particular player, so it is not possible to find and delete "your" records; if you have questions, write to us.</p>'),
            ('Changes', '<p>If this policy changes, the new version will appear on this page with a new date.</p>'),
            ('Contact', f'<p>App owner: {OWNER}.<br>Questions: <a href="mailto:{EMAIL}">{EMAIL}</a></p>'),
        ],
    },
}


def prefix(lang):
    return BASE if lang == 'ru' else f'{BASE}{lang}/'


def page(lang, slug, title, desc, body):
    t = T[lang]
    file = 'index.html' if slug == '' else f'{slug}.html'
    alt = ''.join(f'<link rel="alternate" hreflang="{l}" href="https://warlockjohn.github.io{prefix(l)}{file if slug else ""}">' for l in LANGS)
    langs = ''.join(f'<a href="{prefix(l)}{file if slug else ""}" class="{"on" if l == lang else ""}" hreflang="{l}">{LANG_LABEL[l]}</a>' for l in LANGS)
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}assets/icon.png">
<meta name="theme-color" content="#0E1620">
{alt}
<link rel="icon" href="{BASE}assets/favicon.png">
<link rel="apple-touch-icon" href="{BASE}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{BASE}style.css">
</head>
<body>
<div class="wrap">
<header class="top">
  <a class="brand" href="{prefix(lang)}"><img src="{BASE}assets/icon.png" alt="">{t['name']}</a>
  <nav class="langs">{langs}</nav>
</header>
{body}
<footer>
  <span>© 2026 {t['name']} · {t['made']}</span>
  <a href="{prefix(lang)}">{t['home']}</a>
  <a href="{prefix(lang)}privacy.html">{t['privacy']}</a>
  <a href="{TG}" data-goatcounter-click="tg-chat-footer">Telegram</a>
  <a href="mailto:{EMAIL}">{EMAIL}</a>
</footer>
</div>
<script data-goatcounter="https://{GOAT}.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</body>
</html>
'''


def home(lang):
    t = T[lang]
    cta = (f'<div class="btns"><a class="btn" href="{BETA}" data-goatcounter-click="get-ios" data-goatcounter-title="iPhone">{t["badge"]}<small>{t["badge_small"]}</small></a>'
           f'<a class="btn" href="{APK}" data-goatcounter-click="get-android" data-goatcounter-title="Android">{t["apk"]}<small>{t["apk_small"]}</small></a></div>'
           f'<p class="apkhint">{t["apk_hint"]}</p>'
           f'<a class="btn tg" href="{TG}" data-goatcounter-click="tg-chat" data-goatcounter-title="Telegram">{t["tg"]}<small>{t["tg_small"]}</small></a>' if BETA
           else f'<p class="soon">{t["soon"]}</p>')
    # ?v=<хэш файла> — чтобы браузер не показывал старую картинку после замены
    ver = lambda f: hashlib.md5(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', f), 'rb').read()).hexdigest()[:8]
    shots = ''.join(f'<img src="{BASE}assets/{f}?v={ver(f)}" alt="" loading="lazy">' for f in SHOTS[lang])
    feats = ''.join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in t['feat'])
    body = f'''<section class="hero">
  <img class="logo" src="{BASE}assets/icon.png" alt="">
  <h1>{t['h1']}</h1>
  <p class="lead">{t['lead']}</p>
  {cta}
  <p class="note">{t['note']}</p>
</section>
<section>
  <h2>{t['shots_h']}</h2>
  <div class="shots">{shots}</div>
</section>
<section>
  <h2>{t['feat_h']}</h2>
  <div class="grid">{feats}</div>
</section>'''
    return page(lang, '', t['title'], t['desc'], body)


def privacy(lang):
    t = T[lang]
    parts = ''.join((f'<h2>{h}</h2>' if h else '') + b for h, b in t['p_body'])
    body = f'<article class="doc"><h1>{t["p_title"]}</h1><p class="date">{t["updated"]}</p>{parts}</article>'
    return page(lang, 'privacy', f'{t["p_title"]} — {t["name"]}', t['desc'], body)


here = os.path.dirname(os.path.abspath(__file__))
for lang in LANGS:
    d = here if lang == 'ru' else os.path.join(here, lang)
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w').write(home(lang))
    open(os.path.join(d, 'privacy.html'), 'w').write(privacy(lang))
print('ok')
