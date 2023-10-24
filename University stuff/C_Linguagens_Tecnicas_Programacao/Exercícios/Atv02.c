
// Discipline: C Language
// Professor: Pietro Martins de Oliveira
// Description: Gather & Show Data
// Author: Paulo R. Muniz
// Current date: 10/19/2023

#include <stdio.h>
#include <stdlib.h>


int main ()
{
    char name[100];
    int age,yearBorn;
    float height;
    
    printf("What's your name? \n");
    scanf("%s", name); // Don't need to use & operator because an array is already a pointer to the first element

    printf("What's your age? \n");
    scanf("%d", &age);

    printf("What's your height?\n");
    scanf("%f", &height);

    yearBorn = 2023 - age; // Use <time.h> if want to update to current year automatically

    printf("Your name is %s, you were born in the year of %d and you are %.2fcm tall", name, yearBorn, height);

}