''' Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
venceu ou perdeu'''

from random import randint
from time import sleep
print('Pense em um número inteiro entre 0 e 5 ')
numero = int(input('Digite o número que você acha que o computador escolheu: '))
computador = randint(0, 5)
print('PROCESSANDO...')
sleep(2)
print('O computador escolheu o número {}'.format(computador)) # jogador tenta advinhar
if numero == computador:
    print('Parabéns, você venceu!')
else:
    print('Que pena, você perdeu!')

