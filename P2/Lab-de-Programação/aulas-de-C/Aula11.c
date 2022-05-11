#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main ()
{
    setlocale(LC_ALL, "Portuguese_Brazil");

    int contador = 1;

    while (contador <=5)
    {
        printf("%d\n", contador);
        ++contador;
    }
    

    system("pause");
    return 0;
}