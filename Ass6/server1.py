import socket

def udp_server():
    host = "127.0.0.1"  # Localhost
    port = 12345  # Server port

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f"Server listening on {host}:{port}...")

    while True:
        data, addr = server_socket.recvfrom(1024)  # Receive message
        message = data.decode()
        print(f"Received from {addr}: {message}")

        if message.lower() == "bye":
            print("Client disconnected. Exiting...")
            break

    server_socket.close()

udp_server()
