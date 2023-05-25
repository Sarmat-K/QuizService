# QuizService

QuizService - это веб-сервис, который получает случайные вопросы для викторины из публичного API и сохраняет их в базе данных PostgreSQL. Он предоставляет REST API для получения ранее сохраненных вопросов для викторины.

## Подготовка

- Docker
- Docker Compose

## Начало работы

Чтобы начать работу с QuizService, выполните следующие шаги:

1. Клонируйте репозиторий:

   ```bash
   git clone <repository-url>

2. Перейдите в папку проекта:

    ```bash
    cd QuizService

3. Соберите и запустите Docker контейнеры:


    ```bash
    docker-compose up -d

Это создаст и запустит контейнер PostgreSQL вместе с контейнером Flask веб-сервиса.

4. Получите доступ к API веб-сервиса:
API веб-сервиса доступно по адресу http://localhost:5000/.
Используйте инструменты, такие как cURL или Postman, для отправки запросов к API.

# Документация по API

API QuizService предоставляет следующий эндпоинт:

## Получение случайных вопросов для викторины


-URL: /questions
-Метод: POST
-Формат тела запроса: JSON
-Пример тела запроса:
        
        {
    "questions_num": 5
        }
    -Формат ответа: JSON
    -Пример ответа:
        {
    "questions": [
        {
        "id": 1,
        "question": "Какая столица Франции?",
        "answer": "Париж",
        "created_at": "2023-05-24 10:00:00"
        },
        {
        "id": 2,
        "question": "Какая самая большая планета в Солнечной системе?",
        "answer": "Юпитер",
        "created_at": "2023-05-24 10:01:00"
        },
        ...
    ]
    }

# Разработка

Чтобы запустить QuizService локально для разработки, выполните следующие шаги:

1.Создайте и активируйте виртуальное окружение (опционально, но рекомендуется):

    ```bash 
    python -m venv venv
    ```
    source venv/bin/activate

2. Установите необходимые пакеты Python:

    ```bash 
    pip install -r requirements.txt

3. Установите переменные окружения:
    
    ```bash 
    export FLASK_APP=app.py
    export FLASK_ENV=development

4. Запустите сервер разработки Flask:
    
    ```bash 
    flask run




