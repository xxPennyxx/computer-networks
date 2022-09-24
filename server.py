import socket

def server_program():
    host = socket.gethostname()
    port = 12345  # initiate port no above 1024
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    server_socket.bind((host, port))  
    print("Server listening...")
    msg,cliaddr = server_socket.recvfrom(1024)
    print(f"Client ({cliaddr}) says:",msg.decode())
    while msg != "Exit":
        msg = input("Server says: ")
        if msg == "Exit":
            server_socket.sendto("Bye".encode(), cliaddr)
            break
        server_socket.sendto(msg.encode(), cliaddr)

    msg,addr = server_socket.recvfrom(1024)
    print(f"Client ({addr}) says:",msg.decode())   


if __name__ == '__main__':
    server_program()