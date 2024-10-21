import socket

def udp_server(host='localhost', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f'UDP Server listening on {host}:{port}')

        buffer = []
        while True:
            data, addr = server_socket.recvfrom(1024)
            if data == b'END':
                break
            buffer.append(data)
        
        with open('received_file.txt', 'wb') as f:
            for chunk in buffer:
                f.write(chunk)
        
        print('File received successfully.')
        server_socket.sendto(b'File received successfully.', addr)

if __name__ == "__main__":
    udp_server()

