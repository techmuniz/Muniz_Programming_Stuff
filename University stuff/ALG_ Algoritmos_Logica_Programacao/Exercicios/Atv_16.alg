algoritmo "Matriz de 4 ordem"

var
   m: vetor [1..4, 1..4] de Inteiro
   l, c, sDP, p2L, mai3c: Inteiro
inicio
      sDP <- 0
      p2L <- 1                                                                   // É importante receber o valor 1, pois ele será multiplicado

      para l <- 1 ate 4 faca                                                     // Script para receber os valores da matriz
           para c <- 1 ate 4 faca
                Escreva ("Digite o valor da posição [", l, ",", c, "]: ")
                Leia (m[l,c])
                Se (l = c) entao
                   sDP <- sDP + (m[l,c])
                FimSe
           fimpara
      fimpara
      
      para l <- 1 ate 4 faca                                                     // Script para mostrar a matriz impressa na tela
           para c <- 1 ate 4 faca
                escreva (m[l,c]:5)
           fimpara
           escreval ()
      fimpara
      
                                                                                 // Script para descobrir o produto dos numeros da segunda linha (nota que a Linha foi fixa - 2 - )
      para c <- 1 ate 4 faca
           p2l <- p2l * m[2,c]
      fimpara
      
      para l <- 1 ate 4 faca                                                     // Script para descobrir qual o maior número da 3ª coluna (dessa vez é a colun que ficou fixa)
           Se (m[l,3] > mai3c) entao
              mai3c <- m[l,3]
           fimse
      fimpara
      
      escreval ("O maior valor da terceira coluna é", mai3c,"")
      escreval ("O produto dos valores da segunda linha é", p2L,"")
      escreval ("A soma dos valores da diagonal principal é", sDP,"")
fimalgoritmo