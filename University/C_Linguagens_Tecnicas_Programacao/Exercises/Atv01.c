
// Discipline: C Language
// Professor: Pietro Martins de Oliveira
// Description: sum two numbers and show result
// Author: Paulo R. Muniz
// Current date: 10/18/2023



#include <stdio.h>
#include <stdlib.h>

int main() {
     float value1, value2, result;
     
     printf("Input the first number:\n");
     scanf("%f", &value1);

     printf("Input the second number:\n");
     scanf("%f", &value2);

     result = (value1 + value2);

     printf("The result is %.2f", result);
}