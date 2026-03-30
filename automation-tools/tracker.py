import json
import os
import requests # Biblioteka do pobierania IP z sieci
from datetime import datetime

# Ścieżka zgodna z Twoim wymaganiem
LOG_PATH = "logs/log.json"

def get_public_ip():
    """Pobiera prawdziwy publiczny adres IP użytkownika"""
    try:
        # Używamy zewnętrznego API, żeby dostać prawdziwe IP, a nie lokalne 127.0.0.1
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        return response.json()['ip']
    except Exception:
        return "127.0.0.1 (Error fetching IP)"

def record_transaction(item_name, price):
    """Zapisuje realną transakcję do bazy log.json"""
    
    # Tworzenie folderu logs jeśli go nie ma
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Pobieranie danych
    current_ip = get_public_ip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_log = {
        "event_id": os.urandom(4).hex(), # Generuje unikalne ID transakcji
        "time": timestamp,
        "user_ip": current_ip,
        "product": item_name,
        "amount_pln": float(price),
        "status": "SUCCESS"
    }

    # Obsługa pliku JSON
    logs_data = []
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            try:
                logs_data = json.load(f)
            except json.JSONDecodeError:
                logs_data = []

    # Dodanie wpisu
    logs_data.append(new_log)

    # Zapis z ładnym formatowaniem (indent=4)
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(logs_data, f, indent=4, ensure_ascii=False)

    print(f"--- LOG SYSTEM ---")
    print(f"Zapisano zdarzenie: {item_name}")
    print(f"Adres IP: {current_ip}")
    print(f"Lokalizacja: {LOG_PATH}")

# Uruchomienie zapisu (Przykład dla Miecz S4 U3)
if __name__ == "__main__":
    # Możesz to wywołać z dowolnymi danymi
    record_transaction("Miecz S4 U3", 12.00)