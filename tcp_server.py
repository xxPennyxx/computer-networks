import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((socket.gethostname(), 12345))

server_socket.listen(5)

print("Server socket is listening")

(connection, address) = server_socket.accept()
print(f"Connection from: {address}")

start_conversation = input("Start conversation? (y/n)")
if start_conversation.lower() == "n":
    connection.send("Bye".encode())
    connection.close()
    server_socket.close()
    exit(0)

msg = connection.recv(1024).decode()

print("Client: ", msg)

while msg != "Bye":
    msg = input("Server: ")

    if msg == "Bye":
        connection.send("Bye".encode())
        break
    connection.send(msg.encode())

    msg = connection.recv(1024).decode()
    print("Client: ", msg)
connection.close()
server_socket.close()

