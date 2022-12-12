#Escreva um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores PARES sorteados pela função anterior. Mostre os valores pares e ímpares de
# cores diferentes

from time import sleep
from random import randint

def sorteio(lista):
    print('Inciando o sorteio: ', end=' ')
    for i in range(0, 5):
        sleep(0.5)
        valor = randint(1, 100)
        if valor %2 == 0:
            print(f"{valor}", end=' ')
        else:
            print(f"{valor}", end=' ')
        lista.append(valor)
    sleep(0.5)
    print("Sorteados!")

def somaPares(lista):
    soma = 0
    sleep(0.5)
    for elemento in lista:
        if elemento % 2 == 0:
            soma += elemento
    print(f"A soma dos valores pares da {lista} é {soma}.")

numeros = list()
sorteio(numeros)
somaPares(numeros)

