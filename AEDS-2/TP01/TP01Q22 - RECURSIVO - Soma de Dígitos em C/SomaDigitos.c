/*
   ==UserScript==
 @name         TP01Q22 - RECURSIVO - Soma de Dígitos em C
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q22 - RECURSIVO - Soma de Dígitos em C
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

int somaDigitos(char entrada[], int tam, int soma){
  int charInt;

  if (tam < 0){
    return soma;
  }

  else{
    charInt = entrada[tam] - '0';
    soma += charInt;
    return somaDigitos(entrada, tam-1, soma);
  }
}

int main() {

  char entrada[99];
  int soma;

  scanf(" %[^\r\n]", entrada);

  int tam = tamanhoEntrada(entrada);

  while(!isEnd(entrada)){
    soma = 0;
    printf("%d\n", somaDigitos(entrada, tam-1, soma));
    scanf(" %[^\r\n]", entrada);
    tam = tamanhoEntrada(entrada);
  }

  return 0;
}