import socket

def udp_client():
    host = "127.0.0.1"
    port = 12345
    server_address = (host, port)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = input("Enter message (type 'bye' to exit): ")
        client_socket.sendto(message.encode(), server_address)

        if message.lower() == "bye":
            print("Exiting client...")
            break

    client_socket.close()

udp_client()
