





#include <stdio.h>
#include <stdlib.h>

int main() {
     int valor1 = 10;
     int valor2 = 15;
     int resultado;
     
     // resultado aqui vai ser 25
     resultado = valor1 + valor2;
     
     printf("O valor resultado eh %d \n", resultado);
     
     // resultado vai assumir 25 -3 = 22
     resultado = resultado - 3;

     printf("O valor resultado eh %d \n", resultado);
return 0;	
}