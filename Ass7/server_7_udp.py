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
divisor = "1101"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
data, client_addr = s.recvfrom(1024)
message = data.decode()
print("Message (dividend):", message)
print("Divisor:", divisor)
appended = message + "0"*(len(divisor)-1)
print("Appended Dividend:", appended)
q, r, crc_value = crc(message, divisor)
print("Quotient:", q)
print("Remainder:", r)
print("CRC value:", crc_value)
s.sendto(f"{q},{r},{crc_value}".encode(), client_addr)
s.close()


