#include <stdio.h>
#include <locale.h>
#include <stdlib.h>

int main ()
{
    setlocale(LC_ALL, "Portuguese_Brazil");

    int MinhaIdade;

    MinhaIdade = 19;

    printf("Sua idade é %d anos.\n", MinhaIdade);

    system("pause");
    return 0;
}