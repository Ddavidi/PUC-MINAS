/*
   ==UserScript==
 @name         TP02Q10 - Quicksort em C
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP02Q10 - Quicksort em C
 @author       @ddavidi_
   ==/UserScript==
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_CAST 100
#define MAX_LISTED_IN 100
#define MAX_STRING 200
#define MAX_SHOWS 1370
#define MAX_PARTES 12

// Estrutura para representar uma data
typedef struct {
    char month[20];
    int day;
    int year;
} Date;

//Setters
void setMonth(Date* data, char* month) {snprintf(data->month, sizeof(data->month), "%s", month);}
void setDay(Date* data, int day) {data->day = day;}
void setYear(Date* data, int year) {data->year = year;}

//Getters
char* getMonth(Date* data) {return data->month;}
int getDay(Date* data) {return data->day;}
int getYear(Date* data) {return data->year;}

// Funções para manipular a estrutura Date
Date newDate() {
    Date date = {"March", 1, 1900};
    return date;
}

Date* initDate(int day, int year,char* month) {
    Date* data = (Date*)malloc(sizeof(Date));
    if (data != NULL) {
        data->day = day;
        data->year = year;
        snprintf(data->month, sizeof(data->month), "%s", month);
    }
    return data;
}

Date parseDate(const char* date_str) {
    Date date = newDate();
    if (date_str == NULL || strlen(date_str) == 0 || strcmp(date_str, "NaN") == 0) {
        return date;
    }

    sscanf(date_str, "%s %d, %d", date.month, &date.day, &date.year);
    return date;
}

char* dateToString(Date* date) {
    char* str = (char*)malloc(30 * sizeof(char));
    snprintf(str, 30, "%s %d, %d", date->month, date->day, date->year);
    return str;
}


void freeDate(Date* data) {
    if (data != NULL) {
        free(data);
        data = NULL;
    }
}

// Estrutura para representar um Show
typedef struct {
    char show_id[20];
    char type[50];
    char title[100];
    char director[100];
    char cast[MAX_CAST][50];
    int cast_count;
    char country[50];
    Date date_added;
    int release_year;
    char rating[10];
    char duration[30];
    char listed_in[MAX_LISTED_IN][50];
    int listed_count;
    char description[MAX_STRING];
} Show;

//Getters
char* getShowId(Show* show) {return show->show_id;}
char* getType(Show* show) {return show->type;}
char* getTitle(Show* show) {return show->title;}
char* getDirector(Show* show) {return show->director;}
char (*getCast(Show* show))[20] {return (show != NULL) ? show->cast : NULL;}
char* getCountry(Show* show) {return show->country;}
char* getDateAdded(Show* show) {return dateToString(&show->date_added);}
int getReleaseYear(Show* show) {return show->release_year;}
char* getRating(Show* show) {return show->rating;}
char* getDuration(Show* show) {return show->duration;}
char (*getListedIn(Show* show))[20] {return (show != NULL) ? show->listed_in : NULL;}
char* getDescription(Show* show) {return show->description;}

//Setters
void setShowId(Show* show, char* show_id) {snprintf(show->show_id, sizeof(show->show_id), "%s", show_id);}
void setType(Show* show, char* type) {snprintf(show->type, sizeof(show->type), "%s", type);}
void setTitle(Show* show, char* title) {snprintf(show->title, sizeof(show->title), "%s", title);}
void setDirector(Show* show, char* director) {snprintf(show->director, sizeof(show->director), "%s", director);}
void setCast(Show* show, char cast[][20], int size) {
    for (int i = 0; i < size; i++) {
        snprintf(show->cast[i], sizeof(show->cast[i]), "%s", cast[i]);
    }
}
void setCountry(Show* show, char* country) {snprintf(show->country, sizeof(show->country), "%s", country);}
void setDateAdded(Show* show, Date* date_added) {show->date_added = *date_added;}
void setReleaseYear(Show* show, int release_year) {show->release_year = release_year;}
void setRating(Show* show, char* rating) {snprintf(show->rating, sizeof(show->rating), "%s", rating);}
void setDuration(Show* show, char* duration) {snprintf(show->duration, sizeof(show->duration), "%s", duration);}
void setListedIn(Show* show, char listed_in[][20], int size) {
    for (int i = 0; i < size; i++) {
        snprintf(show->listed_in[i], sizeof(show->listed_in[i]), "%s", listed_in[i]);
    }
}
void setDescription(Show* show, char* description) {snprintf(show->description, sizeof(show->description), "%s", description);}

// Funções para manipular a estrutura Show
Show* newShow() {
    Show* show = (Show*)malloc(sizeof(Show));
    if (show != NULL) {
        snprintf(show->show_id, sizeof(show->show_id), "NaN");
        snprintf(show->type, sizeof(show->type), "NaN");
        snprintf(show->title, sizeof(show->title), "NaN");
        snprintf(show->director, sizeof(show->director), "NaN");
        show->cast_count = 0;
        snprintf(show->country, sizeof(show->country), "NaN");
        show->date_added = newDate();
        show->release_year = 1900;
        snprintf(show->rating, sizeof(show->rating), "NaN");
        snprintf(show->duration, sizeof(show->duration), "NaN");
        show->listed_count = 0;
        snprintf(show->description, sizeof(show->description), "NaN");
    }
    return show;
}

Show* initShow(char* show_id, char* type, char* title, char* director, char* country, Date* date_added, int release_year, char* rating, char* duration, char* description) {
    Show* show = (Show*)malloc(sizeof(Show));
    if (show != NULL) {
        snprintf(show->show_id, sizeof(show->show_id), "%s", show_id);
        snprintf(show->type, sizeof(show->type), "%s", type);
        snprintf(show->title, sizeof(show->title), "%s", title);
        snprintf(show->director, sizeof(show->director), "%s", director);
        snprintf(show->country, sizeof(show->country), "%s", country);
        show->date_added = parseDate(date_added);
        show->release_year = release_year;
        snprintf(show->rating, sizeof(show->rating), "%s", rating);
        snprintf(show->duration, sizeof(show->duration), "%s", duration);
        snprintf(show->description, sizeof(show->description), "%s", description);
    }
    return show;
}

void freeShow(Show* show) {
    if (show != NULL) {
        free(show);
    }
}

Show* cloneShow(const Show* original) {
    if (original == NULL) return NULL;
    
    Show* clone = newShow();
    if (clone != NULL) {
        snprintf(clone->show_id, sizeof(clone->show_id), "%s", original->show_id);
        snprintf(clone->type, sizeof(clone->type), "%s", original->type);
        snprintf(clone->title, sizeof(clone->title), "%s", original->title);
        snprintf(clone->director, sizeof(clone->director), "%s", original->director);
        for (int i = 0; i < original->cast_count; i++) {
            snprintf(clone->cast[i], sizeof(clone->cast[i]), "%s", original->cast[i]);
        }
        clone->cast_count = original->cast_count;
        snprintf(clone->country, sizeof(clone->country), "%s", original->country);
        clone->date_added = original->date_added;
        clone->release_year = original->release_year;
        snprintf(clone->rating, sizeof(clone->rating), "%s", original->rating);
        snprintf(clone->duration, sizeof(clone->duration), "%s", original->duration);
        for (int i = 0; i < original->listed_count; i++) {
            snprintf(clone->listed_in[i], sizeof(clone->listed_in[i]), "%s", original->listed_in[i]);
        }
        clone->listed_count = original->listed_count;
        snprintf(clone->description, sizeof(clone->description), "%s", original->description);
    }
    return clone;
}

void swapChar(char* a, char* b) {
    char temp[50];
    strcpy(temp, a);
    strcpy(a, b);
    strcpy(b, temp);
}

void ordenarCast(char cast[MAX_CAST][50], int count) {
    for (int i = 0; i < count - 1; i++) {
        int menor = i;
        for (int j = i + 1; j < count; j++) {
            if (strcmp(cast[j], cast[menor]) < 0) {
                menor = j;
            }
        }
        if (menor != i) {
            swapChar(cast[i], cast[menor]);
        }
    }
}

void trim(char *str) {
    int start = 0, end = strlen(str) - 1;
    
    // Avança enquanto for espaço no início
    while (isspace((unsigned char)str[start])) {
        start++;
    }
    
    // Retrocede enquanto for espaço no fim
    while (end >= start && isspace((unsigned char)str[end])) {
        end--;
    }
    
    // Move a string para o início
    int i = 0;
    while (start <= end) {
        str[i++] = str[start++];
    }
    
    str[i] = '\0'; // Termina a string
}

void replace_char(char *str, char antigo) {
    int i, j;
    for (i = 0, j = 0; str[i] != '\0'; i++) {
        if (str[i] != antigo) {
            str[j++] = str[i];
        }
    }
    str[j] = '\0';
}

void lerShow(Show* show, const char* linha) {
    char partes[MAX_PARTES][MAX_STRING];
    int parte_idx = 0;
    
    const char* start = linha;
    int in_quotes = 0;
    
    // Divide a linha em partes, considerando aspas e vírgulas
    for (const char* p = linha; *p; p++) {
        if (*p == '"') {
            in_quotes = !in_quotes;
        } else if (*p == ',' && !in_quotes) {
            strncpy(partes[parte_idx], start, p - start);
            partes[parte_idx][p - start] = '\0';
            replace_char(partes[parte_idx], '"'); // Remove aspas
            trim(partes[parte_idx]); // Remove espaços em branco
            parte_idx++;
            start = p + 1;
        }
    }
    strncpy(partes[parte_idx], start, strlen(start));
    partes[parte_idx][strlen(start)] = '\0';
    replace_char(partes[parte_idx], '"'); // Remove aspas
    
    // Preenche os campos do Show, atribuindo "NaN" para valores vazios
    snprintf(show->show_id, sizeof(show->show_id), "%s", strlen(partes[0]) > 0 ? partes[0] : "NaN");
    snprintf(show->type, sizeof(show->type), "%s", strlen(partes[1]) > 0 ? partes[1] : "NaN");
    snprintf(show->title, sizeof(show->title), "%s", strlen(partes[2]) > 0 ? partes[2] : "NaN");
    snprintf(show->director, sizeof(show->director), "%s", strlen(partes[3]) > 0 ? partes[3] : "NaN");
    
    // Processa o elenco
    char* cast_raw = partes[4];
    if (strlen(cast_raw) > 0) {
        char* token = strtok(cast_raw, ",");
        trim(token);
        while (token != NULL && show->cast_count < MAX_CAST) {
            snprintf(show->cast[show->cast_count++], sizeof(show->cast[0]), "%s", token);
            trim(show->cast[show->cast_count - 1]); // Remove espaços em branco
            token = strtok(NULL, ",");
        }
        ordenarCast(show->cast, show->cast_count);
    } else {
        snprintf(show->cast[0], sizeof(show->cast[0]), "NaN"); // Preenche com "NaN"
        show->cast_count = 1;
    }
    
    snprintf(show->country, sizeof(show->country), "%s", strlen(partes[5]) > 0 ? partes[5] : "NaN");
    show->date_added = strlen(partes[6]) > 0 ? parseDate(partes[6]) : newDate();
    show->release_year = strlen(partes[7]) > 0 ? atoi(partes[7]) : 1900;
    snprintf(show->rating, sizeof(show->rating), "%s", strlen(partes[8]) > 0 ? partes[8] : "NaN");
    snprintf(show->duration, sizeof(show->duration), "%s", strlen(partes[9]) > 0 ? partes[9] : "NaN");
    
    // Processa os gêneros
    char* listed_raw = partes[10];
    if (strlen(listed_raw) > 0) {
        char* token = strtok(listed_raw, ",");
        trim(token);
        while (token != NULL && show->listed_count < MAX_LISTED_IN) {
            snprintf(show->listed_in[show->listed_count++], sizeof(show->listed_in[0]), "%s", token);
            trim(show->listed_in[show->listed_count - 1]); // Remove espaços em branco
            token = strtok(NULL, ",");
        }
    } else {
        snprintf(show->listed_in[0], sizeof(show->listed_in[0]), "NaN"); // Preenche com "NaN"
        show->listed_count = 1;
    }
    
    snprintf(show->description, sizeof(show->description), "%s", strlen(partes[11]) > 0 ? partes[11] : "NaN");
}

Show* lerArquivo(const char* filename, int* total) {
    FILE* file = fopen(filename, "r");
    if (!file) {
        perror("Erro ao abrir o arquivo");
        return NULL;
    }
    
    Show* shows = (Show*)malloc(MAX_SHOWS * sizeof(Show));
    if (!shows) {
        fclose(file);
        return NULL;
    }
    
    char linha[1024];
    int index = 0;
    
    fgets(linha, sizeof(linha), file); // Pula o cabeçalho
    while (fgets(linha, sizeof(linha), file) && index < MAX_SHOWS) {
        linha[strcspn(linha, "\r\n")] = '\0'; // Remove newline
        lerShow(&shows[index++], linha);
    }
    
    fclose(file);
    *total = index;
    return shows;
}

void imprimirShow(const Show* show) {
    printf("=> %s ## %s ## %s ## %s ## [", show->show_id, show->title, show->type, show->director);
    for (int i = 0; i < show->cast_count; i++) {
        printf("%s", show->cast[i]);
        if (i < show->cast_count - 1) printf(", ");
    }
    printf("] ## %s ## %s %d, %04d ## %d ## %s ## %s ## [", show->country, show->date_added.month,
        show->date_added.day, show->date_added.year, show->release_year, show->rating, show->duration);
        for (int i = 0; i < show->listed_count; i++) {
            printf("%s", show->listed_in[i]);
            if (i < show->listed_count - 1) printf(", ");
        }
    printf("] ##\n");
}

void toLowerString(const char* src, char* dest) {
    int i = 0;
    while (src[i]) {
        dest[i] = tolower((unsigned char)src[i]);
        i++;
    }
    dest[i] = '\0';
}

void swapShow(Show *a, Show *b) {
    Show temp = *a;
    *a = *b;
    *b = temp;
}

int getMonthNumber(const char* month) {
    const char* months[] = {
        "january", "february", "march", "april", "may", "june",
        "july", "august", "september", "october", "november", "december"
    };

    char lowerMonth[20];
    toLowerString(month, lowerMonth);

    for (int i = 0; i < 12; i++) {
        if (strcmp(lowerMonth, months[i]) == 0) {
            return i + 1;
        }
    }
    return 0; // Mês inválido
}

int compareDates(Show* a, Show* b) {
    int yearA = a->date_added.year;
    int yearB = b->date_added.year;
    if (yearA != yearB) return yearA - yearB;

    int monthA = getMonthNumber(a->date_added.month);
    int monthB = getMonthNumber(b->date_added.month);
    if (monthA != monthB) return monthA - monthB;

    return a->date_added.day - b->date_added.day;
}

int compareShowByDate(Show* a, Show* b) {
    int dateCmp = compareDates(a, b);
    if (dateCmp != 0) return dateCmp;

    // Desempate por title (case-insensitive)
    char titleA[256], titleB[256];
    toLowerString(a->title, titleA);
    toLowerString(b->title, titleB);
    return strcmp(titleA, titleB);
}


int partition(Show* array, int low, int high) {
    Show pivot = array[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (compareShowByDate(&array[j], &pivot) <= 0) {
            i++;
            swapShow(&array[i], &array[j]);
        }
    }

    swapShow(&array[i + 1], &array[high]);
    return i + 1;
}

void quicksort(Show* array, int low, int high) {
    if (low < high) {
        int pivotIndex = partition(array, low, high);
        quicksort(array, low, pivotIndex - 1);
        quicksort(array, pivotIndex + 1, high);
    }
}


int main() {
    int total = 0;
    Show* shows = lerArquivo("/tmp/disneyplus.csv", &total);
    if (!shows) {
        return 1;
    }

    Show* arr = (Show*)malloc(MAX_SHOWS * sizeof(Show));
    for(int j = 0; j < MAX_SHOWS; j++) {
        arr[j] = *newShow(); // Inicializa com valores padrão
    }
    int i = 0;
    

    char entrada[10];
    scanf("%s", entrada);
    while (strcmp(entrada, "FIM") != 0) {
        int index = atoi(entrada + 1) - 1;
        if (index >= 0 && index < total) {
            arr[i] = shows[index];
            i++;
        } else {
            printf("Índice inválido.\n");
        }
        scanf("%s", entrada);
    }

    quicksort(arr, 0, i - 1);

    for (int j = 0; j < i; j++) {
        if (strcmp(arr[j].show_id, "NaN") != 0) {
            imprimirShow(&arr[j]);
        }
    }
    
    free(shows);

    return 0;
}