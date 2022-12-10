#Escreva um programa que tenha uma função área(), que receba as dimensões de
# um terreno retangular (largura e comprimento) e mostre a área do ‘terreno.

def titulo():
    print('*' * 30)
    print(f"{'Controle de Terreno':^30}")
    print('*' * 30)

def area(largura, comprimento):
    A = largura*comprimento
    print(f"A área do terreno será de A = {A:.2f} m².")

titulo()
l = float(input('Informe a largura do terreno: '))
c = float(input('Informe o comprimento do terreno: '))
area(l, c)




