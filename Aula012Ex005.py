#Escreva um programa que leia nome, sexo e idade de várias pessoas, guardando os dados
# de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#1)	Quantas pessoas foram cadastradas;
#2)	A média de idade do grupo;
#3)	Uma lista com todas as mulheres;
#4)	Uma lista coom todas as pessoas com idade acima da média.


idade_acima = 0
pessoa = dict()
grupo = list()

e = 'Erro! Somente M ou F...'
t = 'Erro! Somente S ou N...'
age = 'Erro! Somente números...'
erro = f"\033[31m{e}\033[m"
erro2 = f"\033[31m{t}\033[m"
erro3 = f"\033[31m{age}\033[m"

while True:
    pessoa['Nome'] = str(input('Informe seu nome: ')).title().strip()
    pessoa['Sexo'] = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]

    while pessoa['Sexo'] not in 'MF':
        pessoa['Sexo'] = str(input(f"{erro}\nInforme seu sexo [M/F]: ")).strip().upper()[0]

    aux = input('Informe sua idade: ').strip()
    while not aux.isnumeric():
        aux = input(f"{erro3}\nInforme sua idade: ")
    aux = int(aux)
    idade_acima += aux
    pessoa['Idade'] = aux
    grupo.append(pessoa.copy())

    r = str(input('Deseja Continuar [S/N]? ')).upper().strip()[0]
    while r not in 'SN':
        r = str(input(f"{erro2}\nDeseja continuar [S/N]? ")).upper().strip()[0]
    if r == 'N':
        break
media = idade_acima/len(grupo)
print()
print(f" => o grupo tem {len(grupo)} pessoas.")
print(f" => A media de idade é {media:.2f}.")

print(' => As mulheres cadastradas fora: ', end=' ')
for i in range(0, len(grupo)):
    if grupo[1]['Sexo'] == 'F':
        print(f"{grupo[1]['Nome']}", end=' ')

print()
print(' => As pessoas cadastradas acima da idade media:')
for i in range(0, len(grupo)):
    if grupo[1]['Idade'] > media:
        print(f" => Nome = {grupo[1]['Nome']};\nSexo = {grupo[1]['Sexo']};\nIdade = {grupo[1]['Idade']}")

print(f"\033[31m{f'FIM DO PROGRAMA!':°^30}")
