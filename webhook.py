import requests

def send_alert_to_make(data):
    webhook_url = "https://hook.make.com/TON_WEBHOOK"

    payload = {
        "temperature": data["temperature"],
        "humidite": data["humidite"],
        "mouvement": data["mouvement"],
        "date": data["created_at"],
        "message": data["message"]
    }

    requests.post(webhook_url, json=payload)