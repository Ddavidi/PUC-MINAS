/*
   ==UserScript==
 @name         TP03Q02 - Lista com Alocação Sequencial em C
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP03Q02 - Lista com Alocação Sequencial em C
 @author       @ddavidi_
   ==/UserScript==
*/

#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>
#include <stdbool.h>
#include <time.h>
#include <locale.h>

#define MAX_LINE 1024
#define MAX_SHOWS 500

typedef struct {
    char *show_ID;
    char *type;
    char *title;
    char *director;
    char **cast;
    int cast_count;
    char *country;
    time_t data_added;
    int release_year;
    char *rating;
    char *duration;
    char **listed_in;
    int listed_count;
} Show;

void init_show(Show *s) {
    s->show_ID = NULL;
    s->type = NULL;
    s->title = NULL;
    s->director = NULL;
    s->cast = NULL;
    s->cast_count = 0;
    s->country = NULL;
    s->data_added = (time_t)-1;
    s->release_year = 0;
    s->rating = NULL;
    s->duration = NULL;
    s->listed_in = NULL;
    s->listed_count = 0;
}

void free_show(Show *s) {
    if(s->show_ID) free(s->show_ID);
    if(s->type) free(s->type);
    if(s->title) free(s->title);
    if(s->director) free(s->director);
    if(s->country) free(s->country);
    if(s->rating) free(s->rating);
    if(s->duration) free(s->duration);
    if(s->cast) {
       for (int i = 0; i < s->cast_count; i++) {
            free(s->cast[i]);
       }
       free(s->cast);
    }
    if(s->listed_in) {
       for (int i = 0; i < s->listed_count; i++) {
            free(s->listed_in[i]);
       }
       free(s->listed_in);
    }
}

int converteStr(const char *entrada) {
    int len = strlen(entrada);
    int valor = 0;
    int multiplicador = 1;
    for (int i = len - 1; i > 0; i--) {
        int numero = entrada[i] - '0';
        valor += numero * multiplicador;
        multiplicador *= 10;
    }
    return valor;
}
int ehFim(const char *entrada) {
    return (strcmp(entrada, "FIM") == 0);
}

void imprimir_show(const Show *s) {
    char date_str[32];
    if (s->data_added == (time_t)-1) {
        strcpy(date_str, "NaN");
    } else {
        struct tm *tm_ptr = localtime(&s->data_added);
        strftime(date_str, sizeof(date_str), "%B %-d, %Y", tm_ptr);
    }
    char elenco[1024] = "[";
    if (s->cast) {
        for (int i = 0; s->cast[i] != NULL; i++) {
            strcat(elenco, s->cast[i] ? s->cast[i] : "NaN");
            if (s->cast[i + 1] != NULL)
                strcat(elenco, ", ");
        }
    }
    strcat(elenco, "]");
    char categorias[1024] = "[";
    if (s->listed_in) {
        for (int i = 0; s->listed_in[i] != NULL; i++) {
            strcat(categorias, s->listed_in[i] ? s->listed_in[i] : "NaN");
            if (s->listed_in[i + 1] != NULL)
                strcat(categorias, ", ");
        }
    }
    strcat(categorias, "]");
    printf("=> %s ## %s ## %s ## %s ## %s ## %s ## %s ## %d ## %s ## %s ## %s ##\n",
        s->show_ID ? s->show_ID : "NaN",
        s->title ? s->title : "NaN",
        s->type ? s->type : "NaN",
        s->director ? s->director : "NaN",
        elenco,
        s->country ? s->country : "NaN",
        date_str,
        s->release_year,
        s->rating ? s->rating : "NaN",
        s->duration ? s->duration : "NaN",
        categorias);
}

void ordena(char *array[], int tam) {
    int trocou;
    do {
        trocou = 0;
        for (int i = 0; i < tam - 1; i++) {
            if (strcmp(array[i], array[i+1]) > 0) {
                char *temp = array[i];
                array[i] = array[i+1];
                array[i+1] = temp;
                trocou = 1;
            }
        }
        tam--;
    } while(trocou);
}

void separa_e_ordena(char ***destino, char *texto) {
    int quantidade = 1;
    for (int i = 0; texto[i] != '\0'; i++) {
        if (texto[i] == ',') quantidade++;
    
    }
    *destino = malloc(sizeof(char *) * (quantidade + 1));  

    int indice = 0;
    char *token = strtok(texto, ",");
    while (token != NULL) {
        while (*token == ' ') token++;  
        (*destino)[indice++] = strdup(token);  
        token = strtok(NULL, ",");
    }
    (*destino)[indice] = NULL; 
    ordena(*destino, quantidade);
}

time_t converter_data(const char *texto) {
    if (texto == NULL || texto[0] == '\0') return (time_t)-1;
    struct tm tm_data = {0};
    if (strptime(texto, "%B %d, %Y", &tm_data) == NULL) return (time_t)-1;
    return mktime(&tm_data);
}

