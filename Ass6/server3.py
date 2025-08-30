import socket

def count_ones(binary_string):
    return binary_string.count("1")

def udp_server():
    host = "127.0.0.1"
    port = 12347

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f"Server listening on {host}:{port}...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        message = data.decode()

        if message.lower() == "quit":
            print("Client disconnected. Exiting...")
            break

        num_ones = count_ones(message)
        server_socket.sendto(str(num_ones).encode(), addr)

    server_socket.close()

udp_server()
