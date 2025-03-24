/*
   ==UserScript==
 @name         LAB01Q04 - Aquecimento Recursivo em C
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - LAB01Q04 - Aquecimento Recursivo em C
 @author       @ddavidi_
   ==/UserScript==
*/

#include <stdio.h>
#include <string.h>

int isFim(char entrada[]) {
    return entrada[0] == 'F' && entrada[1] == 'I' && entrada[2] == 'M' && entrada[3] == '\0';
}

int tamString(char entrada[], int i) {
    if (entrada[i] == '\0') {
        return 0;
    }
    return 1 + tamString(entrada, i + 1);
}

int retornaQntInteiro(char entrada[], int i, int tam) {
    if (i >= tam) {
        return 0;
    }
    if (entrada[i] >= 'A' && entrada[i] <= 'Z') {
        return 1 + retornaQntInteiro(entrada, i + 1, tam);
    }
    return retornaQntInteiro(entrada, i + 1, tam);
}

int main(void) {
    char entrada[99];
    int qntInteiro;

    scanf("%[^\n]", entrada);

    while (!isFim(entrada)) {
        int tamanho = tamString(entrada, 0);
        qntInteiro = retornaQntInteiro(entrada, 0, tamanho);

        printf("%d\n", qntInteiro);

        scanf(" %[^\n]", entrada);
    }

    return 0;
}