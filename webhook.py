import requests

def send_alert_to_make(data):
    webhook_url = "y5skp23xpqt5g200bp2ikorbapk5sjob@hook.eu1.make.com"

    payload = {
        "secret_key": "SUIVI4K_2026",
        "temperature": data["temperature"],
        "humidite": data["humidite"],
        "mouvement": data["mouvement"],
        "date": data["created_at"],
        "message": data["message"]
    }

    requests.post(webhook_url, json=payload)