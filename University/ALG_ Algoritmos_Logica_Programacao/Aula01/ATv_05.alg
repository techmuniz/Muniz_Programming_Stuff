algoritmo "Gather some Data"

// Discipline: Algorithm and Programming Logic
// Professor: Pietro Martins de Oliveira
// Description: Gather some Data from User
// Author: Paulo R. Muniz
// Current date: 12/09/2023


var

telephone, name : vetor [1.. 15] de caractere
age : inteiro
height: real

inicio

escreval ("Tell me your name:")
leia (name)

escreval ("Your age:")
leia (age)

escreval ("Your height - in CM:")
leia (height)

escreval ("Your telephone number:")
leia (telephone)

escreva ("Your name is ", name, ", you have ", age, " and you are ", height, " cm height. Also your phone number is ", telephone)

fimalgoritmo