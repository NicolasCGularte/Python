#Escreva um programa que ajude um jogador da MEGA SENA a criar
#palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6
#números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

from random import randint
from time import sleep

lista = list()
jogos = list()

print('Jogo da Mega Sena!')

jogo = int(input('Quantos jogos deseja que sejam sorteados? '))
total = 1
while total <= jogo:
    i = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            i += 1
        if i >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(f'Sorteando {jogo} jogos')
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)