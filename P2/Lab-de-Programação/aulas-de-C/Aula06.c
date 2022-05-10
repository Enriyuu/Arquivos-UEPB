#include <stdio.h>
#include <locale.h>
#include <stdlib.h>

int main ()
{
    setlocale(LC_ALL, "Portuguese_Brazil");

    int MinhaIdade = 20;
    int MaeIdade = 40;
    int PaiIdade = 40;
    int IrmaoIdade = 15;

    int IdadeTotal = MinhaIdade * MaeIdade / PaiIdade * IrmaoIdade;

    printf("%d\n", IdadeTotal);

    system("pause");
    return 0;
}