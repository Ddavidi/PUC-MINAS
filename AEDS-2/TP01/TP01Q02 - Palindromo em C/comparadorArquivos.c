#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 1024

// Função para ler um arquivo e retornar suas linhas em um array
char** read_file(const char* filename, int* line_count) {
    FILE* file = fopen(filename, "r");
    if (!file) {
        perror("Erro ao abrir arquivo");
        return NULL;
    }

    char** lines = NULL;
    char line[MAX_LINE_LENGTH];
    int count = 0;
    size_t capacity = 0;

    while (fgets(line, MAX_LINE_LENGTH, file) != NULL) {
        // Remove o '\n' do final da linha
        line[strcspn(line, "\n")] = 0;
        
        if (count >= capacity) {
            capacity = capacity ? capacity * 2 : 10;
            char** temp = realloc(lines, capacity * sizeof(char*));
            if (!temp) {
                perror("Erro ao alocar memória");
                fclose(file);
                return NULL;
            }
            lines = temp;
        }

        lines[count] = strdup(line);
        count++;
    }

    fclose(file);
    *line_count = count;
    return lines;
}

// Função para liberar a memória alocada para as linhas
void free_lines(char** lines, int count) {
    for (int i = 0; i < count; i++) {
        free(lines[i]);
    }
    free(lines);
}

// Função para comparar os arquivos
void compare_files(char** file1, int count1, char** file2, int count2) {
    int max_lines = count1 > count2 ? count1 : count2;
    int identical = 1;

    for (int i = 0; i < max_lines; i++) {
        const char* line1 = (i < count1) ? file1[i] : "Linha ausente";
        const char* line2 = (i < count2) ? file2[i] : "Linha ausente";

        if (strcmp(line1, line2) != 0) {
            identical = 0;
            printf("Diferença na linha %d:\n", i + 1);
            printf("Saida Esperada: %s\n", line1);
            printf("Minha saida: %s\n", line2);
            printf("-------------------\n");
        }
    }

    if (identical) {
        printf("Os arquivos são idênticos.\n");
    }
}

int main() {
    const char* file1_path = "pub.out";
    const char* file2_path = "saida.txt";

    int count1, count2;
    char** lines1 = read_file(file1_path, &count1);
    char** lines2 = read_file(file2_path, &count2);

    if (lines1 && lines2) {
        compare_files(lines1, count1, lines2, count2);
    }

    if (lines1) free_lines(lines1, count1);
    if (lines2) free_lines(lines2, count2);

    return 0;
}