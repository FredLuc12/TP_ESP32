from nicegui import app
from database import get_connection

@app.post('/api/data')
async def receive_data(data: dict):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sensor_data (temperature, humidite, mouvement)
        VALUES (?, ?, ?)
    """, (data['temperature'], data['humidite'], data['mouvement']))

    conn.commit()
    conn.close()

    return {"status": "ok"}

# http://IP_RASPBERRY:8080/api/data