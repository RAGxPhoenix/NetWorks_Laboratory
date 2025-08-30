import socket
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl(url, depth):
    if depth <= 0:
        return []
    
    visited = set()
    urls_to_visit = [(url, 0)]
    found_urls = []

    while urls_to_visit:
        current_url, current_depth = urls_to_visit.pop(0)
        if current_url in visited or current_depth > depth:
            continue

        visited.add(current_url)
        try:
            response = requests.get(current_url, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')

            for link in soup.find_all('a', href=True):
                full_url = urljoin(current_url, link['href'])
                if full_url not in visited:
                    urls_to_visit.append((full_url, current_depth + 1))
                    found_urls.append(full_url)
        except requests.exceptions.RequestException:
            continue
    
    return found_urls

def start_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data or data.lower() == 'quit':
            print("Client has disconnected.")
            break

        try:
            url, depth = data.split()
            depth = int(depth)
            urls = crawl(url, depth)
            response = '\n'.join(urls) if urls else "No URLs found."
        except Exception as e:
            response = f"Error: {str(e)}"
        
        conn.send(response.encode())

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()

