# Questão 1 (5,0 pontos)
# Faça um algoritmo que mostre os conceitos finais dos alunos de uma classe de 75 alunos, considerando (use o comando CASO):  
# a) os dados de cada aluno (número de matrícula e nota numérica final) serão fornecidos pelo usuáriob) a 
#     tabela de conceitos segue abaixo:
# de 0,0 a 4,9 - D
# de 5,0 a 6,9 - C
# de 7,0 a 8,9 - B
# de 9,0 a 10,0 - A

for i in range(1, 76):
    print('Informe o número de matrícula do aluno',i,':',end='')
    matricula = input()
    n = float(input('Informe a sua nota final: '))
    if n >= 0 and n <= 4.9:
        print('O aluno com a matrícula', matricula, ', com a nota', n, ' pertence ao grupo D')
    if n >= 5 and n <= 6.9:
        print('O aluno com a matrícula', matricula, ', com a nota', n, ' pertence ao grupo C')
    if n >= 7 and n <= 8.9:
        print('O aluno com a matrícula', matricula, ', com a nota', n, ' pertence ao grupo B')
    if n >= 9 and n <= 10:
        print('O aluno com a matrícula', matricula, ', com a nota', n, ' pertence ao grupo A')