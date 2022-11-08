#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
#lendo o nome deles e escrevendo o nome escolhido.

from random import choice
aluno1 = input('informe o nome do primeiro aluno: ')
aluno2 = input('informe o nome do segundo aluno: ')
aluno3 = input('informe o nome do terceiro aluno: ')
aluno4 = input('informe o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
aluno = choice(lista)
print('O aluno sorteado que vai apagar o quadro é {}'.format(aluno))


