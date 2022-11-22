#Escreva um programa que vai gerar cinco números aleatórios e colocar dentro em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique
# o menor e o maior valor que estão na tupla.
import random
numero = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
print(numero)
for i in range(0, 5):
    if i == 0:
        maior = menor = numero[0]
    else:
        if numero[i] > maior:
            maior = numero[i]
        if numero[i] < menor:
            menor = numero[i]

print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')


