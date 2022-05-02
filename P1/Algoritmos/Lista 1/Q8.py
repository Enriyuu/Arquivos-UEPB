# Faça um programa que leia um valor inteiro e mostre na tela uma sequência incluindo os
# dois números que vem antes, o número digitado, e os dois números que vem depois dele.
# Ex.: digitou 5; o programa mostra 3 4 5 6 7.

n = int(input('Digite o número '))
seq1 = n - 2
seq2 = seq1 + 1
seq3 = n
seq4 = n + 1
seq5 = seq4 + 1
print(seq1, seq2, seq3, seq4, seq5)