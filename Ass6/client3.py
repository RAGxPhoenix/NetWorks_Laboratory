import socket

def udp_client():
    host = "127.0.0.1"
    port = 12347
    server_address = (host, port)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = input("Enter binary string (type 'Quit' to exit): ")
        client_socket.sendto(message.encode(), server_address)

        if message.lower() == "quit":
            print("Exiting client...")
            break

        data, _ = client_socket.recvfrom(1024)
        print(f"Server response: Number of 1s = {data.decode()}")

    client_socket.close()

udp_client()
