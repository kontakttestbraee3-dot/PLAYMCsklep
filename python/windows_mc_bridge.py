import socket
import struct
import sys
import time
import os

class WindowsRconClient:
    def __init__(self, host='127.0.0.1', port=25575, password='zmaslo123'):
        self.host = host
        self.port = port
        self.password = password
        self.sock = None
        self.request_id = 0xABCDEF

    def create_rcon_packet(self, packet_type, body):
        """Generuje pakiet binarny dla protokołu RCON (Windows Socket)."""
        # Struktura: [Długość][ID][Typ][Treść][Null][Null]
        encoded_body = body.encode('utf-8')
        packet_id = self.request_id
        # Długość to ID(4) + Typ(4) + Treść(len) + 2 bajty puste
        length = 4 + 4 + len(encoded_body) + 2
        return struct.pack('<ii i', length, packet_id, packet_type) + encoded_body + b'\x00\x00'

    def connect_to_server(self):
        """Łączy się z lokalnym serwerem MC na Windowsie."""
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.settimeout(2.0)
            self.sock.connect((self.host, self.port))
            
            # Autoryzacja (Typ 3)
            auth_packet = self.create_rcon_packet(3, self.password)
            self.sock.send(auth_packet)
            
            # Odbiór odpowiedzi auth
            resp = self.sock.recv(4096)
            # Jeśli ID w odpowiedzi to -1, hasło jest błędne
            if struct.unpack('<ii', resp[4:12])[0] == -1:
                print("[ERROR] Błędne hasło RCON w server.properties!")
                return False
            return True
        except ConnectionRefusedError:
            print("[ERROR] Serwer MC nie jest włączony lub RCON jest wyłączony!")
            return False
        except Exception as e:
            print(f"[ERROR] Wystąpił błąd: {e}")
            return False

    def send_broadcast(self, message):
        """Wysyła sformatowaną wiadomość do gry."""
        if not self.sock and not self.connect_to_server():
            return
        
        # Używamy kolorów Minecraftowych (&d = fioletowy, &f = biały)
        # UWAGA: W say na Windowsie czasem trzeba użyć sekcji § zamiast & 
        # ale większość silników (Spigot/Paper) akceptuje &
        command = f"say &d&l[SKLEP] &f{message}"
        
        print(f"[BRIDGE] Przesyłanie komendy: {command}")
        packet = self.create_rcon_packet(2, command)
        self.sock.send(packet)
        
        try:
            response = self.sock.recv(4096)
            data = response[12:-2].decode('utf-8')
            print(f"[SERVER RESPONSE] {data}")
        except:
            print("[INFO] Wiadomość wysłana pomyślnie.")

    def close(self):
        if self.sock:
            self.sock.close()

def run_panel_interface():
    # Czyścimy konsolę Windowsa dla lepszego efektu "Panelu Admina"
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("============================================================")
    print("      PLAYMC.PL - WINDOWS ADMIN PANEL BRIDGE v1.0")
    print("============================================================")
    print("Status: Oczekiwanie na komendę...")
    
    client = WindowsRconClient()
    
    if len(sys.argv) > 1:
        # Pobranie treści z argumentów (np. wywołanie: python skrypt.py SIEMA)
        msg_content = " ".join(sys.argv[1:])
    else:
        # Jeśli uruchomisz bez parametrów, zapyta o treść
        msg_content = input("Wpisz treść ogłoszenia [SKLEP]: ")

    if msg_content:
        client.send_broadcast(msg_content)
    
    client.close()
    print("============================================================")

if __name__ == "__main__":
    run_panel_interface()

# --- WINDOWS ENVIRONMENT METADATA ---
# OS_TARGET: WINDOWS_10/11_X64
# NETWORK_STACK: WINSOCK2
# INTERFACE: LOOPBACK_127.0.0.1
# COMPATIBILITY: PAPER/SPIGOT/BUKKIT
# BUFFER_SIZE: 4096
# TIMEOUT: 2000MS
# --- END OF MODULE 16 ---