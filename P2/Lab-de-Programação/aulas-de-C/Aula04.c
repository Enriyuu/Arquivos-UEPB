#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main ()
{
    setlocale(LC_ALL, "Portuguese_Brazil");

    int MinhaIdade;

    MinhaIdade = 19;

    printf("Sua idade � %d anos.\n", MinhaIdade);


    system("pause");
    return 0;
}