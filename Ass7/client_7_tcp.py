import socket
host = 'localhost'
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
message = input("Enter message in binary bits: ")
s.send(message.encode())
data = s.recv(1024).decode()
q, r, crc_value = data.split(',')
print("Quotient:", q)
print("Remainder:", r)
print("CRC value:", crc_value)
s.close()


