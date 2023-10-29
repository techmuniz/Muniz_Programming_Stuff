algoritmo "padeiro"


var

    p1, p2, soma, poupanca, totalp1, totalp2: real

inicio

    escreval ("Quantos pãezinhos foram vendidos no dia? ")
    leia (p1)

    escreval ("Quantas broas foram vendidas no dia? ")
    leia (p2)

    totalp1 <- (p1 * 0.12)
    totalp2 <- (p2 *1.50)
    soma <- (totalp1 + totalp2)
    poupanca <- (soma * 0.1)

    escreval ("No final do dia, você vendeu R$",soma:2:2,", e deve guardar R$", poupanca:2:2,".")


fimalgoritmo
