algoritmo "Activity01"

// Discipline: Algorithm and Programming Logic
// Professor: Pietro Martins de Oliveira
// Description: Read and display name, age, weight, height, country and phone number
// Author: Paulo R. Muniz
// Current date: 10/09/2023
// Program is in Portuguese-BR (PT_BR) as it is the language used in the class

var
    // Declaration of variables
    country, phone, name : vetor [1..10] de caractere
    age : inteiro
    weight, height : real

inicio
    // Input of data
    escreva ("Tell me your name: ")
    leia (name)
    escreva ("Tell me your age: ")
    leia (age)
    escreva ("Tell me your weight: ")
    leia (weight)
    escreva ("Tell me your height: ")
    leia (height)
    escreva ("Tell me your country: ")
    leia (country)
    escreva ("Tell me your phone number: ")
    leia (phone)
    escreva ("Your name is: ", name, " and you are ", age, " years old. Your weight is ", weight,"kg",  " and your height is ", height, ". You live in ", country, " and your phone number is ", phone)
fimalgoritmo

