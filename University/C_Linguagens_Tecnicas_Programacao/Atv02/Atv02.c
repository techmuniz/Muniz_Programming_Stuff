

// Discipline: Algorithm and Programming Logic
// Professor: Emerson Porfírio
// Description: party
// Author: Paulo R. Muniz
// Current date: 19/09/2023

// Valor do ingresso depende de bebida, comida, decoração e pessoas

#include <stdio.h>
#include <stdlib.h>

int main() {

    float final, bebida, comida, decor;
    int qtde;

    printf ("Quanto foi gasto em bebida?");
    scanf ("%f", &bebida);

    printf ("Quanto foi gasto em comida?");
    scanf ("%f", &comida);

    printf ("Quanto foi gasto em decoracao?");
    scanf ("%f", &decor);

    printf ("Quantas pessoas foram?");
    scanf ("%d", &qtde);

    final = (bebida + comida + decor)/qtde;
    printf ("O valor por pessoa e de: %f", final);

    return 0;
}