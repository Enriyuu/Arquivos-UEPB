contador = 10
lista_de_filmes = []
for i in range(0, contador):
    print('Informe o filme', i+1, 'disponível: ', end='')
    filme = input()
    lista_de_filmes.append(filme)
def filmes_assistidos(lista_de_filmes):
    lista = []
    for i in range(contador):
        print('Você já assistiu o filme', lista_de_filmes[i],'?', end='')
        assistiu = input()
        if assistiu == 'sim': 
            lista.append(True)
        else:
            lista.append(False)
    return lista
usuario1 = input('Informe o nome do usuario 1: ')
lista_usuario1 = filmes_assistidos(lista_de_filmes)
usuario2 = input('Informe o nome do usuario 2: ')
lista_usuario2 = filmes_assistidos(lista_de_filmes)
print('Lista de filmes recomendados para o usuário', usuario1)
for i in range(contador):
    if lista_usuario1[i] == False and lista_usuario2[i] == True:
        print(lista_de_filmes[i], end=' | ')
print('Lista de filmes recomendados para o usuário', usuario2)
for i in range(contador):
    if lista_usuario2[i] == False and lista_usuario1[i] == True:
        print(lista_de_filmes[i], end=' | ')