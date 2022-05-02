# Faça um programa que solicite ao usuário o valor do litro de combustível (ex. 4,75) e
# quanto em dinheiro ele deseja abastecer (ex. 50,00). Calcule quantos litros de combustível
# o usuário obterá com esses valores.

litros = float(input('Quanto é o litro do combustível?   '))
valor_gasto = float(input('Quando em R$ o senhor(a) deseja abastecer?   '))
litros_obtidos = valor_gasto/litros
print('R$',valor_gasto,'para',litros,'litros dão',round(litros_obtidos),'litros')