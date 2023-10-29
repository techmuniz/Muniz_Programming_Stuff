algoritmo "nome1"


"16. A lanchonete Gostosura vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias de 
queijo, uma fatia de presunto e uma rodela de hambúrguer. Sabendo que cada fatia de queijo ou 
presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas, faça um algoritmo em 
que o dono forneça a quantidade de sanduíches a fazer, e a máquina informe as quantidades (em 
quilos) de queijo, presunto e carne necessários para compra. "

var

    hamb: inteiro
    queijo, pres, carne: real
    
inicio

    escreval ("Digite quantos hambúrgueres você deseja fazer: ")
    leia (hamb)

    queijo <- hamb * 100
    pres <- hamb * 50
    carne <- hamb * 100

    escreval ("Você irá precisa de", queijo:2:2, "g de Queijo, ", pres:2:2, "g de presunto, e ", carne:2:2,"g de carne")
fimalgoritmo
