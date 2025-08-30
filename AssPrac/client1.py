import socket

def start_client(server_ip='127.0.0.1', port=12345, url="http://example.com"):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))
    client_socket.send(url.encode())

    data = b""
    while True:
        chunk = client_socket.recv(4096)
        if not chunk:
            break
        data += chunk

    with open("downloaded_page.html", "wb") as file:
        file.write(data)

    print("Webpage downloaded as 'downloaded_page.html'")
    client_socket.close()

if __name__ == "__main__":
    url = input("Enter the URL to fetch: ")
    start_client(url=url)

