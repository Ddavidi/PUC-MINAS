/*
   ==UserScript==
 @name         TP01Q17 - RECURSIVO - Palíndromo em C
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q17 - RECURSIVO - Palíndromo em C
 @author       @ddavidi_
   ==/UserScript==
*/

#include <stdio.h>

int isEnd(char entrada[]){
    return entrada[0] == 'F' && entrada[1] == 'I' && entrada[2] == 'M' && entrada[3] == '\0';
}

int tamanhoEntrada(char entrada[]){
    int i = 0;

    while (entrada[i] != '\0'){
        i++;
    }

    return i;
}

int isPalindromo(char entrada[], int inicio, int fim){

    if(inicio >= fim){
        return 1;
    }

    if(entrada[inicio]!=entrada[fim]){
        return 0;
    }

    return isPalindromo(entrada, inicio+1, fim-1);
}

int isPalindromoAuxiliar(char entrada[]){
    int tamEntrada = tamanhoEntrada(entrada);

    if(tamEntrada == 0) return 1;

    return isPalindromo(entrada, 0, tamEntrada-1);
}

int main(void) {
    char entrada[500];

    scanf(" %[^\r\n]", entrada);

    while(!isEnd(entrada)){
        printf("%s\n", isPalindromoAuxiliar(entrada) ? "SIM" : "NAO");
        scanf(" %[^\r\n]", entrada);
    }

    return 0;
}