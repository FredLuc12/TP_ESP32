import sqlite3
import os
import hashlib

DB_PATH = "data/suivi4k.db"

def hash_password(password):
    """Hash SHA256 sécurisé."""
    if not password:
        return ""
    return hashlib.sha256(password.encode()).hexdigest()

def get_connection():
    """Connexion à la BDD."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    """Crée toutes les tables."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        prenom TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sensor_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        temperature REAL NOT NULL,
        humidite REAL NOT NULL,
        mouvement INTEGER NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS thresholds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        temp_max REAL DEFAULT 28.0,
        humidite_max REAL DEFAULT 75.0,
        mouvement_actif INTEGER DEFAULT 1,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sensor_data_id INTEGER,
        type_alerte TEXT,
        message TEXT,
        sent INTEGER DEFAULT 0,
        resolved INTEGER DEFAULT 0,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(sensor_data_id) REFERENCES sensor_data(id)
    )
    """)

    conn.commit()
    conn.close()
    print(" Tables créées")

def insert_test_data():
    """Données de test."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # User test : jean.dupont@email.com / password123
    password_hash = hash_password('password123')
    cursor.execute("""
        INSERT OR REPLACE INTO users (nom, prenom, email, password_hash)
        VALUES (?, ?, ?, ?)
    """, ('DUPONT', 'Jean', 'jean.dupont@email.com', password_hash))
    
    cursor.execute("INSERT OR IGNORE INTO thresholds (id, temp_max, humidite_max, mouvement_actif) VALUES (1, 28.0, 75.0, 1)")
    cursor.execute("INSERT INTO sensor_data (temperature, humidite, mouvement) VALUES (24.5, 68.0, 1)")
    
    # Données capteurs (pour FK)
    cursor.execute("INSERT INTO sensor_data (temperature, humidite, mouvement) VALUES (24.5, 68.0, 1)")
    sensor_id1 = cursor.lastrowid
    cursor.execute("INSERT INTO sensor_data (temperature, humidite, mouvement) VALUES (29.5, 78.0, 0)")  # Alerte temp+humid
    sensor_id2 = cursor.lastrowid
    cursor.execute("INSERT INTO sensor_data (temperature, humidite, mouvement) VALUES (25.0, 70.0, 1)")
    sensor_id3 = cursor.lastrowid
    
    # 3 ALERTES TEST
    cursor.execute("""
        INSERT INTO alerts (sensor_data_id, type_alerte, message, sent, resolved) 
        VALUES (?, 'temperature', 'Température dépasse 28°C : 29.5°C', 1, 0)
    """, (sensor_id2,))
    
    cursor.execute("""
        INSERT INTO alerts (sensor_data_id, type_alerte, message, sent, resolved) 
        VALUES (?, 'humidite', 'Humidité dépasse 75% : 78%', 1, 1)
    """, (sensor_id2,))
    
    cursor.execute("""
        INSERT INTO alerts (sensor_data_id, type_alerte, message, sent, resolved) 
        VALUES (?, 'mouvement', 'Mouvement détecté - zone sécurisée', 1, 1)
    """, (sensor_id1,))
    conn.commit()
    conn.close()
    print(" User créé : jean.dupont@email.com / password123")
    print("Seuils + capteurs + 3 alertes test insérés")

if __name__ == "__main__":
    create_tables()
    insert_test_data()
