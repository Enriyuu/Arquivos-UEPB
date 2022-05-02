# Faça um programa que calcule a área total (m2) de uma casa com 4 cômodos. O usuário
# deve inserir a largura e comprimento de cada um dos cômodos, calcular a área individual de
# cada um e por fim exibir a área total da casa.

largura1 = float(input('Informe a largura do primeiro cômodo em m2    '))
comprimento1 = float(input('Informe a comprimento do primeiro cômodo em m2   '))
largura2 = float(input('Informe a largura do primeiro cômodo em m2   '))
comprimento2 = float(input('Informe a comprimento do primeiro cômodo em m2   '))
largura3 = float(input('Informe a largura do primeiro cômodo em m2   '))
comprimento3 = float(input('Informe a comprimento do primeiro cômodo em m2   '))
largura4 = float(input('Informe a largura do primeiro cômodo em m2   '))
comprimento4 = float(input('Informe a comprimento do primeiro cômodo em m2   '))

area1 = largura1 * comprimento1
area2 = largura2 * comprimento2
area3 = largura3 * comprimento3
area4 = largura4 * comprimento4

area_total = area1 + area2 + area3 + area4

print('A área total da casa é',area_total,'m2')