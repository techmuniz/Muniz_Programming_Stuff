algoritmo "matriz"

var

    mat: vetor[1..2, 1..3] de inteiro
    linha, coluna: inteiro
    
inicio
      // Primeiro, o algoritmo preenche todas as colunas da primeira linha com 1
      // depois vai para a segunda linha, e preenche todas elas com o número 1
      para linha <- 1 ate 2 faca
        para coluna <- 1 ate 3 faca
            mat [linha, coluna] <- 1
        fimpara
      fimpara

      // Essa segunda parte do código é para mostrar ao usuário, os valores da matriz,
      // para comprovar se o resultado está correto
      para linha <- 1 ate 2 faca
        para coluna <- 1 ate 3 faca
            escreva (mat [linha, coluna]: 5)
        fimpara
        escreval ()
      fimpara

fimalgoritmo


