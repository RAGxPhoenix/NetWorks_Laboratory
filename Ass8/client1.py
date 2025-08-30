import socket
import threading

def listen_for_messages(client_socket):
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received from server: {message}")
            else:
                break
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def send_message_to_server(client_socket):
    try:
        while True:
            message = input("Enter message to send to the server (or 'exit' to disconnect): ")

            if message.lower() == 'exit':
                print("Disconnecting from server...")
                client_socket.send(message.encode('utf-8'))
                break  
            client_socket.send(message.encode('utf-8'))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((host, port))

    listen_thread = threading.Thread(target=listen_for_messages, args=(client_socket,))
    listen_thread.daemon = True 
    listen_thread.start()

    send_message_to_server(client_socket)

if __name__ == "__main__":
    host = '127.0.0.1'
    port = 12345 

    start_client(host, port)

