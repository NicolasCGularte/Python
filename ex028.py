'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
nome separadamente

ex: Ana Maria de Souza
primeiro = Ana
último = Souza'''

nome = str(input('Digite seu nome inteiro: ')).strip()
inteiro = nome.split()
print('Seu primeiro nome é {} '.format(inteiro[0]))
print('Seu último nome é {}'.format(inteiro[len(inteiro)-1]))
