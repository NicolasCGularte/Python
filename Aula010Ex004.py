#Escreva um programa que vai ler vários valores numéricos e colocar eles em uma lista. No final, mostre:
#1)	Quantos números foram digitados;
#2)	A lista de valores digitados, ordenada de forma crescente;
#3)	Se o valor 5 foi digitado e está ou não na lista.


numeros = list()

while True:
    numeros.append(int(input('Digite um número: ')))

    r = str(input('Deseja continuar [S/N]?')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Resposta inválida! Deseja continuar [S/N]?')).upper().strip()[0]
    if r == 'N':
        break
numeros.sort()
print(f'Foram digitados {len(numeros)} números')
print(f'A lista de números em ordem crescente é {numeros}')
if 5  in numeros:
    print('O número 5 consta na lista de números digitados!')
else:
    print('O número 5 NÃO faz parte da lista de números digitados!')


