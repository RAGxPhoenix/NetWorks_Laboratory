import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Enter server IP address: ")  # e.g., '127.0.0.1' or '192.168.1.x'
port = 12345

try:
    client.connect((host, port))
except Exception as e:
    print("Connection error:", e)
    exit()

while True:
    try:
        message = client.recv(1024).decode()
        if not message:
            break
        print(message, end='')
        if "Goodbye" in message:
            break
        inp = input()
        client.send(inp.encode())
    except:
        print("Server disconnected.")
        break

client.close()
