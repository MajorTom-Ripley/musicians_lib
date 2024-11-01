from app import db, create_app
from app.models import Musician

# Создаем экземпляр приложения
app = create_app()

musicians_data = [
    {
        "id": 1,
        "name": "Дэвид Боуи",
        "instrument": "Вокал",
        "genre": "Рок",
        "image": "david_bowie.jpg",
        "bio": "Британский рок-музыкант, известный своими экспериментами с музыкальными стилями и образом. Один из самых влиятельных артистов в истории рока.",
        "song": "music/song_1.mp3",
        "video": {
            "youtube": {"url": "https://www.youtube.com/watch?v=123"},
            "rutube": {"url": "https://rutube.ru/video/123"},
            "plvideo": {"url": "https://plvideo.ru/video/123"}
        }
    },
    {
        "id": 2,
        "name": "Том Йорк",
        "instrument": "Вокал",
        "genre": "Рок",
        "image": "Thom_Yorke_1998.jpg",
        "bio": "Британский рок-музыкант, вокалист и гитарист группы Radiohead, известный своим уникальным вокальным стилем и глубокими текстами.",
        "song": "music/song_2.mp3",
        "video": {
            "youtube": {"url": "https://www.youtube.com/watch?v=123"},
            "rutube": {"url": "https://rutube.ru/video/123"},
            "plvideo": {"url": "https://plvideo.ru/video/123"}
        }
    },
    {
        "id": 3,
        "name": "Дэймон Албарн",
        "instrument": "Вокал, клавишные",
        "genre": "Рок",
        "image": "damon_albarn.jpg",
        "bio": "Британский музыкант, известный прежде всего как фронтмен группы Blur, а также как основатель и один из основных участников проектов Gorillaz.",
        "song": "music/song_3.mp3",
        "video": {
            "youtube": {"url": "https://www.youtube.com/watch?v=123"},
            "rutube": {"url": "https://rutube.ru/video/123"},
            "plvideo": {"url": "https://plvideo.ru/video/123"}
        }
    },
    {
        "id": 4,
        "name": "Дэвид Бирн",
        "instrument": "Вокал, гитара",
        "genre": "Рок, постпанк",
        "image": "david_byrne_no_jacket_required.jpg",
        "bio": "Американский музыкант, известный как основатель группы Talking Heads. Один из главных представителей альтернативного рока.",
        "song": "music/song_4.mp3",
        "video": {
            "youtube": {"url": "https://www.youtube.com/watch?v=123"},
            "rutube": {"url": "https://rutube.ru/video/123"},
            "plvideo": {"url": "https://plvideo.ru/video/123"}
        }
    },
    {
        "id": 5,
        "name": "Лиам и Ноэль Галлахеры",
        "instrument": "Вокал, гитара",
        "genre": "Рок, бритпоп",
        "image": "oasis.jpeg",
        "bio": "Британские музыканты, братья, участники культовой группы Oasis, ставшие символами бритпопа 90-х годов.",
        "song": "music/song_5.mp3",
        "video": {
            "youtube": {"url": "https://www.youtube.com/watch?v=123"},
            "rutube": {"url": "https://rutube.ru/video/123"},
            "plvideo": {"url": "https://plvideo.ru/video/123"}
        }
    },
    {
        "id": 6,
        "name": "Мэттью Беллами",
        "instrument": "Вокал, гитара, клавишные",
        "genre": "Рок",
        "image": "metyu_bellamy.jpg",
        "bio": "Британский музыкант, фронтмен группы Muse, известный своими уникальными вокальными способностями и виртуозной игрой на гитаре.",
        "song": "music/song_6.mp3",
        "video": {
            "youtube": {"url": "https://www.youtube.com/watch?v=123"},
            "rutube": {"url": "https://rutube.ru/video/123"},
            "plvideo": {"url": "https://plvideo.ru/video/123"}
        }
    },

    {
        "id": 7,
        "name": "Ричард Эшкрофт",
        "instrument": "Вокал, гитара",
        "genre": "Бритпоп, альтернативный рок",
        "image": "verve.jpg",
        "bio": "Британский музыкант, наиболее известен как вокалист и автор песен группы The Verve. После распада коллектива продолжил успешную сольную карьеру, сочетая рок и поп-звучание.",
        "song": "music/song_7.mp3",
        "video": {
            "youtube": {"url": "https://www.youtube.com/watch?v=123"},
            "rutube": {"url": "https://rutube.ru/video/123"},
            "plvideo": {"url": "https://plvideo.ru/video/123"}
        }
    },

    {
        "id": 8,
        "name": "Ким Джонван",
        "instrument": "Вокал, гитара, клавишные",
        "genre": "Альтернативный рок, инди-рок",
        "image": "kim_jong_wan.jpg",
        "bio": "Южнокорейский музыкант, вокалист и автор песен группы Nell. Известен своими проникновенными текстами, атмосферным звучанием и меланхоличным вокалом, которые сделали группу культовой на корейской рок-сцене.",
        "song": "music/song_8.mp3",
        "video": {
            "youtube": {"url": "https://www.youtube.com/watch?v=123"},
            "rutube": {"url": "https://rutube.ru/video/123"},
            "plvideo": {"url": "https://plvideo.ru/video/123"}
        }
    },
    {
        "id": 9,
        "name": "Моррисси",
        "instrument": "Вокал, тексты",
        "genre": "Альтернативный рок, инди-поп",
        "image": "morrisey.jpg",
        "bio": "Стивен Патрик Моррисси – британский музыкант и автор песен, ставший известным как фронтмен группы The Smiths (1982–1987). Его поэтичные, часто меланхоличные тексты в сочетании с уникальным вокальным стилем сделали группу культовой. После распада The Smiths он продолжил успешную сольную карьеру, сочетая постпанк и поп с острой социальной и политической лирикой.",
        "song": "music/song_9.mp3",
        "video": {
            "youtube": {"url": "https://www.youtube.com/watch?v=123"},
            "rutube": {"url": "https://rutube.ru/video/123"},
            "plvideo": {"url": "https://plvideo.ru/video/123"}
        }
    }
]


# Функция для добавления данных в базу
def add_musicians(musicians):
    with app.app_context():  # Устанавливаем контекст приложения
        for musician in musicians:
            new_musician = Musician(
                id=musician["id"],
                name=musician["name"],
                instrument=musician["instrument"],
                genre=musician["genre"],
                image=musician["image"],
                bio=musician["bio"],
                song=musician["song"],
                youtube_video_url=musician["video"]["youtube"]["url"],
                rutube_video_url=musician["video"]["rutube"]["url"],
                plvideo_video_url=musician["video"]["plvideo"]["url"],
            )
            db.session.add(new_musician)  # Добавляем нового музыканта в сессию

        db.session.commit()  # Сохраняем изменения в базе данных

# Вызов функции для добавления музыкантов
add_musicians(musicians_data)