void interpreta(Show *s, char *linha) {
    char campo_temp[1024];
    int posicao = 0;
    int dentro_aspas = 0;
    int indice_campo = 0;
    char *campos[20];
    int i;
    for (i = 0; i < 20; i++) {
        campos[i] = NULL;
    }

    campos[0] = malloc(1024);
    posicao = 0;

    for (i = 0; linha[i] != '\0'; i++) {
        char letra = linha[i];
        if (letra == '"') {
            dentro_aspas = !dentro_aspas;
        } else if (letra == ',' && !dentro_aspas) {
            campos[indice_campo][posicao] = '\0';
            indice_campo++;
            campos[indice_campo] = malloc(1024);
            posicao = 0;
        } else {
            campos[indice_campo][posicao++] = letra;
        }
    }
    campos[indice_campo][posicao] = '\0';

   
    s->show_ID = strdup(campos[0]);
    s->type = (strcasecmp(campos[1], "movie") == 0) ? strdup("Movie") : strdup("TV Show");
    s->title = strdup(campos[2]);
    s->director = (campos[3][0] == '\0') ? strdup("NaN") : strdup(campos[3]);
    s->country = (campos[5][0] == '\0') ? strdup("NaN") : strdup(campos[5]);
    s->rating = strdup(campos[8]);
    s->duration = strdup(campos[9]);
    // Analisa e array de strings, e decide se é vazio ou não, se não for, é preparado e ordenado
    if (campos[4][0] == '\0') {
        s->cast = malloc(sizeof(char *) * 2);
        s->cast[0] = strdup("NaN");
        s->cast[1] = NULL;
    } else {
        separa_e_ordena(&s->cast, campos[4]);
    }
    if (campos[10][0] == '\0') {
        s->listed_in = malloc(sizeof(char *) * 2);
        s->listed_in[0] = strdup("NaN");
        s->listed_in[1] = NULL;
    } else {
        separa_e_ordena(&s->listed_in, campos[10]);
    }

    s->data_added = converter_data(campos[6]);

    s->release_year = (campos[7][0] == '\0') ? 0 : atoi(campos[7]);

    for (i = 0; i <= indice_campo; i++) {
        free(campos[i]);
    }
}

void show_from_id(Show *s, char *entrada) {
    int id = converteStr(entrada);
    FILE *fp = fopen("/tmp/disneyplus.csv", "r");
    if (!fp) {
        perror("Erro ao abrir o arquivo");
        exit(1);
    }
    char line[MAX_LINE];
    int contador = 0;
    bool encontrado = false;
    while (fgets(line, MAX_LINE, fp) && !encontrado) {
        // Remove o caractere de nova linha, se existir
        size_t l = strlen(line);
        if(l > 0 && line[l-1]=='\n')
            line[l-1] = '\0';
        if (contador == id) {
            interpreta(s, line);
            encontrado = true;
        }
        contador++;
    }
    fclose(fp);
    if (!encontrado) {
        // Caso o id digitado seja invalido, inicianliza sem valor
        init_show(s);
    }
}

void clone(Show *original, Show *clone){
    init_show(clone); // Sempre inicialize antes

    clone->show_ID = strdup(original->show_ID);
    clone->type = strdup(original->type);
    clone->title = strdup(original->title);
    clone->director = strdup(original->director);
    clone->country = strdup(original->country);
    clone->data_added = original->data_added;
    clone->release_year = original->release_year;
    clone->rating = strdup(original->rating);
    clone->duration = strdup(original->duration);
    // primeiro copia a contagem, para depois conseguir copiar completamente cada parte
    clone->cast_count = original->cast_count;
    clone->cast = malloc(clone->cast_count * sizeof(char*));
    for (int i = 0; i < clone->cast_count; i++) {
        clone->cast[i] = strdup(original->cast[i]);
    }
    clone->listed_count = original->listed_count;
    clone->listed_in = malloc(clone->listed_count * sizeof(char*));
    for (int i = 0; i < clone->listed_count; i++) {
        clone->listed_in[i] = strdup(original->listed_in[i]);
    }
}

void inserirFim(Show show, Show lista[], int *tam){
    // Insere o show diretamente na ultima posição e em seguida incrementa tam
    lista[(*tam)++] = show;
}


void inserirInicio(Show show, Show lista[], int *tam) {
    // Abre espaço no array para ser colocado um elemento no inicio
    for (int i = *tam; i > 0; i--) {
        lista[i] = lista[i - 1];
    }
    lista[0] = show;
    (*tam)++;
}

void inserir(Show show, int pos, Show lista[], int *tam) {
    // Abre espaço na posição para ser inserido o show
    for (int i = *tam; i > pos; i--) {
        lista[i] = lista[i - 1];
    }
    lista[pos] = show;
    (*tam)++;
}

