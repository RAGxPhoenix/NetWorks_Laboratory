import socket

host = 'localhost'
port = 12345

# Create UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Get user inputs
message = input("Enter message in binary bits (dividend): ")
divisor = input("Enter divisor in binary bits: ")

# Send both message and divisor separated by comma
s.sendto(f"{message},{divisor}".encode(), (host, port))

# Receive response
data, addr = s.recvfrom(1024)
q, r, crc_value = data.decode().split(',')
print("Quotient:", q)
print("Remainder:", r)
print("CRC value:", crc_value)

s.close()

