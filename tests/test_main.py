import json
from fastapi.testclient import TestClient
from main import app, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from models import Stop

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Создаем временную базу данных SQLite для тестов
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Создаем таблицы в тестовой базе данных
Base.metadata.create_all(bind=engine)

# Создаем тестового клиента
client = TestClient(app)

def test_create_stop():
    # Отправляем запрос на создание остановки
    stop_data = {"name": "Test Stop", "location": "Test Location"}
    response = client.post("/stops/", json=stop_data)

    # Проверяем, что запрос завершился успешно (код 200)
    assert response.status_code == 200

    # Проверяем, что в ответе содержатся правильные данные
    data = response.json()
    assert data["name"] == "Test Stop"
    assert data["location"] == "Test Location"

def test_read_stops():
    # Отправляем запрос на получение списка остановок
    response = client.get("/stops/")

    # Проверяем, что запрос завершился успешно (код 200)
    assert response.status_code == 200

    # Проверяем, что в ответе содержатся данные
    data = response.json()
    assert len(data) > 0
    assert "id" in data[0]
    assert "name" in data[0]
    assert "location" in data[0]
