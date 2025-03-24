/*
   ==UserScript==
 @name         LAB01Q03 - Aquecimento Interativo em C
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - LAB01Q03 - Aquecimento Interativo em C
 @author       @ddavidi_
   ==/UserScript==
*/

#include <stdio.h>
#include <string.h>

int isFim (char entrada[]) {
    return entrada[0] == 'F' && entrada[1] == 'I' && entrada[2] == 'M' && entrada[3] == '\0';
}

int tamString (char entrada[]){
    int i = 0;
    while(entrada[i]!= '\0'){
        i++;
    }

    return i;
}

int retornaQntInteiro(char entrada[]) {
    int tam = tamString(entrada);
    int j = 0;

    for(int i=0;i<tam; i++){
        if(entrada[i]>='A' && entrada[i]<='Z'){
            j++;
        }
    }

    return j;
}

int main (void) {

    char entrada[99];
    int qntInteiro;

    scanf("%[^\n]", entrada);

    while(!isFim(entrada)){

        qntInteiro = retornaQntInteiro(entrada);

        printf("%d\n", qntInteiro);

        scanf(" %[^\n]", entrada);

    }

    return 0;
}