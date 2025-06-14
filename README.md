# AI Blog

Блог о искусственном интеллекте и машинном обучении, созданный на Django.

## Возможности

- Публикация новостей и статей
- Система комментариев
- Лайки и дизлайки для новостей
- Модерация контента
- Административная панель
- Поддержка изображений
- Адаптивный дизайн

## Технологии

- Python 3.13+
- Django 5.2
- Bootstrap 5
- JavaScript
- SQLite (для разработки)
- Pillow (для работы с изображениями)

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Crowley55555/dj01.git
cd ai-blog
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл .env в корневой директории проекта и добавьте необходимые переменные окружения:
```
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
```

5. Примените миграции:
```bash
python manage.py migrate
```

6. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

7. Запустите сервер разработки:
```bash
python manage.py runserver
```

## Использование

1. Откройте браузер и перейдите по адресу http://127.0.0.1:8000/
2. Для доступа к административной панели перейдите по адресу http://127.0.0.1:8000/admin/

## Структура проекта

```
ai-blog/
├── cyberblog/              # Основной проект Django
│   ├── ai_blog/           # Приложение для статей и данных
│   ├── news/              # Приложение для новостей
│   ├── templates/         # Общие шаблоны
│   └── static/            # Статические файлы
├── media/                 # Загруженные файлы
├── requirements.txt       # Зависимости проекта
└── README.md             # Документация
```

## Разработка

1. Создайте новую ветку для ваших изменений:
```bash
git checkout -b feature/your-feature-name
```

2. Внесите изменения и зафиксируйте их:
```bash
git add .
git commit -m "Описание ваших изменений"
```

3. Отправьте изменения в репозиторий:
```bash
git push origin feature/your-feature-name
```

## Лицензия

MIT License. См. файл LICENSE для подробностей.

## Контакты

Если у вас есть вопросы или предложения, создайте issue в репозитории проекта.


## Разработчики

- [Crowley](https://github.com/Crowley55555) Лавров Артем

