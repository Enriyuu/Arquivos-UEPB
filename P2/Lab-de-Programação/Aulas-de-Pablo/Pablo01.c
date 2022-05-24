#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main ()
{
    setlocale(LC_ALL, "Portuguese_Brazil");

    float nota1;
    float nota2;

    printf("Digite as duas notas:    \n");
    scanf("%f   %f", &nota1, &nota2);

    float media = (nota1+nota2)/2;

    if (media>=7)
    {
        printf("Aprovado\n");
        
    }else
    {

        printf("Reprovado\n");

    }

        printf("Sua média foi de: %.1f  \n", media);
    

    system("pause");
    return 0;
}