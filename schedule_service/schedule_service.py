from fastapi import FastAPI
import httpx

app = FastAPI()

async def get_schedule_from_routes_service(route_id: int):
    async with httpx.AsyncClient() as client:
        url = f"http://routes-service:8000/route/{route_id}/schedule"
        response = await client.get(url)
        return response.json()

@app.get("/schedule/{route_id}")
async def get_schedule(route_id: int):
    schedule = await get_schedule_from_routes_service(route_id)
    return schedule
