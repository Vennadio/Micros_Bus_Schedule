from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fastapi.testclient import TestClient
from bus_stops_service.main import app, get_db

SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False})
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

def test_create_and_read_stops():
    # Проверяем создание остановки
    stop_data = {"name": "Test Stop", "location": "Test Location"}
    response = client.post("/stops/", json=stop_data)
    assert response.status_code == 200
    created_stop = response.json()
    assert created_stop["name"] == "Test Stop"
    assert created_stop["location"] == "Test Location"

    # Проверяем чтение списка остановок
    response = client.get("/stops/")
    assert response.status_code == 200
    stops = response.json()
    assert len(stops) == 1
    assert stops[0]["name"] == "Test Stop"
    assert stops[0]["location"] == "Test Location"
