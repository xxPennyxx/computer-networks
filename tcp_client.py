import socket

client_socket = socket.socket()

port = 12345
client_socket.connect((socket.gethostname(), 12345))
print("Connection established")

msg = ""
while msg != "Bye":
    msg = input("Client: ")

    if msg == "Bye":
        client_socket.send("Bye".encode())
        break
    client_socket.send(msg.encode())

    msg = client_socket.recv(1024).decode()
    print("Server: ", msg)

client_socket.close()