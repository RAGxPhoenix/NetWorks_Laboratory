import socket

def start_client(host='127.0.0.1', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    while True:
        user_input = input("Enter a string (or 'Quit' to exit): ")
        client_socket.sendall(user_input.encode())

        if user_input.lower() == 'quit':
            break

        response = client_socket.recv(1024).decode()
        print(f"Server Response (Reversed): {response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()

