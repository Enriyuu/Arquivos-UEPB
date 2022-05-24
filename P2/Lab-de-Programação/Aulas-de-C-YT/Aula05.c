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
                            //formas de declarar vari�vel
    int PaiIdade = 49;

    printf("Minha idade � %d anos\nA idade da minha m�e � %d anos\nA idade do meu pai � %d anos\n",
    MinhaIdade, PaiIdade, MaeIdade);

    system("pause");
    return 0;
}