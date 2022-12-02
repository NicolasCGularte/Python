'''#1] Escreva um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#1)	Quantas pessoas foram cadastradas;
#2)	Uma listagem com as pessoas mais pesadas;
#3)	Uma listagem com as pessoas mais leve.

nomes = list()
i = list()


while True:
    print('=' * 20)
    print(f"{f'CADSTRO {len(nomes) + 1}':^20}")
    print('=' * 20)
    i.append(str(input('Nome: ')))
    i.append(int(input('Peso: ')))

    if len(nomes) == 0:
        maior_p = menor_p = i[1]

    else:
        if i[1] > maior_p:
            maior_p = i[1]

        if i[1] < menor_p:
            menor_p = i[1]

    nomes.append(i[:])
    i.clear()

    r = str(input('Deseja Continuar [S/N]? ')).upper().strip()
    while r not in 'SN':
        print('=' * 20)
        r = str(input('Resposta inválida!\n Deseja Continuar [S/N]?')).upper().strip()
    if r == 'N':
        break

print('O MAIOR peso digitado foi {}Kg. Peso de', end='').format(maior_p)
for nome in nomes:
    if nome[1] == maior_p:
        print(f"[{nome[0]}]", end=' ')

print('O MENOR peso digitado foi {}Kg. Peso de', end='').format(menor_p)
for nome in nomes:
    if nome[1] == menor_p:
        print(f"[{nome[0]}]", end=' ')'''

'''lista = list()
n = list()
pares = list()
impares = list()

while True:
    i = int(input('Digite u  número: '))
    n.append(i)
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

    r = str(input('Deseja Continuar [S/N]?')).upper().strip()
    while r not in 'SN':
        r = str(input('Resposta Inválida!\n Deseja Continuar [S/N]? ')).upper().strip()
    if r == 'N':
        break

lista.append(n[:])
lista.append(pares[:])
lista.append(impares[:])
pares.sort(reverse=True)
impares.sort(reverse=True)
print(f"Lista = {lista}")
print(f"Numeros = {n}")
print(f"Pares = {pares}")
print(f"Impares = {impares}")
'''


'''matrix = [[], [], []]
pares = terceira_linha = 0 #ex004
    


for i in range(0, 3):
    for j in range(0, 3):
        matrix[i].append(int(input(f"Matrix[{i}][{j}] =")))

print('='*10)
print(f"{f'MATRIX':^10}")
print('='*10)
for i in range(0, 3):
    for j in range(0, 3):
        print(f" {matrix[i][j]}", end=' ')
        if matrix[i][j] % 2 == 0: #ex004
            pares += matrix[i][j] #ex004
        if i == 2:                #ex004
            terceira_linha += matrix[i][j] #ex004
        if i == 1:  #ex004
            if j == 0: #ex004
                maior = matrix[i][j] #ex004
            else: #ex004
                if matrix[i][j] > maior:  #ex004
                    maior = matrix[i][j] #ex004
                                
    print('')
    
print('=*10)
print(f"A soma de todos os valores pares {pares}")
print(f"A soma da terceira linha = {terceira_linha}")
print(f"O maior valor da segunda linha = {maior}")'''


