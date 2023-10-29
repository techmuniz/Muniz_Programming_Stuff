algoritmo "nome"

"1. A imobiliária Imóbilis vende apenas terrenos retangulares. Faça um algoritmo para ler as 
dimensões de um terreno e depois exibir a área do terreno."


var
    area, n1, n2: inteiro

inicio

    escreval ("Digite as dimensões do terreno - em metros")
    leia (n1)
    leia (n2)

    area <- n1 * n2

    escreval ("A área do terreno é de ",area,"m²")

fimalgoritmo
