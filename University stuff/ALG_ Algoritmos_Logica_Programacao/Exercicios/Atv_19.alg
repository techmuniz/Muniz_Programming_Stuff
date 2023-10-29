algoritmo "nome1"

"6. O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição. Escreva um algoritmo 
que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar. Assuma que a 
balança já desconte o peso do prato."


var

    pesoTotal, preco: real

inicio

    escreval ("Digite o peso do prato montado: ")
    leia(pesoTotal)

    preco <- (pesoTotal*12)

    escreval("O valor total a pagar é de R$", preco:2:2, ".")

fimalgoritmo
