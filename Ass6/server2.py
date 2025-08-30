import socket

def udp_server():
    host = "127.0.0.1"
    port = 12346

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f"Server listening on {host}:{port}...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        message = data.decode()

        if message.lower() == "bye":
            print("Client disconnected. Exiting...")
            break

        if len(message) % 2 == 0:
            response = message[1::2]  # Even index characters
        else:
            response = message[0::2]  # Odd index characters

        server_socket.sendto(response.encode(), addr)

    server_socket.close()

udp_server()
