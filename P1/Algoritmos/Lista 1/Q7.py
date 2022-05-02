# Faça um programa que calcula o tempo (em anos) que uma pessoa irá demorar para
# poupar R$ 1.000.000,00 (Um Milhão de Reais). O usuário informa o salário mensal e o total
# de despesas mensais.

salario_mensal = float(input('Qual o salario mensal?    '))
despesas = float(input('Quanto em despesas é gasto pôr mês do salário?  '))
salario_final = salario_mensal - despesas
meta = 1000000.00
salarios_meses = meta / salario_final
tempo_anos = salarios_meses / 12
print('Levará',round(tempo_anos),'anos para atingir R$ 1.000.000,00')