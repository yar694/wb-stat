# Wildberries Analytics — v0 (Backend-first)

Минимальный каркас сервиса аналитики для продавца Wildberries. На этом этапе — готов API на FastAPI с тестовым эндпоинтом для статистики рекламной кампании (демо-данные).

## Как запустить локально

1) Установите Python 3.11+.
2) Создайте и активируйте виртуальное окружение:
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```
3) Установите зависимости и запустите сервер:
```bash
pip install -r backend/requirements.txt
uvicorn app.main:app --app-dir backend --reload
```
Сервер поднимется на `http://127.0.0.1:8000`.
Открыть Swagger можно по адресу: `http://127.0.0.1:8000/docs`.

## Переменные окружения

Скопируйте `.env.example` в `.env` и при необходимости заполните:
```
WB_API_TOKEN=your_token_here
```
Пока токен не используется (данные демонстрационные), но скоро подключим настоящий клиент.

## Docker (опционально)

```bash
docker build -t wb-analytics-backend -f backend/Dockerfile backend
docker run --rm -p 8000:8000 wb-analytics-backend
```

## Структура

```
wb-analytics/
├─ backend/
│  ├─ app/
│  │  ├─ main.py
│  │  ├─ config.py
│  │  ├─ wb_client.py
│  │  └─ routers/
│  │     ├─ health.py
│  │     └─ ads.py
│  ├─ tests/
│  │  └─ test_health.py
│  ├─ requirements.txt
│  └─ Dockerfile
├─ .env.example
└─ .gitignore
```

## Пушим в GitHub

1. Создайте новый пустой репозиторий на GitHub (без README/License, чтобы избежать конфликтов).
2. В терминале из корня проекта (`wb-analytics/`):
```bash
git init
git add .
git commit -m "chore: init wb-analytics backend scaffold"
git branch -M main
git remote add origin https://github.com/<ВАШ_НИК>/<ИМЯ_РЕПОЗИТОРИЯ>.git
git push -u origin main
```
Готово!

## Дальше (на выбор)

- Подключить настоящий Wildberries API (ads stats, orders, stocks).
- Добавить базу данных (PostgreSQL) и расписание ETL-задач (например, APScheduler/Celery).
- Сделать простую админ-панель/фронтенд (React) с графиками.
- Добавить авторизацию пользователей и роли.
- Написать алерты/рекомендации (логика + шаблоны уведомлений).