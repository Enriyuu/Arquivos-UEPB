#include <stdio.h>
#include <locale.h>
#include <stdlib.h>

int main ()
{
    setlocale(LC_ALL, "Portuguese_Brazil");

    int MinhaIdade;
    MinhaIdade = 19;

    int MaeIdade;
    MaeIdade = 48;
                            //formas de declarar variável
    int PaiIdade = 49;

    printf("Minha idade é %d anos\nA idade da minha mãe é %d anos\nA idade do meu pai é %d anos\n",
    MinhaIdade, PaiIdade, MaeIdade);

    system("pause");
    return 0;
}