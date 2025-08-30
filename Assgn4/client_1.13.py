import socket

HOST = '127.0.0.1'
PORT = 65433

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input("Enter message to send (or type 'bye' to quit): ")
        s.sendall(message.encode())
        if message == 'bye':
            break
        data = s.recv(1024).decode()
        print('Received:', data)
