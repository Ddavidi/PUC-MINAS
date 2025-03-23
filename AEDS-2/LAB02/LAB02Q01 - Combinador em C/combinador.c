/*
   ==UserScript==
 @name         LAB02Q01 - Combinador em C
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - LAB02Q01 - Combinador em C
 @author       @ddavidi_
   ==/UserScript==
*/

#include <stdio.h>

int tamString(char entrada[]){
    int i = 0;
    
    while(entrada[i] != '\0'){
        i++;
    }

    return i;
}

void mostraCombinador(char string1[], char string2[]){
    int tam1 = tamString(string1);
    int tam2 = tamString(string2);
    char stringFinal[tam1 + tam2 + 1];
    int maiorTamanho = tam1 > tam2 ? tam1 : tam2;
    int j=0;

    for(int i=0; i<maiorTamanho; i++){
        if(i<tam1){
            stringFinal[j] = string1[i];
            j++;
        }
        if(i<tam2){
            stringFinal[j] = string2[i];
            j++;
        }
    }

    stringFinal[j] = '\0';

    printf("%s\n", stringFinal);

}

int main(){
    char string1[100];
    char string2[100];

    while(scanf(" %s %s", string1, string2) != EOF){
        mostraCombinador(string1, string2);
    }

    return 0;
}