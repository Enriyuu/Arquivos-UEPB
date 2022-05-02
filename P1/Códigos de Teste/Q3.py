# Faça um programa que calcule o valor a ser pago por uma dívida em atraso. O usuário
# deve informar o valor original da dívida (ex. R$ 50,00), a quantidade de dias em atraso (ex.
# 35 dias) e o valor da multa por dia de atraso (ex. R$ 0,25).

valor_original = float(input('Qual o valor original da dívida?  '))
dias_atrasados = float(input('Quantos dias em atraso tem a dívida?  '))
multa = float(input('Qual o valor da multa por dia? '))

multa *= dias_atrasados
pagamento_final = valor_original + multa

print('O valor a ser pago é',pagamento_final,('reais'))