n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))
n3 = float(input('Número 3: '))
n4 = float(input('Número 4: '))
n5 = float(input('Número 5: '))

maior = n1
menor = n1

if maior < n2:
  maior = n2
if maior < n3:
  maior = n3
if maior < n4:
  maior = n4
if maior < n5:
  maior = n5
if menor > n2:
  menor = n2
if menor > n3:
  menor = n3
if menor > n4:
  menor = n4
if menor > n5:
  menor = n5

soma = n1 + n2 + n3 + n4 + n5
soma -= menor
soma -= maior

media = soma/3

print('Média:', media)