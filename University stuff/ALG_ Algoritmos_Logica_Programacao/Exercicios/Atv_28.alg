algoritmo "nome1"

"5) Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, 
imprimindo o resultado. "

var
    n1: inteiro

inicio

    Escreval ("Digite um número: ")
    leia (n1)

    SE (n1 > 0) ENTAO
        n1 <- n1 * 2
        escreval ("O dobro do seu número é", n1:2:2)
    SENAO
        n1 <- n1 * 3
        escreval ("O triplo do seu número é", n1:2:2)
    fimse
fimalgoritmo
