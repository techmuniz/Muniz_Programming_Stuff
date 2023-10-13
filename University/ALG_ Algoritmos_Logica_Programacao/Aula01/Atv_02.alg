algoritmo "Average Grade"

// Discipline: Algorithm and Programming Logic
// Professor: Pietro Martins de Oliveira
// Description: Final average for the four grades
// Author: Paulo R. Muniz
// Current date: 12/09/2023

var

grade01, grade02, grade03, grade04 : real

average_grade: real

inicio

escreval ("Write down the first grade: ")
leia (grade01)

escreval ("Write down the second grade: ")
leia (grade02)

escreval ("Write down the third grade: ")
leia (grade03)

escreval ("Write down the forth grade: ")
leia (grade04)

average_grade <- (grade01 + grade02 + grade03 + grade04) /4

escreva ("Your final grade is: ", average_grade)

fimalgoritmo