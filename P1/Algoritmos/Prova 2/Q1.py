def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        coluna = [0] * colunas
        matriz.append(coluna)
    return matriz

def matriz_transposta(matriz, linhas, colunas):
    matriz2 = criar_matriz(colunas, linhas)
    for i in range(0, linhas):
        for j in range(0, colunas):
            matriz2[j][i] = matriz[i][j]
    return matriz2



linhas = int(input('Informe a quantidade de linhas da matriz:'))
colunas = int(input('Informe a quantidade decolunas da matriz:'))

matriz = criar_matriz(linhas, colunas)

for i in range(linhas):
    for j in range(colunas):
        print('Informe o número da linha', i+1,', coluna', j+1, 'da matriz:', end='')
        matriz[i][j] = int(input())


transposta = matriz_transposta(matriz, linhas, colunas)


for i in matriz:
    print(i)
for i in transposta:
    print(i)