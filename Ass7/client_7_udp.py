import socket
host = 'localhost'
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input("Enter message in binary bits: ")
s.sendto(message.encode(), (host, port))
data, addr = s.recvfrom(1024)
q, r, crc_value = data.decode().split(',')
print("Quotient:", q)
print("Remainder:", r)
print("CRC value:", crc_value)
s.close()


