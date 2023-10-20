// Discipline: C Language
// Professor: Pietro Martins de Oliveira
// Description: Show number before and after
// Author: Paulo R. Muniz
// Current date: 10/09/2023

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int number, previous, next;

    printf("Input a number &(intenger): \n");
    scanf("%d", &number);

    previous = number--;
    next = number++;

    printf("The previous number is %d and the next one is %d", previous, next);


}