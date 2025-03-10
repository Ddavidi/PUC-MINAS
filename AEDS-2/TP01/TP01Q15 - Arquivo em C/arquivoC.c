/*
   ==UserScript==
 @name         TP01Q15 - Arquivo em C
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q15 - Arquivo em C
 @author       @ddavidi_
   ==/UserScript==
*/

#include <stdio.h>
#include <string.h>

int main(){
    FILE *arquivoWrite = fopen("arquivo.txt", "w");
    if(arquivoWrite == NULL){
        printf("ERRO - cant open file write");
        return 1;
    }
    int n;
    float input;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        scanf("%f", &input);
        fprintf(arquivoWrite, "%f\n", input);
    }
    fclose(arquivoWrite);
    //double output;
    FILE *arquivoRead = fopen("arquivo.txt", "r");
    if(arquivoRead == NULL){
        printf("ERRO - cant open file read");
        return 1;
    }
    double values[n];
    for(int i = 0; i < n; i++){
        fscanf(arquivoRead, "%lf", &values[i]);
        fscanf(arquivoRead, "\n");
    }
    for(int i = n-1; i >= 0; i--){
        printf("%g\n", values[i]);
    }
    fclose(arquivoRead);
    return 0;
}