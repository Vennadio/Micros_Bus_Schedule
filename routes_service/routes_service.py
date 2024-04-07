from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# URL первого сервиса, откуда будем брать данные об остановках
FIRST_SERVICE_URL = "http://stops-service:8000/stops/"

@app.get("/processed_stops/")
def process_stops():
    try:
        # Получаем данные об остановках из первого сервиса
        response = requests.get(FIRST_SERVICE_URL)
        response.raise_for_status()  # Проверяем успешность запроса

        stops_data = response.json()

        # Обработка данных
        processed_stops = []

        for stop in stops_data:
            # Например, преобразование названия остановки в верхний регистр
            processed_stop = {
                "name": stop["name"].upper(),
                "location": stop["location"]
            }
            processed_stops.append(processed_stop)

        return processed_stops

    except requests.RequestException as e:
        # В случае ошибки при запросе к первому сервису
        raise HTTPException(status_code=500, detail=f"Error while fetching stops data: {str(e)}")
