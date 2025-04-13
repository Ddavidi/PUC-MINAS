#include <stdio.h>

int isPush(char acao[]){
    return acao[0] == 'P' && acao[1] == 'U' && acao[2] == 'S' && acao[3] == 'H' && acao[4] == '\0';
}

int isPop(char acao[]){
    return acao[0] == 'P' && acao[1] == 'O' && acao[2] == 'P' && acao[3] == '\0';
}

int isMin(char acao[]){
    return acao[0] == 'M' && acao[1] == 'I' && acao[2] == 'N' && acao[3] == '\0';
}

int main(void) {
    int N, valor, tamanhoLista, menor;
    char acao[10];
    int presentes[500];

    scanf("%d", &N);

    tamanhoLista = -1;
    menor = 99;

    for(int i=0; i<N; i++){

        scanf(" %s[^/r/n]", acao);
        
        if(isPush(acao)){
            tamanhoLista++;
            scanf("%d", &valor);
            presentes[tamanhoLista] = valor;
        }

        else if(isPop(acao)){
            tamanhoLista--;
        }

        else{
            for(int j=0; j<tamanhoLista; j++){
                if(presentes[j] < menor){
                    menor = presentes[j];
                }
            }

            printf("%d\n", menor);
        }
    }
}