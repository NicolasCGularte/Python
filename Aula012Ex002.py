#Escreva um programa onde 4 jogadores joguem um dado e tenham resultados
#aleatórios. Guarde esses resultados em um dicionário. No final,
#coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior
#número no dado.

from random import randint
from time import sleep

players = {'Player 1:':randint(1, 6),
           'Player 2:':randint(1, 6),
           'Player 3:':randint(1, 6),
           'Player 4:':randint(1, 6)}

print(f"\033[34m{'>JOGADAS<':=^30}\033[m")
for key, value in players.items():
    print(f'O {key} tirou o número {value}')
    sleep(0.5)

rank = list()
rank = sorted(players.items())
print(f"\033[35m{'>RANKING<':=^30}\033[m")
for posicao, valor in enumerate(rank):
    print(f'{posicao + 1}° Lugar: {valor[0]} com {valor[1]}')
    sleep(0.5)

