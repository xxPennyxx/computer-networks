import socket

def sum(x,y):
    return x+y
def negate(x):
    return -x

host = socket.gethostname()
port = 5000  # initiate port no above 1024
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #SOCK_STREAM for TCP protocol
server_socket.bind((host, port)) #bind the socket to host and port
server_socket.listen(2)#listen only for upto 2 incoming interfaces connected to the server
conn, address = server_socket.accept()  
print("Connected to host",str(address[0]),"@ port",str(address[1])+"!")
while True:
    request = conn.recv(1024).decode()
    #receive the request from the client depending on whether it's a sum or a negate
    if not request:
         break
    #request=str(request)
    #print(request)
    req1=request.split()[0]

    if req1=='sum':
        try:#check if client has entered sum followed by 2 variables, if only one entered then throws error
            x,y=int(request.split()[1]),int(request.split()[2])
            print("Here's what the client requested:")
            print(request)
            ans=sum(x,y)
        except IndexError as x:
            ans="Index Error occurred."
            print(x,"! Oh dear.")
    elif req1=='negate':#if user entered negate followed by 2 variables, by default will take the first 
        x=int(request.split()[1])
        print("Here's what the client requested:")
        print(request)
        ans=negate(x)
    else:
        ans="Wrong input!"

    conn.send(str(ans).encode())  
conn.close() 

