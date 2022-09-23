#include<stdio.h>
#include<stdio.h>
#include<netinet/in.h>
#include<stdlib.h>
#include<string.h>
#include<sys/socket.h>
#include<sys/types.h>
#define MAX 80


void func(int connfd){
    char buff[MAX];
    int n;
    for(;;){
        bzero(buff,MAX);
        
    }
}
int main()

{
    int sockfd,connfd,len;
    struct sockaddr_in servaddr,cli;
    sockfd=socket(AF_INET,SOCK_STREAM,0);
    if (sockfd==-1){ printf("HUIQWHUIQI");
    exit(0);}
    else
    printf("connected");
    bzero(&servaddr,sizeof(servaddr));
    servaddr.sin_family=AF_INET;
    servaddr.sin_addr.s_addr=htonl(INADDR_ANY)
    servaddr.sin_port=htons(PORT);
    
    if((bind(sockfd,(SA*)&servaddr,sizeof(servaddr)))!=0){
        printf("BIND FAILED");
        exit(0);
    }
    else{
        printf("YEYEYEY");
    }
    
    if((listen(sockfd,5))!=0){
         printf("listen FAILED");
        exit(0);
        
    }
    else{
        printf("YEYEYEY");}
        len=sizeof(cli);
        connfd=accept(sockfd,(SA*)&cli,&len);
        if(connfd<0){
            printf("Conn failed");
            exit(0);
        }
        else{
            printf("Server accept client!");
        }
        func(connfd);
        close(sockfd);
        return 0;
}
