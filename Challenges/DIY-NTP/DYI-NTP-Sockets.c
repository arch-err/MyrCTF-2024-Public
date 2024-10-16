#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <ctype.h>
#include <time.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <pthread.h>

#define PORT 321
#define BUFFER_SIZE 4096

// Behövde konvertera denna jäveln från en lokal utmaning till en med sockets.
// Efter mycket om och men fick jag det att fungera, sen fick chatGPT lägga in send_data funktionen där den behövdes.
// palla skriva om allt själv.

void send_data(int sock, const char *data) {
    send(sock, data, strlen(data), 0);
}

int Introduction(int socket) {
    send_data(socket, "\nHerr Brainiacs egna NTP-server!\nAnvändare utan rättigheter eller behörighet avisas\n");
    return 0;
}

int Menu(int socket) {
    send_data(socket, "\n1. Logga in med lösenord\n2. Hämta tid\n3. Byt Autentiseringsmetod\n4. Exit\n");

    char input[4];
    int res = recv(socket, input, sizeof(input) - 1, 0);

    if (res <= 0) {
        return -1; // Error or disconnect
    }

    input[res] = '\0'; // Null-terminate the received data

    int option = atoi(input); // Convert the input to an integer

    if (option < 1 || option > 4) {
        send_data(socket, "ERROR!\nFelaktig Input!!\n");
        return Menu(socket); // Recursively ask for input again
    }

    return option;
}

int Login(char *LPPasswordBuffer, int socket) {
    send_data(socket, "Logga in med Lösenord: ");
    recv(socket, LPPasswordBuffer, 4096, 0); // Properly receive password input

    send_data(socket, "Fel Lösenord...\n");

    return 1;
}

void mainprogram(int socket) {
    char cPasswordBuffer[256];

    Introduction(socket);

    while (1) {
        int menu = Menu(socket);
        if (menu == -1) {
            break; // Exit the loop on error or disconnect
        }

        switch (menu) {
            case 1:
                Login(cPasswordBuffer, socket);
                break;
            case 2:
                {
                    char timeStr[100];
                    snprintf(timeStr, sizeof(timeStr), "Nuvarande tid från EPOCH: %lu\n", (unsigned long)time(NULL));
                    send_data(socket, timeStr);
                }
                break;
            case 3:
                {
                    char buffer[100];
                    snprintf(buffer, sizeof(buffer), "ERROR IN ERROR: %p\n", (void *)&cPasswordBuffer);
                    send_data(socket, buffer);
                }
                break;
            case 4:
                send_data(socket, "Exiting...\n");
                printf("exiting");
                return; // Exit the function on user request
            default:
                send_data(socket, "ERROR!\nDu har gjort ett fel, rätta dig.\n");
                break;
        }
    }
}

void *client_handler(void *socket_desc) {
    int sock = *(int *)socket_desc;

    mainprogram(sock);

    close(sock);
    free(socket_desc);
    pthread_exit(NULL); // Ensure the thread exits cleanly
}

int main() {
    int server_fd, new_socket, *new_sock;
    struct sockaddr_in address;
    int addrlen = sizeof(address);
    int optval = 1;

    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("Socket failed");
        exit(EXIT_FAILURE);
    }
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &optval, sizeof(optval)) < 0) {
        perror("setsockopt");
        close(server_fd);
        exit(EXIT_FAILURE);
    }


    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }

    if (listen(server_fd, 3) < 0) {
        perror("Listen failed");
        exit(EXIT_FAILURE);
    }

    puts("Awaiting connections...");

    while (1) {
        new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t *)&addrlen);
        if (new_socket < 0) {
            perror("Accept failed");
            continue; // Continue accepting new connections even if one fails
        }

        puts("Connection accepted");

        new_sock = malloc(sizeof(int));
        *new_sock = new_socket;

        pthread_t sniffer_thread;
        if (pthread_create(&sniffer_thread, NULL, client_handler, (void *)new_sock) < 0) {
            perror("Thread creation failed");
            free(new_sock);
            close(new_socket);
            continue; // Handle the error, but continue the loop
        }

        pthread_detach(sniffer_thread); // Detach the thread to ensure resources are cleaned up
    }

    close(server_fd);
    return 0;
}
