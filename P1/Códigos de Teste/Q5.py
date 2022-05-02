# Faça um programa que calcule a conversão monetária de Real para Dólar. O usuário
# informa o valor da cotação do dólar (ex.: 3,78) e quanto em real deseja converter (ex.
# 150,00). O programa exibe quantos dólares valem os reais informados.

cotação_atual = float(input('Qual a cotação atual do dólar? '))
conversão = float(input('Quando em reais deseja converter?  '))
resultado_final = cotação_atual * conversão
print('A conversão fica de ',resultado_final)