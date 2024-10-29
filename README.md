## Домашнее задание на 18.10.2024

```
1. Создать базу данных с помощью SQLAlchemy с подключением маршрутизации и pydantic.
2. Cоздать авторизацию и аутентификацию пользователей по логину и паролю (шифрование пароля с помощью sha-512).
3. Добавление музыкальных треков в избранное, относительно аккаунта пользователя.
```

**Flask-Login** для управления сессиями пользователей.
**Flask-Bcrypt** для безопасного хранения паролей.
**Flask-WTF** для создания и валидации форм.

```cmd
pip install Flask-Login Flask-Bcrypt Flask-WTF
```

```
musicians_lib
├── app/
│   ├── __init__.py              # Инициализация приложения
│   ├── config.py                # Конфигурации приложения
│   ├── models.py                # Модели базы данных
│   ├── routes.py                # Маршруты и обработчики
│   ├── forms.py                 # Формы для аутентификации и других действий
│   ├── security.py              # Защита данных
│   ├── templates/               # HTML-шаблоны
│   │   ├── base.html            # Базовый шаблон
│   │   ├── musicians.html       # Шаблон для отображения музыкантов
│   │   └── musician_detail.html # Шаблон для деталей музыканта
│   │
│   ├── static/                  # Статические файлы (CSS, JS, изображения)
│   │   ├── css/                 # Папка с CSS стилями
│   │   │   └── styles.css       # CSS стили
│   │   ├── images/              # Папка для изображений
│   │   ├── js/                  # Папка для скриптов
│   │   └── music/               # Папка с музыкой
│   │
│   └── instance/                # Папка для базы данных
│       └── musicians.db         # База данных SQLite
│
├── run.py                       # Точка входа в приложение
└── requirements.txt             # Зависимости проекта
```