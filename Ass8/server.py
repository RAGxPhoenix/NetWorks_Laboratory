import socket
import threading

clients = []
def handle_client(client_socket):
    clients.append(client_socket)
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')

            if not message or message.lower() == 'exit':
                print("Client disconnected")
                break

            print(f"Received from client: {message}")
            for client in clients:
                try:
                    client.send(f"Message from server: {message}".encode('utf-8'))
                except:
                    clients.remove(client)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        clients.remove(client_socket)
        client_socket.close()

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"New connection from {client_address}")

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    host = '127.0.0.1'
    port = 12345

    start_server(host, port)
