CREATE TABLE alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_data_id INTEGER,
    type_alerte TEXT NOT NULL,
    message TEXT NOT NULL,
    sent BOOLEAN DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(sensor_data_id) REFERENCES sensor_data(id)
    resolved BOOLEAN DEFAULT 0
);