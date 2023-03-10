#ifndef ARTICLE_H
#define ARTICLE_H
#include <stdio.h>

typedef enum {
    DIVERS,
    VETEMENT,
    NOURRITURE,
    LIVRE
} Type;

typedef struct {
    char a_nom[256];
    float a_prix;
    char a_description[1024];
    Type a_type;
} Article;

/* Déclaration des fonctions */
Article* creer_Article();
void afficher_Article(const Article*);
void modifier_Article(Article*);
void liberer_Article(Article**);
void save_Article(const Article*, const char*);
void load_Article(Article*, FILE*);

#endif /* ARTICLE_H */
