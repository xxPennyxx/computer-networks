import socket


def client_program():
    host = socket.gethostname()  
    port = 12345 
    servaddrport=("10.12.80.199",port)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # instantiate
    #client_socket.connect(servaddrport)  
    msg = ""
    while msg != "Exit":
        msg = input("Client says: ")

        if msg == "Exit":
            client_socket.sendto("Exit".encode(), servaddrport)
            break
    client_socket.sendto(msg.encode(), servaddrport)

    msg, addr = client_socket.recvfrom(1024)
    print("Server says: ", msg.decode())

    client_socket.close()


if __name__ == '__main__':
    client_program()