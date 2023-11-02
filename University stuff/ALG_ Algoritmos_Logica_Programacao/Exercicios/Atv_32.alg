algoritmo "maior_numero"

"informar qual o maior dos 5 números"

var

    res, temp: real

inicio

    escreval ("Digite o primeiro número: ")
    leia (temp)

    res <- temp

    escreval ("Digite o segundo número: ")
    leia  (temp)

    se temp > res entao
        res <- temp
    fimse

    escreval ("Digite o terceiro número: ")
    leia  (temp)

    se temp > res entao
        res <- temp
    fimse

    escreval ("Digite o quarto número: ")
    leia  (temp)
    
    se temp > res entao
        res <- temp
    fimse

    escreval ("Digite o quinto número: ")
    leia  (temp)
    
    se temp > res entao
        res <- temp
    fimse

    escreval ("O maior número foi o", res)

fimalgoritmo
