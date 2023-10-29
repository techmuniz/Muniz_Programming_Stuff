algoritmo "nome1"

"7. Entrar com o dia e o mês de uma data e informar quantos dias se passaram desde o início do 
ano. Esqueça a questão dos anos bissextos e considere sempre que um mês possui 30 dias."

var

    dia, mes, total: inteiro

inicio

    escreval ("Digite qual o dia de hoje - de 1 a 30: ")
    leia (dia)

    escreval ("Agora digite o mês - em um número de 1 à 12:")
    leia (mes)

    total <- (dia + (mes*30 -30))

    escreval ("Considerando as informações acima, já se passaram", total,"dias desde o inicio do ano")


fimalgoritmo
