import socket
import requests

def start_server(host='0.0.0.0', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}...")

    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    url = client_socket.recv(1024).decode()
    print(f"Received URL: {url}")

    try:
        response = requests.get(url)
        if response.status_code == 200:
            client_socket.sendall(response.text.encode())
        else:
            client_socket.sendall(f"Failed to fetch URL, status code: {response.status_code}".encode())
    except Exception as e:
        client_socket.sendall(f"Error fetching URL: {e}".encode())

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()

