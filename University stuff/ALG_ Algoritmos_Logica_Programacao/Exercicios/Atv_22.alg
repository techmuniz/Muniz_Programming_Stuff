algoritmo "nome1"

"12. Faça um algoritmo para ler o salário de um funcionário e aumentá-Io em 15%. Após o aumento, 
desconte 8% de impostos. Imprima o salário inicial, o salário com o aumento e o salário final."


var

    salarioInicial, salarioAumento, salarioFinal: real


inicio

    escreval ("Digite o salário atual do funcionário: ")
    leia (salarioInicial)

    salarioAumento <- (salarioInicial + (salarioInicial*0.15))
    escreval ("O salário com aumento fica em R$", salarioAumento)

    salarioFinal <- (salarioAumento - (salarioAumento*0.08))
    escreval ("O salário final, depois do desconto fica em R$", salarioFinal)

fimalgoritmo
