algoritmo "product"

// Discipline: Algorithm and Programming Logic
// Professor: Pietro Martins de Oliveira
// Description: Calculate the amount to be paid for a product.
// Author: Paulo R. Muniz
// Current date: 12/09/2023


var

final_price, price : real
discountvalue, discountpercent, discountedvalue : real


inicio

escreval("What's the product full price?")
leia(price)

escreval("How much discount does it has?")
leia(discountvalue)

discountpercent <- discountvalue /100

discountedvalue <- price * discountpercent

final_price <- price - discountedvalue

escreval ("Final product's price with discount is: ", final_price)


fimalgoritmo