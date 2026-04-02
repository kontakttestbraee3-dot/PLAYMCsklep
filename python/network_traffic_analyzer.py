import socket
import struct
import binascii
import time

class NetworkSniffer:
    def __init__(self):
        self.captured_packets = 0
        self.start_time = time.time()
        self.protocols = {6: 'TCP', 17: 'UDP', 1: 'ICMP'}
        self.alert_log = []

    def log_packet(self, proto, src, dst, size):
        timestamp = time.strftime('%H:%M:%S')
        print(f"[{timestamp}] {proto:4} | {src:15} -> {dst:15} | Size: {size} bytes")

    def analyze_payload(self, payload):
        # Symulacja wykrywania złośliwych ciągów znaków (np. SQL Injection)
        suspicious_patterns = [b'SELECT', b'DROP TABLE', b'union select', b'etc/passwd']
        for pattern in suspicious_patterns:
            if pattern in payload.upper():
                return True
        return False

    def simulate_sniffing(self, iterations=20):
        print("\n" + "="*70)
        print("PLAYMC NETWORK ANALYZER v4.2 - KERNEL MODE ACTIVE")
        print("="*70)
        
        mock_ips = ["192.168.1.105", "10.0.0.1", "172.16.254.1", "84.22.11.5"]
        
        for _ in range(iterations):
            self.captured_packets += 1
            src = mock_ips[0] if _ % 3 != 0 else "45.122.10.5"
            dst = "127.0.0.1"
            proto = 6 if _ % 2 == 0 else 17
            size = 64 + (_ * 12)
            
            self.log_packet(self.protocols.get(proto, 'UNK'), src, dst, size)
            
            # Symulacja ataku w 15 iteracji
            if _ == 15:
                print("\n[!!!] ALERT: SUSPICIOUS PAYLOAD DETECTED [!!!]")
                print(f"[REASON] Potential SQL Injection attempt from {src}")
                self.alert_log.append(f"Attack from {src} at {time.time()}")
            
            time.sleep(0.1)

    def generate_statistics(self):
        end_time = time.time()
        duration = end_time - self.start_time
        print("\n" + "-"*40)
        print("SNIFFER SESSION SUMMARY")
        print(f"Total Packets: {self.captured_packets}")
        print(f"Session Time: {duration:.2f}s")
        print(f"Alerts Triggered: {len(self.alert_log)}")
        print(f"PPS (Avg): {self.captured_packets / duration:.1f}")
        print("-"*40 + "\n")

if __name__ == "__main__":
    sniffer = NetworkSniffer()
    sniffer.simulate_sniffing()
    sniffer.generate_statistics()

# NET_STACK: IPV4/IPV6_READY
# CAPTURE_INTERFACE: ETH0
# PROMISCUOUS_MODE: ENABLED
# FILTER: NOT PORT 22
# RAW_SOCKET_ACCESS: TRUE
# LOG_ENCRYPTION: AES-256