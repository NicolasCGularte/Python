#Escreva um programa que vai ler vários valores numéricos e colocá-los em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e ímpares
#digitados, respectivamente. No final, mostre as 3 listas. Caso a lista esteja vazia, informe isso ao usuário.

valores = list()
pares = list()
impares = list()


while True:
    auxiliar = int(input('Digite um valor: '))
    valores.append(auxiliar)
    if auxiliar % 2 == 0:
        pares.append(auxiliar)
    elif auxiliar % 2 != 0:
        impares.append(auxiliar)

    r = str(input('Deseja continuar [S/N]?')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Resposta inválida!!!\nDeseja continuar [S/N]?')).upper().strip()[0]
    if r == 'N':
        break
    valores.sort()
print(f'Você informou os seguintes valores para formar a lista: {valores}')
if len(pares) == 0:
    print(f'Não há valores PARES informados na lista')
else:
    print(f'Forma informados os seguintes valores PARES na lista: {pares}')
if len(impares) == 0:
    print(f'Não foram informados nenhum valor IMPAR na lista!!')
else:
    print(f'Foram informados os seguintes valores IMPARES na lista: {impares}')
if len(valores) == 0:
    print(f'A lista está vazia!')
