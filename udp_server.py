import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind((socket.gethostname(), 12345))
print("Server listening")

msg, client_address = server_socket.recvfrom(1024)
msg = msg.decode()
print(f"Client ({client_address}): ", msg)

while msg != "Bye":
    msg = input("Server: ")

    if msg == "Bye":
        server_socket.sendto("Bye".encode(), client_address)
        break
    server_socket.sendto(msg.encode(), client_address)

    msg, addr = server_socket.recvfrom(1024)
    msg = msg.decode()
    print(f"Client {addr}: ", msg)
server_socket.close()