/*
   ==UserScript==
 @name         TP01Q02 - Palíndromo em C
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q02 - Palíndromo em C
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

int isPalindromo(char entrada[]){
    int tamEntrada = tamanhoEntrada(entrada);
    int flag = 1;

    for(int i=0; i<tamEntrada/2; i++){
        if(entrada[i] != entrada[tamEntrada - 1 - i]){
            flag = 0;
            i = tamEntrada;
        }
    }

    return flag;
}

int main(void) {
    char entrada[500];

    scanf(" %[^\r\n]", entrada);

    while(!isEnd(entrada)){
        printf("%s\n", isPalindromo(entrada) ? "SIM" : "NAO");
        scanf(" %[^\r\n]", entrada);
    }

    return 0;
}