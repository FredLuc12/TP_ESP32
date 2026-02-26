CREATE TABLE sensor_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    temperature REAL NOT NULL,
    humidite REAL NOT NULL,
    mouvement BOOLEAN NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);