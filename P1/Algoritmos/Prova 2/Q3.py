def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        coluna = [0] * colunas
        matriz.append(coluna)
    return matriz


linhas = int(input('Informe a quantidade de linhas da matriz:'))
colunas = int(input('Informe a quantidade decolunas da matriz:'))

matriz = criar_matriz(linhas, colunas)

for i in range(linhas):
    for j in range(colunas):
        print('Informe o número da linha', i+1,', coluna', j+1, 'da matriz:', end='')
        matriz[i][j] = int(input())


maior = matriz[0][0]
for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            posicao = [i+1, j+1]

print('Maior número:', maior)
print('posição dele na matriz', posicao)