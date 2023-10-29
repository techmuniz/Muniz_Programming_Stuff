algoritmo "Aula_ao_vivo_03_Exercício_02"

    '''
        Desenvolva um algoritmo que verifique se uma letra, informada pelo usuário, é F ou M.
        Caso a letra seja F, o Algoritmo deverá escrever a mensagem Feminino na tela;
        Caso a letra seja M, o Algoritmo deverá escrever a mensagem Masculino na tela;
        Caso não seja nem F nem M, Letra Inválida
        Considerar que o algoritmo desconsidera a disitnção entre Caixa Alta e Caixa Baixa
    '''


var

    letra: vetor [1..2] de caractere

inicio

    escreval ("Digite uma letra: ")
    leia (letra)

    se (letra = "f") ou (letra = "F") entao
        escreval ("F - Feminino")
    senao 
        se (letra = "m") ou (letra = "M") entao
            escreval ("M - Masculino")
        senao
            escreval ("letra inválida")
        fimse
    fimse
fimalgoritmo
