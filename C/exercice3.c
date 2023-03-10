#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "article.h"
#include "main.h"


Article* creer_Article() {
    Article* article = malloc(sizeof(Article));
    if (article == NULL) {
        printf("Erreur: impossible d'allouer la mémoire pour l'article\n");
        exit(EXIT_FAILURE);
    }
    strcpy(article->a_nom, "Nom par défaut");
    article->a_prix = 0.0;
    strcpy(article->a_description, "Description par défaut");
    article->a_type = DIVERS;
    return article;
}

void afficher_Article(const Article* article) {
    printf("Nom: %s\n", article->a_nom);
    printf("Prix: %.2f\n", article->a_prix);
    printf("Description: %s\n", article->a_description);
    printf("Type: ");
    switch (article->a_type) {
        case DIVERS:
            printf("Divers\n");
            break;
        case VETEMENT:
            printf("Vêtement\n");
            break;
        case NOURRITURE:
            printf("Nourriture\n");
            break;
        case LIVRE:
            printf("Livre\n");
            break;
        default:
            printf("Inconnu\n");
            break;
    }
}

void modifier_Article(Article* article) {
    printf("Entrez le nom de l'article: ");
    fgets(article->a_nom, 256, stdin);
    printf("Entrez le prix de l'article: ");
    scanf("%f", &article->a_prix);
    printf("Entrez la description de l'article: ");
    fgets(article->a_description, 1024, stdin);
    printf("Entrez le type de l'article (0=DIVERS, 1=VETEMENT, 2=NOURRITURE, 3=LIVRE): ");
    int type;
    scanf("%d", &type);
    article->a_type = (Type)type;
}

void liberer_Article(Article** article) {
    free(*article);
    *article = NULL;
}

void save_Article(const Article* article, const char* nomFichier) {
    FILE* fichier = fopen(nomFichier, "wb");
    if (fichier == NULL) {
        printf("Erreur: impossible d'ouvrir le fichier pour sauvegarde\n");
        exit(EXIT_FAILURE);
    }
    fwrite(article, sizeof(Article), 1, fichier);
    fclose(fichier);
}

void load_Article(Article* article, FILE* fichier) {
    fread(article, sizeof(Article), 1, fichier);
}



#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "article.h"

int main_Article(){
    srand(time(NULL));
    int nbArticleMax = 3; // Augmenté le nombre d'articles pour tester la boucle
    Article * tab_Article[nbArticleMax];
    for (int i = 0; i < nbArticleMax; i++){
        tab_Article[i] = creer_Article();
        afficher_Article(tab_Article[i]);
        modifier_Article(tab_Article[i]);
        afficher_Article(tab_Article[i]);
        save_Article(tab_Article[i], "Article.txt");
    }
    for (int i = 0; i < nbArticleMax; i++){
        if (tab_Article[i] != NULL) {
            liberer_Article(&tab_Article[i]);
        }
    }
    FILE* fichier = fopen("Article.txt", "w+");
    if (fichier == NULL) {
        printf("Erreur d'ouverture du fichier\n");
        return 1;
    }
    rewind(fichier);
    for (int i = 0; i < nbArticleMax; i++){
        tab_Article[i] = creer_Article();
        if (tab_Article[i] != NULL) {
            load_Article(tab_Article[i], fichier);
            afficher_Article(tab_Article[i]);
        }
    }
    fclose(fichier);
    for (int i = 0; i < nbArticleMax; i++){
        if (tab_Article[i] != NULL) {
            liberer_Article(&tab_Article[i]);
        }
    }
    return 0;
}
