'''Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar'''

numero = int(input('Digite um número inteiro: '))
if numero % 2 == 0:
    print('O número {} é PAR!'.format(numero))
else:
    print('o número {} é IMPAR!'.format(numero))
