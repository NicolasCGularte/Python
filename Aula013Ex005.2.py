from time import sleep
from random import randint

def linha():
    print('*' * 50)
    print(f"{'Sorteando números Pares e Impares!!':^30}")
    print('*' * 50)


def sorteio(lista):

    """
       Função chamda para realização
       do sorteio de números aleatórios
       em uma lista.
    """

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

    """
       Função cahmada para realizar a soma
       de todos os números PARES sorteados
       em uma lista.
    """

    somap = 0
    sleep(0.5)
    for valor in lista:
        if valor % 2 == 0:
            somap += valor
    print(f"A soma dos valores pares é:\n\033[34m{somap}\033[m.")


def somaImpares(lista):

    """
        Função cahmada para realizar a soma
        de todos os números IMPARES sorteados
        em uma lista.
    """

    somai = 0
    sleep(0.5)
    for valor in lista:
        if valor % 2 != 0:
            somai += valor
    print(f"A soma dos valores Impares é :\n\033[31m{somai}\033[m.")


def somaTotal(lista):

    """
       Função cahmada para realizar a soma
       de todos os números PARES e IMPARES sorteados
       em uma lista, para obter a SOMA total entre
       eles.
    """

    soma = 0
    for i in lista:
        soma += i
    print(f"A soma de todos os valores é :\n\033[32m{soma}\033[m")


'''numeros = list()
linha()
sorteio(numeros)
linha()
somaPares(numeros)
linha()
somaImpares(numeros)
linha()
somaTotal(numeros)'''
print(help(somaPares))
print(help(somaImpares))
print(help(somaTotal))

