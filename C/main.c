#include <stdio.h>

#include "main.h"



int main(void)
{
    int choix;
    // Déclarez une variable booléenne pour indiquer si l'utilisateur souhaite quitter le programme ou non
    int quitter = 0;

    // Utilisez une boucle do-while pour afficher le menu à l'écran et demander à l'utilisateur de saisir son choix
    do
    {
        printf("Menu :\n");
        printf("1. Exo 1 \n");
        printf("2. Exo 2\n");
        printf("3. Exo 3\n");


        printf("Votre choix : ");
        scanf("%d", &choix);

        // Utilisez une instruction switch pour exécuter le code correspondant à l'option choisie
        switch (choix)
        {
            case 1:
                // Inclure le fichier option1.c dans votre programme
                Exercice1();
                break;
            case 2:
                // Inclure le fichier option2.c dans votre programme
                Exercice2();
                break;
            case 3:
                // Inclure le fichier option2.c dans votre programme
                Exercice3();
                break;

            case 4:
                // Mettez la variable quitter à 1 pour indiquer que l'utilisateur souhaite quitter le programme
                quitter = 1;
                break;
            default:
                printf("Choix non valide\n");
                break;
        }
    }
    // Utilisez la variable quitter dans la condition de la boucle pour savoir quand arrêter de boucler
    while (!quitter);

    return 0;
}
