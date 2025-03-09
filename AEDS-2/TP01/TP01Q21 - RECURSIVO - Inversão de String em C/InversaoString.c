/*
   ==UserScript==
 @name         TP01Q21 - RECURSIVO - Inversão de String em C
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q21 - RECURSIVO - Inversão de String em C
 @author       @ddavidi_
   ==/UserScript==
*/

#include <stdio.h>

int tamanhoEntrada(char entrada[]) {
    int i=0;

    while(entrada[i]!='\0'){
        i++;
    }

    return i;
}

void inversaoString(char entrada[], int pos) {
    if (pos < 0) {
        printf("\n");
        return;
    }
    printf("%c", entrada[pos]);
    inversaoString(entrada, pos - 1);
}

void inversaoStringWrapper(char entrada[]) {
    int tam = tamanhoEntrada(entrada);
    inversaoString(entrada, tam - 1);
}

int isEnd(char entrada[]) {
    return entrada[0] == 'F' && entrada[1] == 'I' && entrada[2] == 'M' && entrada[3] == '\0'; 
}

int main() {
    char entrada[1000];
    scanf(" %[^\n]s", entrada);
    while (!isEnd(entrada)) {
        inversaoStringWrapper(entrada);
        scanf(" %[^\n]s", entrada);
    }
    return 0;
}