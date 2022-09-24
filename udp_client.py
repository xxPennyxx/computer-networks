import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverAddressPort = ("10.12.80.199", 12345) # Found the address from the server socket beforehand

msg = ""
while msg != "Bye":
    msg = input("Client: ")

    if msg == "Bye":
        client_socket.sendto("Bye".encode(), serverAddressPort)
        break
    client_socket.sendto(msg.encode(), serverAddressPort)

    msg, addr = client_socket.recvfrom(1024)
    msg = msg.decode()
    print(f"Server {addr}: ", msg)

client_socket.close()