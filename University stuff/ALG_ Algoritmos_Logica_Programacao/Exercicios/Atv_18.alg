algoritmo "nome1"

"5. Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para ler o 
preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no 
tanque. "

var

    preco, pagamento, litros: real


inicio

    escreval ("Qual o valor do litro da gasolina?")
    leia (preco)

    escreval ("Quanto deu o total do pagamento?")
    leia (pagamento)

    litros <- (pagamento/preco)

    escreval ("Você conseguiu colocar cerca de ", litros:0:2, "lt de gasolina")

fimalgoritmo
