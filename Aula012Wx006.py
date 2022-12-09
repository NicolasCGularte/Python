#Escreva um programa que aprimore o exercício 4 para que funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

from random import randint

t = 'Erro! Digite somento números...'
p = 'Erro! Digite somente S ou N...'
s = 'Erro! Esse valor não é um número. Tente novamente...'

jogador = dict()
gols = list()
soma = 0
q = 30


while True:

    jogador['Nome'] = str(input('Informe o nome do jogador: ')).strip().title()
    jogos = input(f"Quantos partidas {jogador['Nome']} jogou? ")

    while not jogos.isnumeric():
        print(f"\033[31m{t}\033[m")
        jogos =input(f"Quantos partidas {jogador['Nome']} jogou? ").strip()
    jogos = int(jogos)

    for i in range(0, jogos):
        auxiliar = input(f" Quantos gols no {i + 1}° jogo? ").strip()

    r = str(input('Deseja continuar [S/N]? ')).upper().strip()
    while r not in 'SN':
        r = input(f"\033[31m{p}\033[m\nDeseja continuar [S/N]? ").upper().strip()
    if r == 'N':
        break
    r = str(r)

    while not auxiliar.isnumeric():
        print(f"\033[31m{t}\033[m")
        auxiliar = input(f" Quantos gos no {i + 1}° jogo? ").strip()
    auxiliar = int(auxiliar)
    soma += auxiliar
    gols.append(auxiliar)


    jogador['Gols'] = gols[:]
    jogador['Total de gols'] = soma

prit('Cód: ', end=' ')
for key in jogador.keys():
    print(f"{key:<15}", end=' ')
print()
print('*' * q)
for chave, valor in enumerate(time):
    print(f"{cahve:<4}", end=' ')
    for i in valor.values():
        print(f"{str(i):<15}", end=' ')
    print()
while True:
    busca = input('Selecione o jogador pelo código [999 to exit]: ').strip()
    while not busca.isnumeric()


print(f"O jogador {jogador['Nome']} jogou {jogos} partidas. ")
for posicao in range(0, jogos):
    print(f" Na partdia {posicao + 1}, fez {jogador['Gols'][posicao]} gols.")
print(f"Total de {jogador['Total de gols']} gols.")