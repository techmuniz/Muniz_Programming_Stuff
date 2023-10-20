// Discipline: C Language
// Professor: Pietro Martins de Oliveira
// Description: Receive deposit value; interest value; calculate profit and total value
// Author: Paulo R. Muniz
// Current date: 10/20/2023


#include <stdio.h>
#include <stdlib.h>

int main ()
    {
        float deposit, interestRate, profit, fvalue;

        printf("Insert how much money you will invest: \n");
        scanf("%f", &deposit);

        printf("Insert the interest rate: \n");
        scanf("%f", &interestRate);

        profit = deposit * (interestRate/100);
        //printf("Profit is R$%.2f", profit); //Test VAR

        fvalue = deposit + profit;
        printf("The amount of money you will profit is R$%.2f and the final value is R$%.2f.\n", profit, fvalue);

    }