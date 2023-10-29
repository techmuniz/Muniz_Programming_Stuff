algoritmo "nome1"

"2) Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e 
estado civil seja “CASADA”, solicitar o tempo de casada (anos)."


var
    nome: vetor [1..10] de caractere
    sexo: vetor [1..2] de caractere
    civil: vetor [1..10] de caractere 
    tcivil: inteiro

inicio

    Escreval("Digite o seu nome: ")
    leia(nome)

    Escreval("Digite o seu sexo - M ou F")
    leia(sexo)

    Escreval("Digite seu Estado Cívil - Solteiro (a) - Casado (a)")
    leia(civil)


    SE (sexo = "F") ENTAO
        SE (civil = "Casada") ENTAO
            escreval ("Por quanto tempo você é casada?")
            leia (tcivil)
        fimse
    fimse

fimalgoritmo