Show removerInicio(Show lista[], int *tam) {
    // Armazena o elemento a ser removido
    Show removido = lista[0];
    // Disloca os elementos para esquerda, para apagar o inicio
    (*tam)--;
    for (int i = 0; i < *tam; i++) {
        lista[i] = lista[i + 1];
    }
    return removido;
}

Show remover(int pos, Show lista[], int *tam) {
    // Armaza o show removido
    Show removido = lista[pos];
    (*tam)--;
    // Disloca os elementos para ocupar o espaço
    for (int i = pos; i < *tam; i++) {
        lista[i] = lista[i + 1];
    }
    return removido;
}

Show removerFim(Show lista[], int *tam) {
    return lista[--(*tam)];
}

bool ehInsere(char *comando){
    return (strcmp(comando, "II") == 0 || strcmp(comando, "IF") == 0);
}


bool ehRemovePos(char *comando) {
    return (strcmp(comando, "R*") == 0);
}

void separa(char entrada[], char partes[][MAX_LINE]){
    int i = 0, j = 0;
    int parte = 0;
    while(entrada[i] != ' '){
        partes[parte][j] = entrada[i];
        i++;
        j++; 
    }
    // Inserção do '\0' que demarca o fim da string
    partes[parte][j] = '\0';
    parte++;
    i++;
    if(ehInsere(partes[0])){
        int j = 0;
        while(entrada[i] != '\0'){
            partes[parte][j] = entrada[i];
            j++;
            i++;
        }
        partes[parte][j] = '\0';
    }
    else if(strcmp(partes[0], "I*") == 0){
        int j = 0;
        while(entrada[i] != ' '){
            partes[parte][j] = entrada[i];
            i++;
            j++;
        }
        partes[parte][j] = '\0';
        i++;
        parte++;
        j = 0;
        while(entrada[i] != '\0'){
            partes[parte][j] = entrada[i];
            i++;
            j++;
        }
        partes[parte][j] = '\0';
    }
    else if(ehRemovePos(partes[0])){
        // Verifica se é 'R*' pois possui 2 campos, comando/posição
        int j = 0;
        while(entrada[i] != '\0'){
            partes[parte][j] = entrada[i];
            i++;
            j++;
        }
        partes[parte][j] = '\0';
    }
}

int main() {
    setlocale(LC_TIME, "C");
    char entrada[MAX_LINE];
    Show lista[MAX_SHOWS];
    int tam = 0;
    // Inicializa todos os objetos no array
    for (int i = 0; i < MAX_SHOWS; i++) {
        init_show(&lista[i]);
    }
    fgets(entrada, MAX_LINE, stdin);
    size_t len = strlen(entrada);
        if(len > 0 && entrada[len-1]=='\n'){
            entrada[len-1] = '\0';
        }
    while(!ehFim(entrada)) {
        show_from_id(&lista[tam], entrada);
        tam++;
        fgets(entrada, MAX_LINE, stdin);
        len = strlen(entrada);
        if(len > 0 && entrada[len-1]=='\n'){
            entrada[len-1] = '\0';
        }
    }
    // Inicio da leitura da 2 parte
    int n;
    scanf("%d", &n);
    char **removidos = malloc(100 * sizeof(char*));
    getchar();
    int ind = 0;
    for(int i = 0; i < n; i++){
        fgets(entrada, MAX_LINE, stdin);
        len = strlen(entrada);
        if(len > 0 && entrada[len-1]=='\n'){
            entrada[len-1] = '\0';
        }
        // Separa os campos da entrada
        char partes[3][MAX_LINE];
        separa(entrada, partes);
        Show show;
        if(strcmp(partes[0], "II") == 0){
            show_from_id(&show, partes[1]);
            inserirInicio(show, lista, &tam);
        }
        else if(strcmp(partes[0], "I*") == 0){
            show_from_id(&show, partes[2]);
            int pos = atoi(partes[1]);
            inserir(show, pos, lista, &tam);
        }
        else if(strcmp(partes[0], "IF") == 0) {
            show_from_id(&show, partes[1]);
            inserirFim(show, lista, &tam);
        }
        else if(strcmp(partes[0], "RI") == 0){
            removidos[ind++] = removerInicio(lista, &tam).title;
        }
        else if(strcmp(partes[0], "R*") == 0){
            int pos = atoi(partes[1]);
            removidos[ind++] = remover(pos, lista, &tam).title;
        } 
        else if(strcmp(partes[0], "RF") == 0) {
            removidos[ind++] = removerFim(lista, &tam).title;
        }
    }
    for(int i = 0; i < ind; i++){
        printf("(R) %s\n", removidos[i]);
    }
    for (int i = 0; i < tam; i++) {
        imprimir_show(&lista[i]);
        free_show(&lista[i]);
    }
    free(removidos);
    removidos = NULL;
    return 0;
}