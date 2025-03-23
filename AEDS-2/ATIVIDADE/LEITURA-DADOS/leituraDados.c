#include <stdio.h>

void processarRegistro(int id, double preco, char* tempo, char* cidade) {
  printf("Registro lido: %d %.2f %s %s\n", id, preco, tempo, cidade);
}

int main(void){
    int id;
    double preco;
    char tempo[6];
    char cidade[50];

    while(scanf(" %d %lf %s %[^\n]", &id, &preco, tempo, cidade) == 4 && id != 0){
        processarRegistro(id, preco, tempo, cidade);   
    }

    return 0;
}