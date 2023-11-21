algoritmo "maior_numero"

"informar qual o maior dos 5 números"

var

    i, res, temp: real

inicio

    res <- 0

    para i de 1 ate 5 passo 1 faca
        Escreval ("Digite o digito de número", i)
        leia (temp)
        se temp > res entao
            res <- temp
        fimse
    fimpara

    Escreval ("O maior valor foi o", res)
fimalgoritmo

