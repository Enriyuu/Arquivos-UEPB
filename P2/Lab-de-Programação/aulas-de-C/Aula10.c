#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main ()
{
    setlocale(LC_ALL, "Portuguese_Brazil");

    int contador;
    int numero = 1;
    
    for (contador = 1; contador <= 10; contador = contador + 1)
    {
        printf("teste\n");
    }
    

    system("pause");
    return 0;
}