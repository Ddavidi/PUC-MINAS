/*
   ==UserScript==
 @name         TP02Q02 - Registro em C
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP02Q02 - Registro em C
 @author       @ddavidi_
   ==/UserScript==
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SHOWS 1370
#define MAX_LINE 1024
#define MAX_CAST 30
#define MAX_NAME 100

typedef struct {
    char show_id[20];
    char type[50];
    char title[200];
    char director[100];
    char cast[300];
    char country[100];
    char date_added[50];
    int release_year;
    char rating[20];
    char duration[20];
    char listed_in[200];
} Show;

void trim_newline(char *str) {
    int i = 0;
    while (str[i]) {
        if (str[i] == '\n') {
            str[i] = '\0';
            return;
        }
        i++;
    }
}

void copiarCampo(char *destino, const char *linha, int *i) {
    int j = 0;
    if (linha[*i] == '"') {
        (*i)++;
        while (linha[*i] && !(linha[*i] == '"' && linha[*i + 1] == ',')) {
            if (linha[*i] == '"' && linha[*i + 1] == '"') {
                // Ignorar as aspas duplas
                (*i) += 2;
            } else {
                destino[j++] = linha[*i];
                (*i)++;
            }
        }
        (*i) += 2; 
    } else {
        while (linha[*i] && linha[*i] != ',' && linha[*i] != '\n') {
            destino[j++] = linha[*i];
            (*i)++;
        }
        if (linha[*i] == ',') (*i)++; 
    }
    destino[j] = '\0';
}
const char* verificaCampo(const char* campo) {
    return (campo[0] == '\0') ? "NaN" : campo;
}

void ordenar_cast(char cast_ordenado[][MAX_NAME], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (strcmp(cast_ordenado[j], cast_ordenado[j + 1]) > 0) {
                char temp[MAX_NAME];
                strcpy(temp, cast_ordenado[j]);
                strcpy(cast_ordenado[j], cast_ordenado[j + 1]);
                strcpy(cast_ordenado[j + 1], temp);
            }
        }
    }
}

void imprimirShow(Show s) {
    // Processar e ordenar cast
    char cast_ordenado[MAX_CAST][MAX_NAME];
    int cast_count = 0;

    if (s.cast[0] != '\0') {
        int i = 0, j = 0, k = 0;
        while (s.cast[i]) {
            if (s.cast[i] == ',' && s.cast[i + 1] == ' ') {
                cast_ordenado[cast_count][j] = '\0';
                cast_count++;
                i += 2;
                j = 0;
            } else {
                cast_ordenado[cast_count][j++] = s.cast[i++];
            }
        }
        cast_ordenado[cast_count][j] = '\0';
        cast_count++;

        ordenar_cast(cast_ordenado, cast_count);
    }

    // Imprimir formatado
    printf("=> %s ## %s ## %s ## %s ## [",
           verificaCampo(s.show_id),
           verificaCampo(s.title),
           verificaCampo(s.type),
           verificaCampo(s.director));

    if (cast_count > 0) {
        for (int i = 0; i < cast_count; i++) {
            printf("%s", verificaCampo(cast_ordenado[i]));
            if (i < cast_count - 1) printf(", ");
        }
    } else {
        printf("NaN");
    }

    printf("] ## %s ## %s ## %d ## %s ## %s ## [%s] ##\n",
           verificaCampo(s.country),
           verificaCampo(s.date_added),
           s.release_year > 0 ? s.release_year : 0,
           verificaCampo(s.rating),
           verificaCampo(s.duration),
           verificaCampo(s.listed_in));
}

int main() {
    FILE *file = fopen("/tmp/disneyplus.csv", "r");
    if (file == NULL) {
        printf("Erro ao abrir o arquivo.\n");
        return 1;
    }

    Show shows[MAX_SHOWS];
    char linha[MAX_LINE];
    int count = 0;

    fgets(linha, MAX_LINE, file); // Pula cabeçalho

    while (fgets(linha, MAX_LINE, file) && count < MAX_SHOWS) {
        int i = 0;
        copiarCampo(shows[count].show_id, linha, &i);
        copiarCampo(shows[count].type, linha, &i);
        copiarCampo(shows[count].title, linha, &i);
        copiarCampo(shows[count].director, linha, &i);
        copiarCampo(shows[count].cast, linha, &i);
        copiarCampo(shows[count].country, linha, &i);
        copiarCampo(shows[count].date_added, linha, &i);

        char release_year_str[10];
        copiarCampo(release_year_str, linha, &i);
        shows[count].release_year = atoi(release_year_str);

        copiarCampo(shows[count].rating, linha, &i);
        copiarCampo(shows[count].duration, linha, &i);
        copiarCampo(shows[count].listed_in, linha, &i);

        count++;
    }

    fclose(file);
    char entrada[20];
    fgets(entrada, sizeof(entrada), stdin);
    trim_newline(entrada);

    while (strcmp(entrada, "FIM") != 0) {
        int encontrado = 0;
        for (int i = 0; i < count; i++) {
            if (strcmp(shows[i].show_id, entrada) == 0) {
                imprimirShow(shows[i]);
                encontrado = 1;
                break;
            }
        }

        fgets(entrada, sizeof(entrada), stdin);
        trim_newline(entrada);
    }

    return 0;
}