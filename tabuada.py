#Escreva um programa que leia um número do usuário e retorne a tábuada desse número

f = 15
n = int(input('Digite um numero: '))
print('='*f)
print(f"{f'TABUADA DO {n}':^{f}}")
print('='*f)

for i in range(1, 11):
    print(f'{i} x {n} = {i*n} ')
print('='*f)