import socket

def udp_client():
    host = "127.0.0.1"
    port = 12346
    server_address = (host, port)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = input("Enter message (type 'bye' to exit): ")
        client_socket.sendto(message.encode(), server_address)

        if message.lower() == "bye":
            print("Exiting client...")
            break

        data, _ = client_socket.recvfrom(1024)
        print(f"Server response: {data.decode()}")

    client_socket.close()

udp_client()

