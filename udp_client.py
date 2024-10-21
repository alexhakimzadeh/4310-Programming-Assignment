import socket

def udp_client(host='localhost', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        with open('desktop/4310programmingassignment/input.txt', 'rb') as f:
            while (chunk := f.read(1024)):
                client_socket.sendto(chunk, (host, port))
        client_socket.sendto(b'END', (host, port))
        print('File sent successfully.')

        confirmation, _ = client_socket.recvfrom(1024)
        print('Server confirmation:', confirmation.decode())

if __name__ == "__main__":
    udp_client()

