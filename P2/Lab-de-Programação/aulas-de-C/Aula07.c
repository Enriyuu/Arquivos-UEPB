#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main ()
{
    setlocale(LC_ALL, "Portuguese_Brazil");

    int base;
    int altura;
    int area;
    
    printf("Digite o valor da base: ");
    scanf("%d", &base);

    printf("Digite o valor da altura: ");
    scanf("%d", &altura);

    area = base * altura;

    printf("O valor da área do retângulo é = %d\n", area);

    system("pause");
    return 0;
}