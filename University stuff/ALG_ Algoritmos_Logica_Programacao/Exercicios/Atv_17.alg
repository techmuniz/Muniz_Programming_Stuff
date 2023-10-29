algoritmo "nome1"

"4. Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos dias de vida 
ela possui. Considere sempre anos completos, e que um ano possui 365 dias. Ex: uma pessoa 
com 19 anos possui 6935 dias de vida; veja um exemplo de saída: MARIA, VOCÊ JÁ VIVEU 6935 
DIAS"


var

    nome: vetor [1..10] de caractere
    idade, tempVida: inteiro

inicio

    Escreval ("Digite seu nome:")
    leia (nome)

    Escreval ("Digite sua idade:")
    leia (idade)

    tempVida <- (idade * 365)

    escreval (nome, " você já viveu ", tempVida," dias")

    SE (tempVida > 10000) ENTAO
        escreval ("Tá ficando velho!")
        
    SENAO
        SE (tempVida < 10000) E (tempVida > 8000) ENTAO
            escreval ("Tá quase velho!")

        SENAO
            escreval ("Tá novo!")
        fimse
    fimse

fimalgoritmo
