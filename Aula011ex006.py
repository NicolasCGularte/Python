#Escreva um programa que leia nome e duas notas de
#vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim
#contendo a média de cada um e permita que o usuário possa mostrar as notas de cada
#aluno individualmente

cond = n = 0
temp = list()
alunos = list()

print('Cadastro de aluno')

while True:
    print('-'*30)

    print(f'Id do aluno: {n}')
    temp.append(str(input('Digite o primeiro nome do aluno: ')))
    temp.append(float(input('Digite a primeira nota: ')))
    temp.append(float(input('Digite a segunda nota: ')))

    alunos.append(temp[:])
    temp.clear()
    n += 1

    print('-'*30)
    obs = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    if obs in 'Nn':
        break


while True:

    print('-'*30)
    cond = str(input('Digite 1 para visualizar a lista de todos os alunos\nDigite 2 para encontra apenas um aluno '
                     'especifico\nDigite 3 para sair\n'))
    if cond in '1':
        print('Lista de aluno')
        print('-' * 30)
        for a in alunos:
            print(f'Nome: {a[0]:^5} \nPrimeira Nota: {a[1]:^5} \nSegunda Nota: {a[2]:^5} \nMédia: {(a[1] + a[2] % 2):^5}')
            print('-' * 30)

    elif cond in '2':
        print('-' * 30)
        nome = int(input('Digite o Id do aluno: '))
        print(f'Aluno Id:{nome} {alunos[nome]}')

    elif cond in '3':
        break



