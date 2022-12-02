matrix = [[], [], []]
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

print('='*10)
print(f"A soma de todos os valores pares {pares}")
print(f"A soma da terceira linha = {terceira_linha}")
print(f"O maior valor da segunda linha = {maior}")