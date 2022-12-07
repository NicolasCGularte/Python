#Escreva um programa queleia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = dict()

aluno['Nome'] = str(input('Nome do aluno: ')).title().strip()
aluno['Media'] = float(input('Media do aluno: '))

for key, value in aluno.items():
    print(f'{key} é igual à {value}!')

print('Situação do aluno é ', end=' ')
if aluno['Media'] >= 7.0:
    print(f'\033[34mAprovado\033[m')
elif 4.0 <= aluno['Media'] < 7.0:
    print(f'\033[33mRecuperação\033[m')
else:
    print(f'\033[31mREPROVADO\033[m')