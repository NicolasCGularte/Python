#Escreva um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo e realize a contagem. Seu programa tem que realizar três contagens através da função:
#1)	De 1 até 10, de 1 em 1;
#2)	De 10 até 0, de 2 em 2;
#3)	Uma contagem personalizada.

import time

def linha():
    print('%' * 30)

def crescente():
    linha()
    print('Vamos contar ate 10? ')
    for i in range(0, 11):
        print(i, end=' ')
        time.sleep(0.5)
    print('\nThe End!')

def decrescente():
    linha()
    print('Vamos contar de 10 até 0, pulando duas casas? ')
    for i in range(10, -1, -2):
        print(i, end=' ')
        time.sleep(0.5)
    print('\nThe End!')

def personalizada():
    linha()

    numeros = dict()
    numeros['Inicio'] = int(input('Início: '))
    numeros['Fim'] = int(input('Fim: '))
    numeros['Passo'] = int(input('Passo: '))
    print(f"Contando de {numeros['Inicio']} até {numeros['Fim']} de {numeros['Passo']} em {numeros['Passo']}!!!")
    for i in range(numeros['Inicio'], numeros['Fim'], numeros['Passo']):
        print(i, end=' ')
    print('\nThe End!')
    linha()
    while (numeros['Inicio'] < numeros['Fim'] and numeros['Passo'] < 0) or (numeros['Inicio'] > numeros['Fim'] and numeros['Passo'] > 0) or (numeros['Passo'] == 0) or (numeros['Fim'] == numeros['Inicio']):
        print('Não como realizar esta contagem!!')
        linha()
        numeros['Inicio'] = int(input('Início: '))
        numeros['Fim'] = int(input('Fim: '))
        numeros['Passo'] = int(input('Passo: '))
        linha()

time.sleep(0.1)
crescente()
decrescente()
personalizada()