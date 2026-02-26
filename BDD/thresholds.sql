CREATE TABLE thresholds (
    id INTEGER PRIMARY KEY,
    temp_max REAL,
    humidite_max REAL,
    mouvement_actif BOOLEAN,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);