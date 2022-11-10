
num = int(input('Digite um numero: '))

total = 0

for c in range(1 , num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m',end=' ')
    print(f'{c}', end=' ')

if total == 2:
    print('\nO numero {} é divisivel por {} valores logo é Primo'.format(num,total))
else:
    print('\nO numero {} é divisivel por {} valores logo não é Primo'.format(num,total))