#Escreva um programa que uma tupla com uma “lista de tops”. (Ex: Campeonato Brasileiro de Futebol,
# ou os países que mais ricos do mundo e etc). Depois mostre:
#1)	A penas os 5 primeiros colocados;
#2)	Os últimos 4 colocados;
#3)	Imprimir eles na tela com todos em ordem alfabética;
#4)	Em que posição estará um dos itens a sua escolha.

top = ('Gremio','Internacional','Juventude','Caxias','Sao Jose','Esportivo','Lajeadense','Aimore','Pelotas','Sao Luiz')
print(top)
print(f'Os 5 primeiros colocados: {top[0:5]}')
print(f'Os 4 últimos colocados : {top[6:]}')
print(sorted(top))
print('A posição de Juventude é:',top.index('Juventude'))
