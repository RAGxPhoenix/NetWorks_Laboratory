import socket

# RARP Table (MAC → IP)
rarp_table = {
    "AA:BB:CC:DD:EE:01": "192.168.1.101",
    "AA:BB:CC:DD:EE:02": "192.168.1.102",
    "AA:BB:CC:DD:EE:03": "192.168.1.103"
}

# Create UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 12345))  # Bind to all available interfaces on port 12345

print("[SERVER] RARP Server is running and waiting for requests...")

while True:
    try:
        # Receive RARP request
        data, addr = s.recvfrom(1024)
        mac = data.decode().strip()  # Decode MAC address request
        print(f"[RARP REQUEST] Received request for MAC: {mac} from {addr}")

        # Look up MAC in the RARP table
        ip = rarp_table.get(mac, "MAC address not found")

        # Send RARP reply
        s.sendto(ip.encode(), addr)
        print(f"[RARP REPLY] Sent IP: {ip} for MAC: {mac}")

    except Exception as e:
        print(f"[ERROR] {e}")

