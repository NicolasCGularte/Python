n = i = s = 0

while True:
    n = int(input('Digite um numero[999 to exit]: '))
    if n == 999:
        break
    else:
        s += n
        i +=1
print(f'Soma = {s}')
print(f'Contador = {i}')
