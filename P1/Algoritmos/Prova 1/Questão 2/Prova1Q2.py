# Questão 2 (5,0 pontos)
# Escrever um algoritmo que lê 5 pares de valores a, b, todos inteiros e positivos, um par de cada vez.
# Caso a < b, escreva os inteiros pares de a até b, incluindo o a e o b se forem pares.

for i in range(0, 5):
    a = int(input('Digite o primeiro valor a:'))
    b = int(input('Digite o primeiro valor b:'))

    if a % 2 == 0 and a < b:
        for i in range(a, b+1, 2):
            print(i)
    else:
        for i in range(a, b, 2):
            print(i+1)