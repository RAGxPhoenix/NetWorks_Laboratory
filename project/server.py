import socket
import threading
import json

accounts_file = 'accounts.json'

def load_accounts():
    try:
        with open(accounts_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_accounts(accounts):
    with open(accounts_file, 'w') as f:
        json.dump(accounts, f, indent=4)

def handle_client(client_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    client_socket.send("Welcome to Python Bank!\n".encode())

    accounts = load_accounts()
    client_socket.send("Do you want to login or register? (login/register): ".encode())
    choice = client_socket.recv(1024).decode().strip()

    client_socket.send("Enter username: ".encode())
    username = client_socket.recv(1024).decode().strip()

    if choice == 'register':
        if username in accounts:
            client_socket.send("Username already exists!\n".encode())
            client_socket.close()
            return
        accounts[username] = {"balance": 0.0, "history": []}
        save_accounts(accounts)
        client_socket.send("Registered successfully.\n".encode())
    elif choice == 'login':
        if username not in accounts:
            client_socket.send("Username does not exist!\n".encode())
            client_socket.close()
            return
        client_socket.send("Logged in successfully.\n".encode())
    else:
        client_socket.send("Invalid choice.\n".encode())
        client_socket.close()
        return

    while True:
        client_socket.send("\nChoose: balance / deposit / withdraw / history / exit: ".encode())
        action = client_socket.recv(1024).decode().strip()

        if action == 'balance':
            balance = accounts[username]['balance']
            client_socket.send(f"Your balance: ₹{balance}\n".encode())

        elif action == 'deposit':
            client_socket.send("Enter amount to deposit: ".encode())
            amt = float(client_socket.recv(1024).decode().strip())
            accounts[username]['balance'] += amt
            accounts[username]['history'].append(f"Deposited ₹{amt}")
            save_accounts(accounts)
            client_socket.send("Amount deposited successfully.\n".encode())

        elif action == 'withdraw':
            client_socket.send("Enter amount to withdraw: ".encode())
            amt = float(client_socket.recv(1024).decode().strip())
            if accounts[username]['balance'] >= amt:
                accounts[username]['balance'] -= amt
                accounts[username]['history'].append(f"Withdrew ₹{amt}")
                save_accounts(accounts)
                client_socket.send("Withdrawal successful.\n".encode())
            else:
                client_socket.send("Insufficient balance.\n".encode())

        elif action == 'history':
            history = "\n".join(accounts[username]['history'])
            client_socket.send(f"Transaction History:\n{history}\n".encode())

        elif action == 'exit':
            client_socket.send("Goodbye!\n".encode())
            break
        else:
            client_socket.send("Invalid action.\n".encode())

    client_socket.close()

# Main Server Code
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12345))
server.listen(5)
print("[STARTED] Server is listening on port 12345")

while True:
    client_socket, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    thread.start()
