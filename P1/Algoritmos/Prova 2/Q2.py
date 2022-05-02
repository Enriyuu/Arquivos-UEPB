def criar_vetor(tamanho):
    vetor = [0] * tamanho
    for i in range(tamanho):
        print('informe o valor',i+1,'do vetor:', end='')
        vetor[i] = int(input())
    return vetor

tamanho = int(input('informe o tamanho do vetor:'))

vetor1 = criar_vetor(tamanho)

vetor2 = criar_vetor(tamanho)


vetor3 = [0] * tamanho
for i in range(tamanho):
    if i % 2 == 0:
        vetor3[i] = vetor2[i]
    else:
        vetor3[i] = vetor1[i]

print(vetor3)