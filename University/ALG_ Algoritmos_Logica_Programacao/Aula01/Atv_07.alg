algoritmo "Number"

// Discipline: Algorithm and Programming Logic
// Professor: Pietro Martins de Oliveira
// Description: Read a number and show the one after and the one before
// Author: Paulo R. Muniz
// Current date: 12/09/2023


var

number, nBefore, nAfter : inteiro

inicio

escreval ("Give me an intenger number:")
leia (number)

nBefore <- number - 1
nAfter <- number + 1

escreval ("The predecessor of number ", number, " is number ", nBefore, ". And the next is ", nAfter)


fimalgoritmo