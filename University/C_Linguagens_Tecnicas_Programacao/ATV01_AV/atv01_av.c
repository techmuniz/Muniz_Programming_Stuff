#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main() 

{
    setlocale(LC_ALL, "Portuguese_Brazil");

    float valorInvestido = 0;
    int periodo = 0;
    float percentualRendimento = 0;

    printf("Digite o valor investido:\n");
    scanf("%f", &valorInvestido);

    printf ("Digite a quantidade de meses do investimento:\n");
    scanf("%d", &periodo);

    printf ("Digite o percentual de rendimento ao m�s:\n");
    scanf("%f", &percentualRendimento);

    /// Primeiro, criei um contador (i), e declarei as vari�veis que usei durante o script
    int i = 0;
    float saldoAtualizado = valorInvestido;
    float lucro;
    float saldoFinal;
    float imposto;


    /// Poderia ter usado a estrutura FOR, por�m quis tentar fazer usando a While
    /// Aqui, a l�gica � que enquanto o contador (i) n�o for igual ao n�mero de meses que foi inserido, o script continua sendo executado
    while (i < periodo)
    {
        i = (i + 1);
        saldoAtualizado = saldoAtualizado + (saldoAtualizado * percentualRendimento/100);
        printf ("Depois do m�s %d ter� = R$%.2f\n", i, saldoAtualizado);            

        /// Ap�s o contador (i) atingir o periodo informado, essa estrutura para de ser executada
        if (i == periodo) {
            break;
        }
    }

    /// Abaixo de cada vari�vel, coloquei uma fun��o printf() para testar se o conteudo estava correto.
    lucro = saldoAtualizado - valorInvestido;
    ///printf("Lucro: %.2f\n", lucro);

    imposto = lucro * 0.15;
    ///printf("Imposto: %.2f\n", imposto);

    saldoFinal = saldoAtualizado - imposto;
    ///printf("Saldo final: %.2f\n", saldoFinal);

    printf("O valor do saldo atualizado � de: R$%.2f. Ap�s dedu��o de 15%% em cima do lucro do rendimento, o valor final fica em R$%.2f", saldoAtualizado, saldoFinal);
}