#include <stdio.h>
#include <stdlib.h>

int main(){

/*
Comando simples de entrada e saída de dados:

        int idade;
        printf("Digite a idade: \n");
        scanf("%d", &idade);
        printf("A idade digitada foi = %d", idade);

        
        float senha;
        printf("Digite a senha: \n");
        scanf("%f", &senha);
        printf("A senha digitada foi %f", senha);
*/

        char nome;
        printf("Digite seu nome: \n");
        scanf("%c", &nome);
        printf("Seu nome eh: %c", nome);


}



// <comentário>
/* 
Regras para criação de identificadores:
       - Nunca começa com número
       - Case sensitive no C

Constantes variaveis e tipos de dados
           8 tipos primitivos:
               char - texto
               int - inteiros
               float - decimais
               double - decimal (precis�o dupla)
               bool - V / F
               enum - dados enumerados
               void - ausência de tipo/valor
               pointer - localização de memória

Modificadores de dados:
              unsigned - Não terá sinal
              short - reduz capacidade de armazenamento
              long - aumenta a capacidade de armazenamento

Palavras Reservadas:
         int, float, double, void, bool, char, enum
         short, long, unsigned
         if, else, do, while, for, switch, case, break, default
         return
         typedef, struct, union

Variáveis
         - Valores armazenados em memória, permite ser alterado
         - Possui sempre UM TIPO e UM NOME

Sintaxe de criação de variável:
        <tipo> <identificador>
        Pode-se declarar várias variaveis na mesma linha
       
Exemplo:
        float salario;
        int idade, ano;   // duas variaveis na mesma linha, todas s�o int
        char nomes[20];   //consegue armazenar 20 caracteres
        bool brasileiro;  //Ou é BR ou não é
        
Sintaxe para criação de constante:
        #define <identificador> <valor>
        
        exemplo:
                #define PI 3.1416
                #define MSG_ERRO "Erro!"
                
Atribui��o:
           Opera��o para armazenar ou alterar o conte�do de uma vari�vel
           Em linguagem C, usa-se o simbolo "igual":
              <vari�vel> = <valor>;
              
Express�es e operadores l�gicos ---

+ Soma 
- Subtra��o 
* Multiplica��o
/ Divis�o
% M�dulo (resto da divis�o)
() Prioridade
              

Operadores relacionais:
           > Maior que
           >= Maior ou igual
           < Menor que
           <= Menor ou igual
           == igual
           != diferent
           
Operadores L�gicos:
           ! Nega��o (inverte o valor l�gico)
           && Conjun��o "E"
           || Disjun��o "Ou"
           
----- Fun��es Intr�nsecas ----- Entrada e Sa�da de dados -----

Existem opera��es complexar que j� foram desenvolvidas em forma de fun��es

Exemplo:
        ceil(x)             - arredonda decimal
        abs(x)              - retorna valor absoluto  
        floor(x)            - Arredonda para baixo
        log (x)             - log em base 2
        long10 (x)          - log em base 10
        z = modf(x, &y)     - 
        pow (x,y)           - Exponencia��o
        sqrt (x)            - Raiz quadrada
        printf("texto")     - Imprimir texto
        scanf (%d, x)       - leitura de um dado atrav� do teclado
        
Entrada e sa�da de dados

Leitura de dados � partir do teclado (scanf)
        Sintaxe:
                scanf("<tipo_da_variavel>", &<variavel>);

Escrita de dados na tela
        Sintaxe:
                printf("texto <tipo_da_variavel>", <variavel>);

Caracteres especiais que indicam o TIPO da variavel (Que vai dentro ali do "")
           %d Imprimir/ler um int
           %f Imprimir/ler um float
           %e Imprimir/ler um double
           %c Imprimir/ler um char
           %s Imprimir/ler um vetor de char (string)

Caracteres especiais para utilizar em textos (dentro das aspas duplas)
           \n  Pula linha
           \0  Infica o fim de um texto (nulo)
           \   Indica que o pr�ximo caractere, caso seja especial, dever� ser interpretado literalmente
           ''  indica espa�o
           \t  insere uma tabula��o (tab)
           \b  retrocesso (tab)
           \f  salta de p�gina de formul�rio































        

        
           









 */