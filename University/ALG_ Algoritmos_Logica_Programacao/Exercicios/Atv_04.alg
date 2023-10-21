algoritmo "Party"

// Discipline: Algorithm and Programming Logic
// Professor: Pietro Martins de Oliveira
// Description: party
// Author: Paulo R. Muniz
// Current date: 12/09/2023

// Valor do ingresso depende de bebida, comida, decoração e pessoas

var

food, decoration, beverage, final_value : real
people: inteiro

inicio

escreval ("How much was paid for beverage?")
leia (beverage)

escreval ("How much was paid for decoration?")
leia (decoration)

escreval ("How much was paid for food?")
leia (food)

escreval ("How many people were there?")
leia (people)

final_value <- (beverage + decoration + food) / people

escreva ("O valor gasto, por cada um foi de: ", final_value)

fimalgoritmo