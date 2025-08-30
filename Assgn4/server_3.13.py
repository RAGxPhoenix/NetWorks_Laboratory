import socket

def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()
   
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            try:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(a / b)
            except IndexError:
                return "Error: Invalid expression"
   
    return str(stack[-1]) if stack else "Error: Invalid expression"

def server():
    # Get the hostname
    host = 'localhost'
    port = 12347
   
    # Create the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
    # Bind host address and port
    server_socket.bind((host, port))
   
    # Configure listen() function
    server_socket.listen(1)
   
    print("Server listening for incoming connections...")
   
    # Accept a new connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")
   
    while True:
        # Receive the encoded input
        expression = client_socket.recv(1024).decode()
       
        if expression.lower() == 'quit':
            break
       
        # Evaluate the postfix expression
        result = evaluate_postfix(expression)
       
        # Send the result back to the client
        client_socket.sendall(result.encode())
   
    # Close the connection
    client_socket.close()
    server_socket.close()

# Call the server function
server()
