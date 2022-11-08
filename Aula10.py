#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random
aluno1 = input('informe o nome do primeiro aluno: ')
aluno2 = input('informe o nome do segundo aluno: ')
aluno3 = input('informe o nome do terceiro aluno: ')
aluno4 = input('informe o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print(f'A ordem dos alunos sorteados é {lista}')
#print(lista)