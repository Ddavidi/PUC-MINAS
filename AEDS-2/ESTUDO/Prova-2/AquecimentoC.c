/*
   ==UserScript==
 @name         LABP2Q2 - Aquecimento em C
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - LABP2Q2 - Aquecimento em C
 @author       @ddavidi_
   ==/UserScript==
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int weight;
    char name[50];
} Athlete;

bool compare(Athlete a1, Athlete a2) {
    if (a1.weight > a2.weight) {
        return true;
    } else if (a1.weight == a2.weight) {
        return (strcmp(a1.name, a2.name) < 0); // Compare names alphabetically
    }
    return false;
}

int main() {
    char name[50];
    int weight;
    int max = 2; // Start small for testing
    int currentUnit = 0;
    Athlete* athletes = malloc(max * sizeof(Athlete));

    while (scanf("%49s %d", name, &weight) == 2) {
        // Resize array if full
        if (currentUnit == max) {
            max *= 2;
            Athlete* temp = realloc(athletes, max * sizeof(Athlete));
            if (!temp) {
                perror("Realloc failed");
                free(athletes);
                return 1;
            }
            athletes = temp;
        }

        // Add athlete
        strcpy(athletes[currentUnit].name, name);
        athletes[currentUnit].weight = weight;
        currentUnit++;
    }

    // Selection sort
    for (int i = 0; i < currentUnit - 1; i++) {
        int biggest = i;
        for (int j = i + 1; j < currentUnit; j++) {
            if (compare(athletes[j], athletes[biggest])) {
                biggest = j;
            }
        }
        Athlete temp = athletes[biggest];
        athletes[biggest] = athletes[i];
        athletes[i] = temp;
    }

    // Print sorted athletes
    for (int i = 0; i < currentUnit; i++) {
        printf("%s %d\n", athletes[i].name, athletes[i].weight);
    }

    free(athletes);
    return 0;
}