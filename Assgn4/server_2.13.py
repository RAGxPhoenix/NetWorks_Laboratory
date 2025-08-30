import socket

HOST = '127.0.0.1'
PORT = 65433

def process_message(a):
	m = a.count('1')
	return str(m)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode()
            if not data or data == 'bye':
                break
            result = process_message(data)
            conn.sendall(result.encode())
