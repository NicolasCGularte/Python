from random import randint
from time import sleep
from operator import itemgetter

players = {'Player 1:':randint(1, 6),
           'Player 2:':randint(1, 6),
           'Player 3:':randint(1, 6),
           'Player 4:':randint(1, 6)}

print(f"\033[34m{'>JOGADAS<':=^30}\033[m")
for key, value in players.items():
    print(f'O {key} tirou o número {value}')
    sleep(0.5)

rank = list()
rank = sorted(players.items(), key=itemgetter(1), reverse=True)
print(f"\033[35m{'>RANKING<':=^30}\033[m")
for posicao, value in enumerate(rank):
    print(f'{posicao + 1}° Lugar: {value[0]} com {value[1]}')
    sleep(0.5)