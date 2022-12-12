from time import sleep
from random import randint


def sorteio(lista):
    print('Inciando o sorteio:\n ', end=' ')
    for i in range(0, 10):
        sleep(0.5)
        valor = randint(1, 100)
        if valor % 2 == 0:
            print(f"\033[34m{valor}\033[m", end=' ')
        else:
            print(f"\033[31m{valor}\033[m", end=' ')
        lista.append(valor)
    sleep(0.5)
    print()
    sleep(0.5)
    print("Sorteados!")


def somaPares(lista):
    somap = 0
    sleep(0.5)
    for elemento in lista:
        if elemento % 2 == 0:
            somap += elemento
    print(f"A soma dos valores pares de:\n{lista} é\033[34m\n{somap}\033[m.")


def somaImpares(lista):
    somai = 0
    sleep(0.5)
    for elemento in lista:
        if elemento % 2 != 0:
            somai += elemento
    print(f"A soma dos valores Impares de:\n{lista} é\033[34m\n{somai}\033[m.")





numeros = list()
sorteio(numeros)
somaPares(numeros)
somaImpares(numeros)
