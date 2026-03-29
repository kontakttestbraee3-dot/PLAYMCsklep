import time

def check_payments():
    print("Sprawdzanie nowych wpłat na PayPal.me/xIWOJTEKIxMinecraft...")
    # Tutaj w przyszłości będzie integracja z API PayPala
    time.sleep(2)
    print("Brak nowych wpłat. Oczekiwanie...")

if __name__ == "__main__":
    while True:
        check_payments()
        time.sleep(60) # Sprawdzaj co minutę