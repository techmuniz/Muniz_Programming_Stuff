algoritmo "nome1"

"7) Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar, 
imprimir o resultado desta operação. "

var
    n1: inteiro

inicio

    escreval ("Digite um número: ")
    leia (n1)

    Se (n1 % 2 = 0) ENTAO
        n1 <- n1 + 5
        escreval(n1)
    senao
        n1 <- n1 + 8
        escreval(n1)
    fimse

fimalgoritmo
