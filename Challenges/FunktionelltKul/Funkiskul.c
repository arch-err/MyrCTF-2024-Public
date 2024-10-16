#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <pthread.h>
#include <time.h>

#define PORT 1337
#define BUFFER_SIZE 16

_Thread_local int socketinfo = 0;


void send_data(int sock, const char *data) {
    send(sock, data, strlen(data), 0);
}

int Introduction(int socket) {
    send_data(socket, "\nVälkommen!\n\n");
}
int Joke(int socket) {
    int r = rand() % 5; // Number between 0 -> 4
    switch(r) {
        case 0:
            send_data(socket, "-----\n\nVad kallar du en läkare utan humor?\n\nLäkare.\n\n-----");
            break;
        case 1:
            send_data(socket, "-----\n\nKlarar man det inte på tredje försöket är man dum i huvudet - Mor\n\n-----");
            break;
        case 2:
            send_data(socket, "-----\n\nDet som inte knäcker nötterna är inte värt att göra\n\n-----");
            break;
        case 3:
            send_data(socket, "-----\n\nDenna utmaningen är lätt.\n\n-----");
            break;
        case 4:
            send_data(socket, "-----\n\nSpiller du ut julmust blir det en skum stämning\n\n-----");
            break;
        default: 
            send_data(socket, "-----\n\nTvå bagare, en smet. Hur många bagare är kvar?\n\n-----");
            break;
    return 0;
    }
}
int Win() {

    send_data(socketinfo, "MyrCTF{dIffiCulTy_eAsy_gL4d_sMil3y}");
    return 0;
}

int Menu(int socket) {
        send_data(socket, "\nDina val\n\n1. Printa ett skämt eller citat\n2. Printa flaggan\n3. ???\n4. Exit\n");

    char input[4];
    int res = recv(socket, input, sizeof(input) - 1, 0);

    if (res <= 0) {
        return -1; // Error or disconnect
    }

    input[res] = '\0'; // Null-terminate the received data

    int option = atoi(input); // Convert the input to an integer

    if (option < 1 || option > 4) {
        send_data(socket, "ERROR!!!!\n");
        return Menu(socket); // Recursively ask for input again
    }

    return option;
}

int MysteriousDataEntry(int socket) {
    char buffer[512];
    send_data(socket, "\nHar du ett skämt för mig?\nBerätta: ");
    recv(socket, buffer, 528, 0); // Recieve data, but not enough for shell.
    send_data(socket, "\nLåt mig fundera...\n");
    return 0;
}
int mainprogram(int socket) {
    srand(time(NULL));
    Introduction(socket);
    while (1) {
        int menu = Menu(socket);
        if (menu == -1) {
            break;
        }

        switch (menu) {
            case 1:
                Joke(socket);
                break;
            case 2:
                void (*winptr) = &Win;
                char str[20];
                sprintf(str, "%p", winptr);
                send_data(socket, str);
                break;
            case 3:
                MysteriousDataEntry(socket);
                send_data(socket, "\nTråkigt skämt :/");
                break;
            case 4:
                send_data(socket, "\nOkej då.");
                return 1;
                break;
            default:
                send_data(socket, "\nhuh?");
                
                break;
            
        }
    }
    return 0;

}
void *client_handler(void *socket_desc) {
    int sock = *(int*)socket_desc;
    socketinfo = (int)(long)sock;
    mainprogram(sock);

    close(sock);
    //free(socketinfo);
    free(socket_desc);
    pthread_exit(NULL);
}

int main() {
    int server_fd, new_socket, *new_sock;
    struct sockaddr_in address;
    int addrlen = sizeof(address);

    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("Socket failed");
        exit(EXIT_FAILURE);
    }
    int option = 1;
    setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &option, sizeof(option));
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }

    if (listen(server_fd, 3) < 0) {
        perror("Listen Failed");
        exit(EXIT_FAILURE);
    }

    puts("Awaiting Connections");

    

    while (1) {
        new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t *)&addrlen);
        if (new_socket < 0) {
            perror("Accept Failed");
            continue;
        }
        puts("connection Accepted!");

        new_sock = malloc(sizeof(int));
        *new_sock = new_socket;

        pthread_t sniffer_thread;
        if (pthread_create(&sniffer_thread, NULL, client_handler, (void *)new_sock) < 0) {
            perror("Thread creation failed");
            free(new_sock);
            close(new_socket);
            continue;
        }
        pthread_detach(sniffer_thread);
    }

    close(server_fd);
    return 0;
}
