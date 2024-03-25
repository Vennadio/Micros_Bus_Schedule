from fastapi import FastAPI
import asyncpg
import asyncio

app = FastAPI()

async def get_schedule_from_db(route_id: int):
    conn = await asyncpg.connect(user="myuser", password="mypassword",
                                 database="mydatabase", host="db")
    try:
        query = "SELECT * FROM bus_schedule WHERE route_id = $1"
        rows = await conn.fetch(query, route_id)
        return [dict(row) for row in rows]
    finally:
        await conn.close()

@app.get("/route/{route_id}/schedule")
async def get_schedule(route_id: int):
    schedule = await get_schedule_from_db(route_id)
    return {"route_id": route_id, "schedule": schedule}
