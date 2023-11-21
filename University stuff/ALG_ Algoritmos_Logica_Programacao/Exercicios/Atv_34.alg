Algoritmo "media"

Var
    nota1, nota2, nota3, media: real

Inicio
    Leia (nota1, nota2, nota3)
    media <- (nota1+nota2+nota3)/3
    Se (media >= 8) entao
        Escreva ("Aprovado direto com conceito A.")
    Senão
        Se (media >= 6) entao
            Escreva ("Aprovado direto com ressalvas, conceito B.")
        Senão
            Se (media > 4 ) entao
                Escreva ("Exame!!!.")
            Senão
                Escreva ("Reprovado por média.")
            Fimse
        Escreva ("Devido a esta nota, sua matrícula está liberada para transferência.")
        Fimse
    Fimse

fimalgoritmo
