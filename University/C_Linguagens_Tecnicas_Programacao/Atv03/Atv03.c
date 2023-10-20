
#include <locale.h>
#include <stdio.h>
#include <stdlib.h>

/*

int main() {
    setlocale (LC_ALL, "");

    printf("Olá mundo\n");

    float valor1;
    printf("digite o valor 1: \n");
    scanf("%f", &valor1);

    float valor2;
    printf("digite o valor 2: \n");
    scanf("%f", &valor2);

    float resultado;

    resultado = valor1 + valor2;

    printf ("O resultado foi %f", resultado);

}

*/

int main() {

    float valorProduto;
    printf ("Digite o valor do produto\n");

    scanf ("%f", &valorProduto);

    float valorDesconto = valorProduto * 0.9;

    printf ("O valor original do produto foi de %.2f e o valor com desconto foi de %2.f\n", valorProduto, valorDesconto);

}

