from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

FIRST_SERVICE_URL = "http://stops-service:8000/stops/"

@app.get("/processed_stops/")
def process_stops():
    try:
        response = requests.get(FIRST_SERVICE_URL)
        response.raise_for_status() 

        stops_data = response.json()

        # Обработка данных
        processed_stops = []

        for stop in stops_data:
            processed_stop = {
                "name": stop["name"].upper(),
                "location": stop["location"]
            }
            processed_stops.append(processed_stop)

        return processed_stops

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error while fetching stops data: {str(e)}")
    
@app.get("/first_stop/")
def get_first_stop():
    try:
        response = requests.get(FIRST_SERVICE_URL)
        response.raise_for_status() 

        stops_data = response.json()

        if stops_data:
            first_stop = {
                "name": stops_data[0]["name"],
                "location": stops_data[0]["location"]
            }
            return first_stop
        else:
            raise HTTPException(status_code=404, detail="No stops found")

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error while fetching stops data: {str(e)}")