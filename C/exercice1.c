#include <stdio.h>
#include "main.h"

double mypow(double x, int N);
double Suite(double x, unsigned N);

int main(){
    Exercice1();
    return 0;
}

void Exercice1(){
    double x;
    printf("Veuillez choisir une valeur pour x : ");
    scanf("%lf", &x);
    int N;
    printf("Veuillez choisir une valeur pour N : ");
    scanf("%d", &N);
    double result = mypow(x, N);
    printf("Le resultat est: %lf\n", result);
}

double mypow(double x, int N) {
    double result = 1.0;
    int i;
    for(i = 0; i < N; i++) {
        result *= x;
    }
    return result;
}

double Suite(double x, unsigned N) {
    double Un = x;
    double x_squared = x * x;
    int n;
    for (n = 1; n <= N; n++) {
        double term = mypow(-1, n) * mypow(x_squared, n) / (2*n - 1);
        Un += term;
    }
    return Un;
}
