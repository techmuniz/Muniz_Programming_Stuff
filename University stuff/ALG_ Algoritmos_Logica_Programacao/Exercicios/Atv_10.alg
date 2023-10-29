algoritmo "Aula_ao_vivo_03_Exercício_01"

          "Desenvolva um Algoritmo que pede para que o usuário informe dois valores inteiros, um em seguida do outro:"
          "- Caso os números sejam iguais, o algoritmo irá mostrar o resultado da MULTIPLICAÇÃO entre eles"
          "- Caso os nuemros sejam diferentes, o algoritmo irá mostrar o resultado da SOMA entre eles"


var
   n1, n2, resultado: inteiro

inicio

      escreval ("Insira os dados")
      leia (n1)
      leia (n2)
      
      SE (n1 = n2) ENTAO
         resultado <- n1 * n2
      SENAO
           resultado <- n1 + n2
      FIMSE
      
      escreva (resultado)

fimalgoritmo