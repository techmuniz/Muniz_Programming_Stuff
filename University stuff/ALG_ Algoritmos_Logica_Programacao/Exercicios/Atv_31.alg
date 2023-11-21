algoritmo "Tabuada do 3"


var

    n1, n2: real
    i: inteiro

inicio

    escreval ("Escreva o número que você deseja ver a tabuada: ")
    leia (n1)

    Para i de 1 ate 10 passo 1 faca
        n2 <- n1 * i
        escreval (n1, "*", i, "=", n2)
    fimpara


fimalgoritmo
