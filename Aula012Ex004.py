#Escreva um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai
#ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado
#em dicionário, incluindo o total de gols feitos durante o campeonato.


t = 'Erro! Digite somento números...'

jogador = dict()
gols = list()
soma = 0

jogador['Nome'] = str(input('Informe o nome do jogador: ')).strip().title()
jogos = input(f"Quantos partidas {jogador['Nome']} jogou? ")

while not jogos.isnumeric():
    print(f"\033[31m{t}\033[m")
    jogos =input(f"Quantos partidas {jogador['Nome']} jogou? ").strip()
jogos = int(jogos)

for i in range(0, jogos):
    auxiliar = input(f" Quantos gos no {i + 1}° jogo? ").strip()

    while not auxiliar.isnumeric():
        print(f"\033[31m{t}\033[m")
        auxiliar = input(f" Quantos gos no {i + 1}° jogo? ").strip()
    auxiliar = int(auxiliar)
    soma += auxiliar
    gols.append(auxiliar)

jogador['Gols'] = gols[:]
jogador['Total de gols'] = soma

print(f"O jogador {jogador['Nome']} jogou {jogos} partidas. ")
for posicao in range(0, jogos):
    print(f" Na partdia {posicao + 1}, fez {jogador['Gols'][posicao]} gols.")
print(f"Total de {jogador['Total de gols']} gols.")
