import socket

def rarp_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("127.0.0.1", 12345)  # Use localhost (same as server)

    while True:
        try:
            mac = input("Enter MAC address (or 'exit' to quit): ").strip()
            if mac.lower() == "exit":
                print("Exiting RARP Client.")
                break

            # Send RARP request
            s.sendto(mac.encode(), server_address)

            # Receive RARP reply
            data, _ = s.recvfrom(1024)
            print("Received RARP reply:", data.decode())

        except ConnectionError:
            print("[ERROR] Server is unavailable. Please check if it is running.")
            break
        except Exception as e:
            print(f"[ERROR] {e}")
            break

    s.close()  # Close socket when done

if __name__ == "__main__":
    rarp_client()

