#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main ()
{
    setlocale(LC_ALL, "Portuguese_Brazil");

    int inteira = 10;
    float decimal = 10.5;
    char caractere = '?a';

    printf("%d\n", inteira);
    printf("%f\n", decimal);
    printf("%c\n", caractere);


    system("pause");
    return 0;
}