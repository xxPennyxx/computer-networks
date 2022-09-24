#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include<stdlib.h>

int main(void){
    int sockdesc;
    struct sockaddr_in server_addr;
    char servermsg[2000], climsg[2000];
    int l = sizeof(server_addr);

    // Reset buffers
    memset(servermsg, '\0', sizeof(servermsg));
    memset(climsg, '\0', sizeof(climsg));

    // Create socket
    sockdesc = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);

    if(sockdesc < 0){
        printf("Error while creating socket\n");
        exit(0);
    }
    else
    printf("Socket created successfully\n");

    // Set port and IP:
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(2000);
    server_addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    // Get input from the user:
    while(1){
    printf("Enter message: ");
    gets(climsg);

    // Send the message to server:
    if(sendto(sockdesc, climsg, strlen(climsg), 0,
         (struct sockaddr*)&server_addr, l) < 0){
        printf("Unable to send message\n");
        exit(0);
    }

    // Receive the server's response:
    if(recvfrom(sockdesc, servermsg, sizeof(servermsg), 0,
         (struct sockaddr*)&server_addr, &l) < 0){
        printf("Error while receiving server's message\n");
        exit(0);
    }
    else
    printf("Server's response: %s\n", servermsg);
        if (strncmp("exit", servermsg, 4) == 0) {
                        printf("Server Exit...\n");
                        break;


    }

    // Close the socket:
    close(sockdesc);

    return 0;
}
