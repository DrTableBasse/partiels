#include "main.h"


typedef double ElementTableau;
typedef ElementTableau* Tableau;

void permuter(ElementTableau* a, ElementTableau* b) {
    ElementTableau tmp = *a;
    *a = *b;
    *b = tmp;
}

void permuter_Tableau(Tableau tab, unsigned size) {
    if (size < 2) {
        return;
    }
    unsigned i;
    for (i = 0; i < size / 2; i++) {
        permuter(&tab[i], &tab[size - i - 1]);
    }
}

Tableau creer_Tableau(unsigned size) {
    Tableau tab = malloc(size * sizeof(ElementTableau));
    if (tab == NULL) {
        printf("Erreur d'allocation de mémoire pour le tableau\n");
        exit(1);
    }
    srand(time(NULL));
    unsigned i;
    for (i = 0; i < size; i++) {
        tab[i] = (double)rand() / RAND_MAX;
    }
    return tab;
}

void liberer_Tableau(Tableau* tab) {
    free(*tab);
    *tab = NULL;
}

void afficher(const Tableau tab, unsigned size) {
    printf("[");
    if (size > 0) {
        printf("%f", tab[0]);
        unsigned i;
        for (i = 1; i < size; i++) {
            printf(", %f", tab[i]);
        }
    }
    printf("]\n");
}

void Exercice2() {
    unsigned size = 5;
    Tableau tab = creer_Tableau(size);
    printf("Tableau initial :\n");
    afficher(tab, size);
    permuter_Tableau(tab, size);
    printf("Tableau après permutation :\n");
    afficher(tab, size);
    liberer_Tableau(&tab);
}
