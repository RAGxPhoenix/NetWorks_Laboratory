import socket
import pickle  # Use pickle for Python 3.x

# Simulated ARP Table
arp_table = {
    "192.168.1.1": "00:1A:2B:3C:4D:5E",
    "192.168.1.2": "00:1A:2B:3C:4D:5F"
}

def arp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 9999))
    server_socket.listen(5)
    print("ARP Server is running and waiting for connections...")

    while True:
        conn, addr = server_socket.accept()
        print("Connection from", addr)

        # Receive ARP Request
        data = conn.recv(1024)
        if not data:
            conn.close()
            continue
        
        try:
            request = pickle.loads(data)
            ip_address = request.get("ip")

            # Send ARP Reply
            mac_address = arp_table.get(ip_address, "Not Found")
            response = {"ip": ip_address, "mac": mac_address}
            conn.send(pickle.dumps(response))

            print(f"ARP Request for {ip_address}, Reply: {mac_address}")

        except pickle.UnpicklingError:
            print("Error: Invalid data received")

        conn.close()

if __name__ == "__main__":
    arp_server()

