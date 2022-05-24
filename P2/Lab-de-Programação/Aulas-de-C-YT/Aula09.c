#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main ()
{
    setlocale(LC_ALL, "Portuguese_Brazil");

    float num1 = 5;
    float num2 = 2;
    float resultado = num1 / num2;

    printf("%f\n", resultado);

    system("pause");
    return 0;
}