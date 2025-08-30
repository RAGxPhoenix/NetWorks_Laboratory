import socket
import pickle  # Use pickle for Python 3

def arp_client(ip_address):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 9999))

    # Send ARP Request
    request = {"ip": ip_address}
    client_socket.send(pickle.dumps(request))

    # Receive ARP Reply
    response = pickle.loads(client_socket.recv(1024))
    print("ARP Response:", response)

    client_socket.close()

if __name__ == "__main__":
    ip = input("Enter IP Address to resolve MAC: ")  # Use input() instead of raw_input()
    arp_client(ip)

