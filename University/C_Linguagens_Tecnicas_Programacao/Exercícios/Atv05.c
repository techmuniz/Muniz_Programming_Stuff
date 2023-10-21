// Discipline: C Language
// Professor: Pietro Martins de Oliveira
// Description: Write a program that receives two numbers, calculates, and presents the result of the first number raised to the power of the second.
// Author: Paulo R. Muniz
// Current date: 10/20/2023

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main () 
{
    float  n1, n2, n3;

    printf("Input first number\n");
    scanf("%f", &n1);

    printf("Input second number\n");
    scanf("%f", &n2);

    n3 = pow(n1, n2);

    printf("The result is %.2f", n3); 

    return 0;

}