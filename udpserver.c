#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include<stdlib.h>
int main()
{
    int sockdesc;
    struct sockaddr_in servaddr, cliaddr;
    char servermsg[2000], climsg[2000];
    int len = sizeof(cliaddr);
    //reset buffers
     memset(servermsg, '\0', sizeof(servermsg));
    memset(climsg, '\0', sizeof(climsg));
    
    // Create UDP socket
    sockdesc = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    if(sockdesc < 0)
    {
        printf("ERROR while creating socket\n");
        exit(0);
    }
    else
    printf("Socket created successfully!\n");
    
    // Set port and IP
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(2000);
    servaddr.sin_addr.s_addr = inet_addr("127.0.0.1");
    
    // Bind to the set port and IP
    if(bind(sockdesc, (struct sockaddr*)&servaddr, sizeof(servaddr)) < 0)
    {
        printf("Binding failed:/\n");
        exit(0);
    }
    else 
    printf("Done with binding\n");
    
     // Receive client's message
     
    if (recvfrom(sockdesc, climsg, sizeof(climsg), 0,
         (struct sockaddr*)&cliaddr, &len) < 0)
         {
        printf("Couldn't receive message:/\n");
        exit(0);
    }
    printf("Received message from IP: %s and port: %i\n",
           inet_ntoa(cliaddr.sin_addr), ntohs(cliaddr.sin_port));
    
    printf("Message from client: %s\n", climsg);
    
    // Respond to client
    strcpy(servermsg, climsg);
    
    if (sendto(sockdesc, servermsg, strlen(servermsg), 0,
         (struct sockaddr*)&cliaddr, len) < 0)
         {
        printf("Can't send message :/\n");
        exit(0);
    }
    
    // Close socket
    close(sockdesc);
    return 0;
}
