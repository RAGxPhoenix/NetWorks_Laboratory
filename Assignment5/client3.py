import socket

def start_client(host='127.0.0.1', port=12345, output_file="crawled_urls.txt"):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        url = input("Enter URL (or 'Quit' to exit): ")
        if url.lower() == 'quit':
            client_socket.sendall(url.encode())
            break

        depth = input("Enter crawl depth: ")
        message = f"{url} {depth}"
        client_socket.sendall(message.encode())

        response = client_socket.recv(4096).decode()
        print(f"Server Response:\n{response}")

        with open(output_file, "w") as file:
            file.write(response)

        print(f"Results saved to {output_file}")

    client_socket.close()

if __name__ == "__main__":
    start_client()

