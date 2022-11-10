#Escreva um programa que leia 6 números inteiros do usuário e mostre
#a soma apenas daqueles que forem pares, Se o valor for ímpar, desconsidere-o.

soma = 0
for x in range(0, 6):
    n = int(input('Número: '))
    if n % 2 == 0:
        soma += n
print(soma)
