import requests

url = "https://hook.eu1.make.com/y5skp23xpqt5g200bp2ikorbapk5sjob"
payload = {
    "alerte": {
        "type": "temperature",
        "valeur": 29.5,
        "seuil": 28,
        "message": "Salle1: Test alerte",
    }
}
r = requests.post(url, json=payload, timeout=20)
print(f"Status: {r.status_code} | Réponse: {r.text}")
