import requests

def send_make_webhook(capteur_type, valeur, seuil, message):
    webhook_url = "https://hook.eu1.make.com/y5skp23xpqt5g200bp2ikorbapk5sjob"

    payload = {
        "secret_key": "SUIVI4K_2026",
        "alerte": {
            "type": capteur_type,
            "valeur": float(valeur),
            "seuil": float(seuil),
            "unite": "°C" if capteur_type == "temperature" else "%" if capteur_type == "humidite" else "",
            "message": message,
        }
    }
    try:
        requests.post(webhook_url, json=payload, timeout=5)
        return True
    except:
        return False