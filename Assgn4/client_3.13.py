import socket

def client():
    # Get the hostname
    host = 'localhost'
    port = 12347
   
    # Create the client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
    # Connect the client socket to the server
    client_socket.connect((host, port))
   
    while True:
        # Take input from user
        expression = input("Enter a postfix expression (or 'Quit' to exit): ")
       
        if expression.lower() == 'quit':
            client_socket.sendall(expression.encode())
            break
       
        # Send the encoded input to the server
        client_socket.sendall(expression.encode())
       
        # Receive the result from the server
        result = client_socket.recv(1024).decode()
       
        # Print the result
        print(f"Result of the postfix expression: {result}")
   
    # Close the connection
    client_socket.close()


client()

