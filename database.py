from app.models import db, Musician
from app import app

musicians_data = [
    {
        "id": 1,
        "name": "Дэвид Боуи",
        "instrument": "Вокал",
        "genre": "Рок",
        "image": "david_bowie.jpg",
        "bio": "Британский рок-музыкант, известный своими экспериментами с музыкальными стилями и образом. Один из самых влиятельных артистов в истории рока.",
        "song": "music/song_1.mp3"
    },
    {
        "id": 2,
        "name": "Том Йорк",
        "instrument": "Вокал",
        "genre": "Рок",
        "image": "Thom_Yorke_1998.jpg",
        "bio": "Британский рок-музыкант, вокалист и гитарист группы Radiohead, известный своим уникальным вокальным стилем и глубокими текстами.",
        "song": "music/song_2.mp3"
    },
    {
        "id": 3,
        "name": "Дэймон Албарн",
        "instrument": "Вокал, клавишные",
        "genre": "Рок",
        "image": "damon_albarn.jpg",
        "bio": "Британский музыкант, известный прежде всего как фронтмен группы Blur, а также как основатель и один из основных участников проектов Gorillaz.",
        "song": "music/song_3.mp3"
    },
    {
        "id": 4,
        "name": "Дэвид Бирн",
        "instrument": "Вокал, гитара",
        "genre": "Рок, постпанк",
        "image": "david_byrne_no_jacket_required.jpg",
        "bio": "Американский музыкант, известный как основатель группы Talking Heads. Один из главных представителей альтернативного рока.",
        "song": "music/song_4.mp3"
    },
    {
        "id": 5,
        "name": "Лиам и Ноэль Галлахеры",
        "instrument": "Вокал, гитара",
        "genre": "Рок, бритпоп",
        "image": "oasis.jpeg",
        "bio": "Британские музыканты, братья, участники культовой группы Oasis, ставшие символами бритпопа 90-х годов.",
        "song": "music/song_5.mp3"
    },
    {
        "id": 6,
        "name": "Мэттью Беллами",
        "instrument": "Вокал, гитара, клавишные",
        "genre": "Рок",
        "image": "metyu_bellamy.jpg",
        "bio": "Британский музыкант, фронтмен группы Muse, известный своими уникальными вокальными способностями и виртуозной игрой на гитаре.",
        "song": "music/song_6.mp3"
    },

    {
        "id": 7,
        "name": "Ричард Эшкрофт",
        "instrument": "Вокал, гитара",
        "genre": "Бритпоп, альтернативный рок",
        "image": "verve.jpg",
        "bio": "Британский музыкант, наиболее известен как вокалист и автор песен группы The Verve. После распада коллектива продолжил успешную сольную карьеру, сочетая рок и поп-звучание.",
        "song": "music/song_7.mp3"
    },

    {
        "id": 8,
        "name": "Ким Джонван",
        "instrument": "Вокал, гитара, клавишные",
        "genre": "Альтернативный рок, инди-рок",
        "image": "kim_jong_wan.jpg",
        "bio": "Южнокорейский музыкант, вокалист и автор песен группы Nell. Известен своими проникновенными текстами, атмосферным звучанием и меланхоличным вокалом, которые сделали группу культовой на корейской рок-сцене.",
        "song": "music/song_8.mp3"
    },
    {
        "id": 9,
        "name": "Моррисси",
        "instrument": "Вокал, тексты",
        "genre": "Альтернативный рок, инди-поп",
        "image": "morrisey.jpg",
        "bio": "Стивен Патрик Моррисси – британский музыкант и автор песен, ставший известным как фронтмен группы The Smiths (1982–1987). Его поэтичные, часто меланхоличные тексты в сочетании с уникальным вокальным стилем сделали группу культовой. После распада The Smiths он продолжил успешную сольную карьеру, сочетая постпанк и поп с острой социальной и политической лирикой.",
        "song": "music/song_9.mp3"
    }
]


def add_musicians_to_db():
    for musician_data in musicians_data:
        musician = Musician(
            id=musician_data["id"],
            name=musician_data["name"],
            instrument=musician_data["instrument"],
            genre=musician_data["genre"],
            image=musician_data["image"],
            bio=musician_data["bio"],
            song=musician_data["song"]
        )
        db.session.add(musician)
    db.session.commit()

# Запуск добавления данных в базу
with app.app_context():
    db.create_all()  # Создаём таблицы
    add_musicians_to_db()  # Добавляем музыкантов