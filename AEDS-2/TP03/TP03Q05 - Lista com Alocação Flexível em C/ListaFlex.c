/*
   ==UserScript==
 @name         TP03Q07 - Fila com Alocação Flexível em C
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP03Q07 - Fila com Alocação Flexível em C
 @author       @ddavidi_
   ==/UserScript==
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_STRING 1000

typedef struct {
    char *show_ID;
    char *type;
    char *title;
    char *director;
    char **cast;
    int cast_count;
    char *country;
    char *date_added;
    int release_year;
    char *rating;
    char *duration;
    char **listed_in;
    int genres_count;
} Show;

typedef struct Node {
    Show show;
    struct Node *proximo;
} Node;

typedef struct {
    Node *primeiro;
    Node *ultimo;
    int tam;
} Lista;

char* alocar_string(const char *str) {
    if (str == NULL) return NULL;
    
    char *nova_str = malloc(strlen(str) + 1);
    if (nova_str != NULL) {
        strcpy(nova_str, str);
    }
    return nova_str;
}

char** alocar_array_strings(char strings[][100], int count) {
    char **array = malloc(count * sizeof(char*));
    if (array != NULL) {
        for (int i = 0; i < count; i++) {
            array[i] = alocar_string(strings[i]);
        }
    }
    return array;
}

void liberar_array_strings(char **array, int count) {
    if (array != NULL) {
        for (int i = 0; i < count; i++) {
            free(array[i]);
        }
        free(array);
    }
}

void inicializar_show(Show *show) {
    show->show_ID = alocar_string("NaN");
    show->type = alocar_string("NaN");
    show->title = alocar_string("NaN");
    show->director = alocar_string("NaN");
    show->cast = NULL;
    show->cast_count = 0;
    show->country = alocar_string("NaN");
    show->date_added = alocar_string("NaN");
    show->release_year = 0;
    show->rating = alocar_string("NaN");
    show->duration = alocar_string("NaN");
    show->listed_in = NULL;
    show->genres_count = 0;
}

void liberar_show(Show *show) {
    free(show->show_ID);
    free(show->type);
    free(show->title);
    free(show->director);
    liberar_array_strings(show->cast, show->cast_count);
    free(show->country);
    free(show->date_added);
    free(show->rating);
    free(show->duration);
    liberar_array_strings(show->listed_in, show->genres_count);
}

void trim_string(char *str) {
    int start = 0;
    int end = strlen(str) - 1;
    
    while (str[start] == ' ' || str[start] == '\t') {
        start++;
    }
    
    while (end >= 0 && (str[end] == ' ' || str[end] == '\t')) {
        end--;
    }
    
    int i;
    for (i = 0; i <= end - start; i++) {
        str[i] = str[start + i];
    }
    str[i] = '\0';
}

int split_string(char *str, char result[][100], int max_parts) {
    int count = 0;
    char *str_copy = alocar_string(str);
    char *token = strtok(str_copy, ",");
    
    while (token != NULL && count < max_parts) {
        strcpy(result[count], token);
        trim_string(result[count]);
        token = strtok(NULL, ",");
        count++;
    }
    
    free(str_copy);
    return count;
}

void ordenar_strings(char arr[][100], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (strcmp(arr[i], arr[j]) > 0) {
                char temp[100];
                strcpy(temp, arr[i]);
                strcpy(arr[i], arr[j]);
                strcpy(arr[j], temp);
            }
        }
    }
}

int extrair_id(char *entrada) {
    int valor = 0;
    int multiplicador = 1;
    int len = strlen(entrada);
    
    for (int i = len - 1; i > 0; i--) {
        int numero = entrada[i] - '0';
        valor += numero * multiplicador;
        multiplicador *= 10;
    }
    return valor;
}

void ler_linha_csv(char *linha, Show *show) {
    char *campos[15];
    int campo_atual = 0;
    char *campo_buffer = malloc(500);
    int pos_campo = 0;
    bool dentro_aspas = false;
    
    for (int i = 0; i < 15; i++) {
        campos[i] = malloc(500);
        campos[i][0] = '\0';
    }
    
    for (int i = 0; i < strlen(linha); i++) {
        char c = linha[i];
        
        if (c == '"') {
            dentro_aspas = !dentro_aspas;
        } else if (c == ',' && !dentro_aspas) {
            campo_buffer[pos_campo] = '\0';
            strcpy(campos[campo_atual], campo_buffer);
            campo_atual++;
            pos_campo = 0;
        } else {
            campo_buffer[pos_campo] = c;
            pos_campo++;
        }
    }
    campo_buffer[pos_campo] = '\0';
    strcpy(campos[campo_atual], campo_buffer);
    liberar_show(show);
    
    show->show_ID = alocar_string(campos[0]);
    
    trim_string(campos[1]);
    if (strcmp(campos[1], "Movie") == 0 || strcmp(campos[1], "movie") == 0) {
        show->type = alocar_string("Movie");
    } else {
        show->type = alocar_string("TV Show");
    }
    
    show->title = alocar_string(campos[2]);
    if (strlen(campos[3]) == 0) {
        show->director = alocar_string("NaN");
    } else {
        show->director = alocar_string(campos[3]);
    }
    
    if (strlen(campos[4]) == 0) {
        show->cast = malloc(sizeof(char*));
        show->cast[0] = alocar_string("NaN");
        show->cast_count = 1;
    } else {
        char temp_cast[50][100];
        show->cast_count = split_string(campos[4], temp_cast, 50);
        if (show->cast_count > 1) {
            ordenar_strings(temp_cast, show->cast_count);
        }
        show->cast = alocar_array_strings(temp_cast, show->cast_count);
    }
    
    if (strlen(campos[5]) == 0) {
        show->country = alocar_string("NaN");
    } else {
        show->country = alocar_string(campos[5]);
    }
    
    if (strlen(campos[6]) == 0) {
        show->date_added = alocar_string("NaN");
    } else {
        show->date_added = alocar_string(campos[6]);
    }
    
    if (strlen(campos[7]) == 0) {
        show->release_year = 0;
    } else {
        show->release_year = atoi(campos[7]);
    }
    
    show->rating = alocar_string(campos[8]);
    show->duration = alocar_string(campos[9]);
    
    if (strlen(campos[10]) == 0) {
        show->listed_in = malloc(sizeof(char*));
        show->listed_in[0] = alocar_string("NaN");
        show->genres_count = 1;
    } else {
        char temp_genres[20][100];
        show->genres_count = split_string(campos[10], temp_genres, 20);
        if (show->genres_count > 1) {
            ordenar_strings(temp_genres, show->genres_count);
        }
        show->listed_in = alocar_array_strings(temp_genres, show->genres_count);
    }
    
    for (int i = 0; i < 15; i++) {
        free(campos[i]);
    }
    free(campo_buffer);
}

Show criar_show(char *entrada) {
    Show show;
    inicializar_show(&show);
    
    char caminho[] = "/tmp/disneyplus.csv";
    int id = extrair_id(entrada);
    FILE *arquivo = fopen(caminho, "r");
    char *linha = malloc(2000);
    int contador = 0;
    bool encontrado = false;
    
    if (arquivo != NULL) {
        while (fgets(linha, 2000, arquivo) && !encontrado) {
            if (contador == id) {
                linha[strcspn(linha, "\n")] = 0;
                ler_linha_csv(linha, &show);
                encontrado = true;
            }
            contador++;
        }
        fclose(arquivo);
    }
    
    free(linha);
    return show;
}

Show copiar_show(Show *original) {
    Show copia;
    copia.show_ID = alocar_string(original->show_ID);
    copia.type = alocar_string(original->type);
    copia.title = alocar_string(original->title);
    copia.director = alocar_string(original->director);
    copia.cast_count = original->cast_count;
    copia.country = alocar_string(original->country);
    copia.date_added = alocar_string(original->date_added);
    copia.release_year = original->release_year;
    copia.rating = alocar_string(original->rating);
    copia.duration = alocar_string(original->duration);
    copia.genres_count = original->genres_count;
    
    if (original->cast != NULL) {
        copia.cast = malloc(copia.cast_count * sizeof(char*));
        for (int i = 0; i < copia.cast_count; i++) {
            copia.cast[i] = alocar_string(original->cast[i]);
        }
    } else {
        copia.cast = NULL;
    }
    
    if (original->listed_in != NULL) {
        copia.listed_in = malloc(copia.genres_count * sizeof(char*));
        for (int i = 0; i < copia.genres_count; i++) {
            copia.listed_in[i] = alocar_string(original->listed_in[i]);
        }
    } else {
        copia.listed_in = NULL;
    }
    
    return copia;
}

void imprimir_show(Show *show) {
    printf("=> %s ## %s ## %s ## %s ## [", 
           show->show_ID, show->title, show->type, show->director);
    
    for (int i = 0; i < show->cast_count; i++) {
        printf("%s", show->cast[i]);
        if (i < show->cast_count - 1) printf(", ");
    }
    
    printf("] ## %s ## %s ## %d ## %s ## %s ## [",
           show->country, show->date_added, show->release_year, 
           show->rating, show->duration);
    
    for (int i = 0; i < show->genres_count; i++) {
        printf("%s", show->listed_in[i]);
        if (i < show->genres_count - 1) printf(", ");
    }
    
    printf("] ##\n");
}

void inicializar_lista(Lista *lista) {
    lista->primeiro = NULL;
    lista->ultimo = NULL;
    lista->tam = 0;
}

Node* criar_no(Show show) {
    Node *novo = malloc(sizeof(Node));
    if (novo != NULL) {
        novo->show = copiar_show(&show);
        novo->proximo = NULL;
    }
    return novo;
}

bool inserir_fim(Lista *lista, Show show) {
    Node *novo = criar_no(show);
    if (novo == NULL) return false;
    
    if (lista->primeiro == NULL) {
        lista->primeiro = novo;
        lista->ultimo = novo;
    } else {
        lista->ultimo->proximo = novo;
        lista->ultimo = novo;
    }
    lista->tam++;
    return true;
}

bool inserir_inicio(Lista *lista, Show show) {
    Node *novo = criar_no(show);
    if (novo == NULL) return false;
    
    if (lista->primeiro == NULL) {
        lista->primeiro = novo;
        lista->ultimo = novo;
    } else {
        novo->proximo = lista->primeiro;
        lista->primeiro = novo;
    }
    lista->tam++;
    return true;
}

Node* obter_no(Lista *lista, int pos) {
    if (pos < 0 || pos >= lista->tam) return NULL;
    
    Node *atual = lista->primeiro;
    for (int i = 0; i < pos; i++) {
        atual = atual->proximo;
    }
    return atual;
}

bool inserir_posicao(Lista *lista, Show show, int pos) {
    if (pos < 0 || pos > lista->tam) return false;
    
    if (pos == 0) return inserir_inicio(lista, show);
    if (pos == lista->tam) return inserir_fim(lista, show);
    
    Node *novo = criar_no(show);
    if (novo == NULL) return false;
    
    Node *anterior = obter_no(lista, pos - 1);
    novo->proximo = anterior->proximo;
    anterior->proximo = novo;
    
    lista->tam++;
    return true;
}

Show remover_inicio(Lista *lista) {
    Node *removido = lista->primeiro;
    Show show = copiar_show(&removido->show);
    
    lista->primeiro = removido->proximo;
    if (lista->primeiro == NULL) {
        lista->ultimo = NULL;
    }
    
    liberar_show(&removido->show);
    free(removido);
    lista->tam--;
    
    return show;
}

Show remover_fim(Lista *lista) {
    if (lista->tam == 1) {
        return remover_inicio(lista);
    }
    
    Node *anterior = obter_no(lista, lista->tam - 2);
    Node *removido = lista->ultimo;
    Show show = copiar_show(&removido->show);
    
    anterior->proximo = NULL;
    lista->ultimo = anterior;
    
    liberar_show(&removido->show);
    free(removido);
    lista->tam--;
    
    return show;
}

Show remover_posicao(Lista *lista, int pos) {
    if (pos == 0) return remover_inicio(lista);
    if (pos == lista->tam - 1) return remover_fim(lista);
    
    Node *anterior = obter_no(lista, pos - 1);
    Node *removido = anterior->proximo;
    Show show = copiar_show(&removido->show);
    
    anterior->proximo = removido->proximo;
    
    liberar_show(&removido->show);
    free(removido);
    lista->tam--;
    
    return show;
}

// Liberar toda a lista
void liberar_lista(Lista *lista) {
    Node *atual = lista->primeiro;
    while (atual != NULL) {
        Node *proximo = atual->proximo;
        liberar_show(&atual->show);
        free(atual);
        atual = proximo;
    }
    inicializar_lista(lista);
}

// Função principal
int main() {
    Lista lista;
    inicializar_lista(&lista);
    
    char *entrada = malloc(100);
    char **removidos = malloc(100 * sizeof(char*));
    int count_removidos = 0;
    
   
    while (true) {
        fgets(entrada, 100, stdin);
        entrada[strcspn(entrada, "\n")] = 0; 
        
        if (strcmp(entrada, "FIM") == 0) break;
        
        Show show = criar_show(entrada);
        inserir_fim(&lista, show);
        liberar_show(&show); 
    }
    
    int n;
    scanf("%d", &n);
    getchar(); 
    for (int i = 0; i < n; i++) {
        fgets(entrada, 100, stdin);
        entrada[strcspn(entrada, "\n")] = 0;
        
        char *entrada_copy = alocar_string(entrada);
        char *token = strtok(entrada_copy, " ");
        char *comando = alocar_string(token);
        
        if (strcmp(comando, "II") == 0) {
            token = strtok(NULL, " ");
            Show show = criar_show(token);
            inserir_inicio(&lista, show);
            liberar_show(&show);
            
        } else if (strcmp(comando, "I*") == 0) {
            // Inserir posição
            token = strtok(NULL, " ");
            int pos = atoi(token);
            token = strtok(NULL, " ");
            Show show = criar_show(token);
            inserir_posicao(&lista, show, pos);
            liberar_show(&show);
            
        } else if (strcmp(comando, "IF") == 0) {
            // Inserir fim
            token = strtok(NULL, " ");
            Show show = criar_show(token);
            inserir_fim(&lista, show);
            liberar_show(&show);
            
        } else if (strcmp(comando, "RI") == 0) {
            Show removido = remover_inicio(&lista);
            removidos[count_removidos] = alocar_string(removido.title);
            count_removidos++;
            liberar_show(&removido);
            
        } else if (strcmp(comando, "R*") == 0) {
            token = strtok(NULL, " ");
            int pos = atoi(token);
            Show removido = remover_posicao(&lista, pos);
            removidos[count_removidos] = alocar_string(removido.title);
            count_removidos++;
            liberar_show(&removido);
            
        } else if (strcmp(comando, "RF") == 0) {
            Show removido = remover_fim(&lista);
            removidos[count_removidos] = alocar_string(removido.title);
            count_removidos++;
            liberar_show(&removido);
        }
        
        free(comando);
        free(entrada_copy);
    }
    
    for (int i = 0; i < count_removidos; i++) {
        printf("(R) %s\n", removidos[i]);
        free(removidos[i]);
    }
    
    Node *atual = lista.primeiro;
    while (atual != NULL) {
        imprimir_show(&atual->show);
        atual = atual->proximo;
    }
    
    liberar_lista(&lista);
    free(entrada);
    free(removidos);
    
    return 0;
}