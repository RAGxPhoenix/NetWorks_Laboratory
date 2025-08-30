import socket

host = 'localhost'
port = 12345

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# Get user input
message = input("Enter message in binary bits (dividend): ")
divisor = input("Enter divisor in binary bits: ")

# Send both message and divisor, separated by comma
s.send(f"{message},{divisor}".encode())

# Receive result
data = s.recv(1024).decode()
q, r, crc_value = data.split(',')
print("Quotient:", q)
print("Remainder:", r)
print("CRC value:", crc_value)

s.close()

