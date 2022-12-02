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