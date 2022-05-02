# Faça um programa que calcule a média de consumo (em km/l) de combustível de um
# veículo. O usuário deve informar o KM inicial (ex. 12500 km), o KM final (ex. 12700 km) e
# quantos litros foram gastos no percurso.

km_inicial = float(input('Qual o KM inicial?    '))
km_final = float(input('Qual o KM final?    '))
litros_gastos = float(input('Quantos litros foram gastos?   '))

soma = km_inicial + km_final + litros_gastos
media = soma/3
print('A média de consumo são de',round(media),'km/l')