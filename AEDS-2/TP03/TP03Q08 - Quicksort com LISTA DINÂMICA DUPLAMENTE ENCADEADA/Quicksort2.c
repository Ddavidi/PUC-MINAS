/*
   ==UserScript==
 @name         TP03Q08 - Quicksort com LISTA DINÂMICA DUPLAMENTE ENCADEADA
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP03Q08 - Quicksort com LISTA DINÂMICA DUPLAMENTE ENCADEADA
 @author       @ddavidi_
   ==/UserScript==
*/

#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <locale.h>

#define MAX_LINE 1024

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


typedef struct Celula {
    Show elemento;
    struct Celula *prox;
    struct Celula *ant;
} Celula;

Celula *primeiro;
Celula *ultimo;
int tamanho;

void inicializar() {
    primeiro = (Celula*)malloc(sizeof(Celula));
    ultimo = primeiro;
    primeiro->prox = NULL;
    primeiro->ant = NULL;
    tamanho = 0;
}

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

void liberar_lista() {
    Celula *temp = primeiro->prox;
    while (temp != NULL) {
        Celula *proxima = temp->prox;
        free_show(&temp->elemento);
        free(temp);
        temp = proxima;
    }
    free(primeiro);
    tamanho = 0;
}

void inserirFim(Show show) {
    Celula *nova = (Celula*)malloc(sizeof(Celula));
    nova->elemento = show;
    nova->prox = NULL;
    nova->ant = ultimo;
    ultimo->prox = nova;
    ultimo = nova;
    tamanho++;
}


char para_minusculo(char c) {
    if (c >= 'A' && c <= 'Z') {
        return c + 32;
    }
    return c;
}

int strcmp_case_insensitive(const char *s1, const char *s2) {
    while (*s1 && *s2) {
        char c1 = para_minusculo(*s1);
        char c2 = para_minusculo(*s2);
        if (c1 != c2) {
            return c1 - c2;
        }
        s1++;
        s2++;
    }
    return para_minusculo(*s1) - para_minusculo(*s2);
}

int string_para_int(const char *str) {
    int resultado = 0;
    int sinal = 1;
    int i = 0;
    
    if (str[0] == '-') {
        sinal = -1;
        i = 1;
    }
    
    while (str[i] != '\0') {
        if (str[i] >= '0' && str[i] <= '9') {
            resultado = resultado * 10 + (str[i] - '0');
        } else {
            break; 
        }
        i++;
    }
    
    return resultado * sinal;
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

// Verifica se a entrada é exatamente "FIM"
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
    s->type = (strcmp_case_insensitive(campos[1], "movie") == 0) ? strdup("Movie") : strdup("TV Show");
    s->title = strdup(campos[2]);
    s->director = (campos[3][0] == '\0') ? strdup("NaN") : strdup(campos[3]);
    s->country = (campos[5][0] == '\0') ? strdup("NaN") : strdup(campos[5]);
    s->rating = strdup(campos[8]);
    s->duration = strdup(campos[9]);
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
    s->release_year = (campos[7][0] == '\0') ? 0 : string_para_int(campos[7]);
    for (i = 0; i <= indice_campo; i++) {
        free(campos[i]);
    }
}

void show_from_id(Show *s, int id) {
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

int compararDataTitulo(const Show *a, const Show *b) {
    int resultado;
    if (a->data_added < b->data_added){
        resultado = -1;
    }
    else if (a->data_added > b->data_added){
        resultado = 1;
    }
    else{
        resultado = strcmp_case_insensitive(a->title, b->title);
    }
    return resultado;
}

void trocaShows(Show *x, Show *y) {
    Show tmp = *x;
    *x = *y;
    *y = tmp;
}

Celula** lista_para_array() {
    Celula **array = (Celula**)malloc(tamanho * sizeof(Celula*));
    Celula *atual = primeiro->prox;
    int i = 0;
    
    while (atual != NULL) {
        array[i++] = atual;
        atual = atual->prox;
    }
    
    return array;
}

int particiona(Celula *vetor[], int esq, int dir, int *comp, int *mov) {
    Show pivo = vetor[(esq + dir) / 2]->elemento;
    int i = esq, j = dir;

    while (i <= j) {
        while (compararDataTitulo(&vetor[i]->elemento, &pivo) < 0){
            i++;
            (*comp)++;
        }
    
        while (compararDataTitulo(&vetor[j]->elemento, &pivo) > 0){
            j--;
            (*comp)++;
        }

        if (i <= j) {
            (*mov)++;
            Celula *temp = vetor[i];
            vetor[i] = vetor[j];
            vetor[j] = temp;
            i++; 
            j--;
        }
    }
    return i;
}

void quickSort(Celula *vetor[], int esq, int dir, int *comp, int *mov) {
    if (esq < dir) {
        int meio = particiona(vetor, esq, dir, comp, mov);
        quickSort(vetor, esq, meio - 1, comp, mov);
        quickSort(vetor, meio, dir, comp, mov);
    }
}

void array_para_lista(Celula **array) {
    if (tamanho == 0) return;
    primeiro->prox = array[0];
    array[0]->ant = primeiro;
    
    for (int i = 0; i < tamanho; i++) {
        if (i > 0) {
            array[i]->ant = array[i-1];
            array[i-1]->prox = array[i];
        }
        
        if (i == tamanho - 1) {
            array[i]->prox = NULL;
            ultimo = array[i];
        }
    }
}

void ordenar_lista(int *comp, int *mov) {
    if (tamanho <= 1) return;
    
    Celula **array = lista_para_array();
    quickSort(array, 0, tamanho - 1, comp, mov);
    array_para_lista(array);
    free(array);
}

void imprimir_lista() {
    Celula *atual = primeiro->prox;
    while (atual != NULL) {
        imprimir_show(&atual->elemento);
        atual = atual->prox;
    }
}

int main() {
    setlocale(LC_TIME, "C");
    char entrada[MAX_LINE];
    inicializar();
    clock_t inicio = clock();
   
    fgets(entrada, MAX_LINE, stdin);
    size_t len = strlen(entrada);
    if(len > 0 && entrada[len-1]=='\n'){
        entrada[len-1] = '\0';
    }
    
    while(!ehFim(entrada)) {
        int id = converteStr(entrada);
        Show show;
        init_show(&show);
        show_from_id(&show, id);
        inserirFim(show);
        
        fgets(entrada, MAX_LINE, stdin);
        len = strlen(entrada);
        if(len > 0 && entrada[len-1]=='\n'){
            entrada[len-1] = '\0';
        }
    }
    
    int comps = 0, mov = 0;
    ordenar_lista(&comps, &mov);
    imprimir_lista();
    
    clock_t fim = clock();
    double tempo = ((double) (fim - inicio) / CLOCKS_PER_SEC) * 1000;
    FILE* log = fopen("matricula_quicksort2.txt", "w");
    fprintf(log, "846072\t%d\t%d\t%.4lf", comps, mov, tempo);
    fclose(log);
    
    liberar_lista();
    return 0;
}