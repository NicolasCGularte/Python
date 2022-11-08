# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares
# ela pode comprar

dinheiro = float(input('informe quanto dinheiro vc tem? R$'))
dolares = dinheiro/3.27
print('você pode comprar {:.2f} dólares'.format(dolares))


