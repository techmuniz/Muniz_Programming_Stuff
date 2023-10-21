
// Discipline: C Language
// Professor: Pietro Martins de Oliveira
// Description: Receive 4 different grades and calculate the average 
// Author: Paulo R. Muniz
// Current date: 10/19/2023

#include <stdio.h>
#include <stdlib.h>

// Easy way

/*int main ()
{
    float fgrade, g1, g2, g3, g4;

    printf("Insert the first grade:\n");
    scanf("%f", &g1);

    printf("Insert the second grade:\n");
    scanf("%f", &g2);

    printf("Insert the third grade:\n");
    scanf("%f", &g3);

    printf("Insert the forth grade:\n");
    scanf("%f", &g4);

    fgrade = (g1+g2+g3+g4)/4;

    printf("Your final grade is %.2f", fgrade);    
}*/

int main ()
{

    int  nGrade;
    float total = 0, average;

    printf("To calculate the average, please insert how many grades will be inputed: ");
    scanf ("%d", &nGrade);

    for (int i = 1; i <= nGrade; i++)
    {
        float grade;
        printf("Insert grade number %d\n", i);
        scanf("%f", &grade);
        total += grade;
    }

    //printf("The total sum of all grades are %.2f\n", total); -- Testing VAR

    average = (total / nGrade);

    printf("The average is %.2f\n", average);
}