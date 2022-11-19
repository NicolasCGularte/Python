#Escreva um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#1)	Quantas pessoas tem mais de 18 anos;
#2)	Quantos homens foram cadastrados;
#3)	Quantas mulheres tem menos de 20 anos.
import numbers

maior_idade = total_homens = total_mulheres = mulher_menor_20 = 0
resposta = 'M'
idade = 0
continua = 'N'


print('*'*40)
print(f"{'CADASTRO ÚNICO':^40}")
print('*'*40)


while True:
    idade = int(input('Digite sua idade: '))
    resposta = str(input('Digite seu sexo: [M/F] ')).upper().strip()
    while resposta not in 'MF':
        resposta = str(input('Resposta Invalida! Digite seu sexo: [M/F]')).upper().strip()[0]
    if idade > 18:
        maior_idade += 1
    if resposta == 'M':
        total_homens += 1
    if resposta == 'F':
        total_mulheres += 1
        if mulher_menor_20 < 20:
            mulher_menor_20 += 1
    continua = str(input('Deseja continuar? [S/N]?')).upper().strip()[0]
    print('*' * 40)
    while continua not in 'SN':
        continua = str(input('Resposta Invalida! \nDeseja continuar? [S/N]?')).upper().strip()[0]
    if continua == 'N':
        break

print(f'Há {maior_idade} pessoas maiores de 18 anos! ')
print(f'Há {total_homens} homens cadastrados!')
print(f'Há {mulher_menor_20} mulheres menores de 20 anos!')