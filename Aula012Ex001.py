#Escreva um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela

Turma = dict()
P = 20
r = 'Resposta Inválida!'

Turma['Aluno'] = input('Nome do aluno: ')
auxiliar = input("Digite a media: ")
while not auxiliar.isnumeric():
    auxiliar = input("Erro: Tente novamente. Digite a media: ")
Turma['Media'] = float(auxiliar)


print()
print('#'*P)
print()

for key, value in Turma.items():
    print(f"{key} é igual à {value}")

print()
print('#'*P)
print()

if Turma['Media'] >= 70:
    print('Aluno \033[032mAprovado!\033[m')
elif Turma['Media'] >= 6.9 and Turma['Media'] >= 50:
    print('Aluno em \033[034mRecuperção!\033[m')
elif Turma['Media'] < 50:
    print('Aluno \033[031mREPROVADO!\033[m')





