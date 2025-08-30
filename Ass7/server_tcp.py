import socket

def crc(dividend, divisor):
    m = len(divisor)
    appended = dividend + "0"*(m-1)
    dividend_list = list(appended)
    quotient = ""
    for i in range(len(dividend)):
        if dividend_list[i] == '1':
            quotient += '1'
            for j in range(m):
                dividend_list[i+j] = str(int(dividend_list[i+j] != divisor[j]))
        else:
            quotient += '0'
    remainder = "".join(dividend_list[-(m-1):])
    crc_value = dividend + remainder
    return quotient, remainder, crc_value

host = 'localhost'
port = 12345

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

print("Server listening...")

conn, addr = s.accept()
print(f"Connected by {addr}")

# Receive message and divisor
data = conn.recv(1024).decode()
message, divisor = data.split(',')
print("Message (dividend):", message)
print("Divisor:", divisor)

# Perform CRC
q, r, crc_value = crc(message, divisor)
print("Quotient:", q)
print("Remainder:", r)
print("CRC value:", crc_value)

# Send result back
conn.send(f"{q},{r},{crc_value}".encode())

conn.close()
s.close()

