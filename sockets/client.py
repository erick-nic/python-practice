import socket

HOST = "127.0.0.1"
PORT = 65500

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print(f"Client connected to {HOST} : {PORT}")
        try:
            message = input("Enter message to send: ")
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print(f"Returned from server: {data.decode()}")
            client_socket.close()
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    start_client()