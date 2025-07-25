/*
   ==UserScript==
 @name         TP03Q07 - Fila com Alocação Flexível em C
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP03Q07 - Fila com Alocação Flexível em C
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
#include <math.h>

#define MAX_LINE 1024
#define MAX_SHOWS 500
#define TAM_FILA 5
#define MAX_CAMPOS 20

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

typedef struct No {
    Show show;
    struct No *prox;
} No;

typedef struct {
    No *primeiro;
    No *ultimo;
    int tamanho;
} FilaCircular;
 
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
        if (tm_ptr == NULL) {
            strcpy(date_str, "NaN");
        } else {
            strftime(date_str, sizeof(date_str), "%B %-d, %Y", tm_ptr);
        }
    }

    char elenco[1024];
    strcpy(elenco, "[");
    if (s->cast) {
        for (int i = 0; i < s->cast_count; i++) {
            strcat(elenco, s->cast[i] ? s->cast[i] : "NaN");
            if (i < s->cast_count - 1)
                strcat(elenco, ", ");
        }
    }
    strcat(elenco, "]");

    char categorias[1024];
    strcpy(categorias, "[");
    if (s->listed_in) {
    for (int i = 0; i < s->listed_count; i++) {
        strcat(categorias, s->listed_in[i] ? s->listed_in[i] : "NaN");
        if (i < s->listed_count - 1)
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

int separa_e_ordena(char ***destino, char *texto) {
    int quantidade = 1;
    for (int i = 0; texto[i] != '\0'; i++) {
        if (texto[i] == ',') quantidade++;
    }

    *destino = malloc(sizeof(char *) * quantidade);

    int indice = 0;
    char *token = strtok(texto, ",");
    while (token != NULL) {
        while (*token == ' ') token++; 
        (*destino)[indice++] = strdup(token);
        token = strtok(NULL, ",");
    }

    ordena(*destino, quantidade);
    return quantidade;
}

time_t converter_data(const char *texto) {
    if (texto == NULL || texto[0] == '\0') return (time_t)-1;
    struct tm tm_data = {0};
    if (strptime(texto, "%B %d, %Y", &tm_data) == NULL) return (time_t)-1;
    return mktime(&tm_data);
}

int parse_csv_line(const char *linha, char campos[][MAX_LINE]) {
    int campo = 0, pos = 0;
    bool dentro_aspas = false;

    for (int i = 0; linha[i] != '\0'; i++) {
        char c = linha[i];

        if (c == '"') {
            dentro_aspas = !dentro_aspas;
        } else if (c == ',' && !dentro_aspas) {
            campos[campo][pos] = '\0';
            campo++;
            pos = 0;
            if (campo >= MAX_CAMPOS) break; 
        } else {
            if (pos < MAX_LINE - 1) {
                campos[campo][pos++] = c;
            }
        }
    }
    campos[campo][pos] = '\0'; 
    return campo + 1; 
}

static void interpreta(Show *s, char *linha) {
    char campos[MAX_CAMPOS][MAX_LINE];
    int num_campos = parse_csv_line(linha, campos);
    s->show_ID = strdup(campos[0]);
    s->type = strcasecmp(campos[1], "movie") == 0 ? strdup("Movie") : strdup("TV Show");
    s->title = strdup(campos[2]);
    s->director = (*campos[3]) ? strdup(campos[3]) : strdup("NaN");
    s->country = (*campos[5]) ? strdup(campos[5]) : strdup("NaN");
    s->rating = strdup(campos[8]);
    s->duration = strdup(campos[9]);

    if (*campos[4]) 
        s->cast_count = separa_e_ordena(&s->cast, campos[4]);
    else {
        s->cast = malloc(sizeof(char*));
        s->cast[0] = strdup("NaN");
        s->cast_count = 1;
    }

    if (*campos[10]) 
        s->listed_count = separa_e_ordena(&s->listed_in, campos[10]);
    else {
        s->listed_in = malloc(sizeof(char*));
        s->listed_in[0] = strdup("NaN");
        s->listed_count = 1;
    }

    s->data_added = converter_data(campos[6]);
    s->release_year = (*campos[7]) ? atoi(campos[7]) : 0;
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
        init_show(s);
    }
}

Show clone(Show *original){
    Show clone;
    init_show(&clone);

    clone.show_ID = strdup(original->show_ID);
    clone.type = strdup(original->type);
    clone.title = strdup(original->title);
    clone.director = strdup(original->director);
    clone.country = strdup(original->country);
    clone.data_added = original->data_added;
    clone.release_year = original->release_year;
    clone.rating = strdup(original->rating);
    clone.duration = strdup(original->duration);
    clone.cast_count = original->cast_count;
    clone.cast = malloc(clone.cast_count * sizeof(char*));
    for (int i = 0; i < clone.cast_count; i++) {
        clone.cast[i] = strdup(original->cast[i]);
    }
    clone.listed_count = original->listed_count;
    clone.listed_in = malloc(clone.listed_count * sizeof(char*));
    for (int i = 0; i < clone.listed_count; i++) {
        clone.listed_in[i] = strdup(original->listed_in[i]);
    }
    return clone;
}

bool filaCheia(FilaCircular *fila){
    return (fila->tamanho == TAM_FILA);
}

bool filaVazia(FilaCircular *fila){
    return (fila->tamanho == 0);
}

void inicializar(FilaCircular *fila){
    fila->primeiro = NULL;
    fila->ultimo = NULL;
    fila->tamanho = 0;
}

Show remover(FilaCircular *fila){
    if (filaVazia(fila)) {
        Show vazio;
        init_show(&vazio);
        return vazio;
    }
    
    No *temp = fila->primeiro;
    Show removido = temp->show;
    
    if (fila->tamanho == 1) {
        fila->primeiro = NULL;
        fila->ultimo = NULL;
    } else {
        fila->primeiro = temp->prox;
        fila->ultimo->prox = fila->primeiro;
    }
    
    free(temp);
    fila->tamanho--;
    return removido;
}

void removedor(FilaCircular *fila){
    if (filaVazia(fila)) return;
    
    No *temp = fila->primeiro;
    
    if (fila->tamanho == 1) {
        fila->primeiro = NULL;
        fila->ultimo = NULL;
    } else {
        fila->primeiro = temp->prox;
        fila->ultimo->prox = fila->primeiro; 
    }
    
    free_show(&temp->show);
    free(temp);
    fila->tamanho--;
}

void inserir(FilaCircular *fila, Show show){
    if (filaCheia(fila)) {
        removedor(fila);
    }
    
    No *novo = malloc(sizeof(No));
    novo->show = show;
    
    if (filaVazia(fila)) {
        fila->primeiro = novo;
        fila->ultimo = novo;
        novo->prox = novo; 
    } else {
        novo->prox = fila->primeiro;
        fila->ultimo->prox = novo;
        fila->ultimo = novo;
    }
    
    fila->tamanho++;
}

bool ehInsere(char *comando){
    return (strcmp(comando, "I") == 0);
}

void separa(char entrada[], char partes[][MAX_LINE]){
    int i = 0, j = 0;
    int parte = 0;
    while(entrada[i] != ' '){
        partes[parte][j] = entrada[i];
        i++;
        j++; 
    }
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
}

void imprimirFila(FilaCircular *fila) {
    if (filaVazia(fila)) return;
    
    No *atual = fila->primeiro;
    for(int j = 0; j < fila->tamanho; j++) {
        printf("[%d] ", j);
        imprimir_show(&atual->show);
        atual = atual->prox;
    }
}

void calcularMedia(FilaCircular *fila){
    if (filaVazia(fila)) {
        printf("[Media] 0\n");
        return;
    }
    
    int soma = 0;
    No *atual = fila->primeiro;
    for(int j = 0; j < fila->tamanho; j++){
        soma += atual->show.release_year;
        atual = atual->prox;
    }
    int media = soma / fila->tamanho;
    printf("[Media] %d\n", media);
}

void liberarFila(FilaCircular *fila) {
    while (!filaVazia(fila)) {
        removedor(fila);
    }
}

int main() {
    char entrada[MAX_LINE];
    FilaCircular fila;
    inicializar(&fila);
    Show show;
    
    fgets(entrada, MAX_LINE, stdin);
    size_t len = strlen(entrada);
    if(len > 0 && entrada[len-1]=='\n'){
        entrada[len-1] = '\0';
    }
    
    while(!ehFim(entrada)) {
        show_from_id(&show, entrada);
        inserir(&fila, clone(&show));
        free_show(&show);
        calcularMedia(&fila);
        fgets(entrada, MAX_LINE, stdin);
        len = strlen(entrada);
        if(len > 0 && entrada[len-1]=='\n'){
            entrada[len-1] = '\0';
        }
    }
    
    int n;
    scanf("%d", &n);
    getchar();
    
    for(int i = 0; i < n; i++){
        fgets(entrada, MAX_LINE, stdin);
        len = strlen(entrada);
        if(len > 0 && entrada[len-1]=='\n'){
            entrada[len-1] = '\0';
        }
        char partes[2][MAX_LINE];
        separa(entrada, partes);
        if(strcmp(partes[0], "I") == 0){
            show_from_id(&show, partes[1]);
            inserir(&fila, clone(&show));
            calcularMedia(&fila);
        }
        else if(strcmp(partes[0], "R") == 0){
            Show removido = remover(&fila);
            printf("(R) %s\n", removido.title ? removido.title : "NaN");
            free_show(&removido);
        }
    }
    
    imprimirFila(&fila);
    liberarFila(&fila);
    return 0;
}