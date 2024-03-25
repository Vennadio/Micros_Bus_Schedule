# Используем базовый образ Python
FROM python:3.9

# Устанавливаем зависимости
RUN pip install --no-cache-dir fastapi uvicorn asyncpg httpx

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем исходный код в контейнер
COPY /routes_service /app/routes_service

# Определяем команду для запуска сервера
CMD ["uvicorn", "routes_service.routes_service:app", "--host", "0.0.0.0", "--port", "8000"]
