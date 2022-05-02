# Faça um programa que calcula o novo valor do salário de um funcionário. O usuário
# informa o salário atual (ex. 1250,00) e o percentual do reajuste (ex. 13,5 %).

salario_atual = float(input('Qual o salario atual? '))
reajuste = float(input('Qual o reajuste? '))
salario_final = salario_atual + (salario_atual * reajuste / 100)
print('O salário somado ao reajuste fica de ',salario_final)