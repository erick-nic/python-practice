import socket

HOST = "127.0.0.1"
PORT = 65500

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server started at {HOST} : {PORT}")
        try:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                print(f"Received from client: {data.decode()}")
                response = "Successfuly received"
                conn.sendall(response.encode())
                server_socket.close()
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    start_server()