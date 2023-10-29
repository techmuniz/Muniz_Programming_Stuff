algoritmo "nome1"

"9. Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo 
vendida respectivamente por 10, 12 e 15 reais. Construa um algoritmo em que o usuário forneça a 
quantidade de camisetas pequenas, médias e grandes referentes a uma venda, e a máquina 
informe quanto será o valor arrecadado."

var
    p, m, g: inteiro
    preco: real

inicio
    escreval ("Digite quantas camisetas tamnho pequeno foram vendidas: ")
    leia(p)

    escreval ("Digite quantas camisetas tamnho médio foram vendidas: ")
    leia(m)

    escreval ("Digite quantas camisetas tamnho grande foram vendidas: ")
    leia(g)

    p <- (p*10)
    m <- (m*12)
    g <- (g*15)

    preco <- (p + m + g)

    escreval ("O preço final é de R$", preco:2:2)


fimalgoritmo
