import socket

def start_client(host='127.0.0.1', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    while True:
        n = input("Enter a string (or 'Quit' to exit): ")
        client_socket.sendall(n.encode())

        if n.lower() == 'quit':
            break

        response = client_socket.recv(1024).decode()
        print(f"Server Response: {response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()

