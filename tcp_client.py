import socket

def tcp_client(host='localhost', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        with open('desktop/4310programmingassignment/input.txt', 'rb') as f:
            while (chunk := f.read(1024)):
                client_socket.sendall(chunk)
        print('File sent successfully.')

        confirmation = client_socket.recv(1024).decode()
        print('Server confirmation:', confirmation)

if __name__ == "__main__":
    tcp_client()

