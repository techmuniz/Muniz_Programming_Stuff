algoritmo "nome1"

"Desenvolva um algoritmo que, com base no valor do IMC de uma pessoa, imprima na tela a classificação da pessoa, 
de acordo com a tabela a seguir:

Menor que 21.0 - Abaixo do peso
Entre 21.0 e 31.75 - Peso normal
Superior a 31.75 - Acima do peso
"


var
    altura, peso, imc: real

inicio
    escreval ("Insira o peso: ")
    leia (peso)

    escreval ("Insira a altura: ")
    leia (altura)

    imc <- peso/(altura*altura)

    escreval (imc)

    se imc < 21 entao
        escreval ("magro")
    senao
        se imc > 21 e imc <=31.75 entao
            escreval("Normal")
        
        senao
            se imc > 31.75 entao
                escreval ("Obeso")
            fimse
        fimse
    fimse
fimalgoritmo
