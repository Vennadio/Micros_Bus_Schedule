from fastapi.testclient import TestClient
from bus_stops_service import main

client = TestClient(app)

def test_create_stop():
    stop_data = {"name": "Test Stop", "location": "Test Location"}
    response = client.post("/stops/", json=stop_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Stop"
    assert data["location"] == "Test Location"

def test_read_stops():
    response = client.get("/stops/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
