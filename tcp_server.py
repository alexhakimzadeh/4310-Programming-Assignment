import socket

def tcp_server(host='localhost', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f'TCP Server listening on {host}:{port}')

        conn, addr = server_socket.accept()
        with conn:
            print(f'Connected by {addr}')
            with open('received_file.txt', 'wb') as f:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)
            print('File received successfully.')
            conn.sendall(b'File received successfully.')

if __name__ == "__main__":
    tcp_server()