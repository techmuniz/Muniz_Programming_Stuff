algoritmo "nome"

    "2. Faça um algoritmo para calcular quantas ferraduras são necessárias para equipar todos os 
    cavalos comprados para um haras. "

var
    cavalos, ferraduras: inteiro

inicio

    ferraduras <- 1

    escreval ("Quantos cavalos foram comprados?")
    leia(cavalos)

    ferraduras <- (ferraduras * cavalos) * 4

    escreval ("Será necessário um total de ", ferraduras, " para equiparem todos os cavalos")

fimalgoritmo
