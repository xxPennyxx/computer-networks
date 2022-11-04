import socket
def Client():
    host = socket.gethostname()  
    port = 5000  
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client_socket.connect((host, port))  
    req=input("Enter 'sum x y' to find sum, or 'negate x' to find negative of a number.\nEnter 'bye' to quit\n")
    while req!='bye':
        client_socket.send(req.encode())#sends request prompt to the server  
        data = client_socket.recv(1024).decode() #receive result from the server
        print("The result is:")
        print(data)
        req=input("Enter 'sum x y' to find sum, or 'negate x' to find negative of a number\n")

    client_socket.close()  


if __name__ == '__main__':
    Client()