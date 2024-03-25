# Используем базовый образ Python
FROM python:3.9

# Устанавливаем зависимости
RUN pip install --no-cache-dir fastapi uvicorn httpx

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем исходный код в контейнер
COPY ./schedule_service /app/schedule_service

# Определяем команду для запуска сервера
CMD ["uvicorn", "schedule_service.schedule_service:app", "--host", "0.0.0.0", "--port", "8000"]
