print('*'*40)
print(f"{'TABUADA':^40}")
print('*'*40)

while True:
    n = int(input('Tabuada de qual número voçê deseja? '))
    if n == 0:
        break
    else:
        print('*' * 40)
        print(f"{f'A TABUADA do {n}':^40}")
        print('*' * 40)
        for i in range(1, 11):
            print(f'{i} x {n} = {i*n}'.center(40))
print('*'*40)
print(f"{'Obrigado por participar!':^40}")
print('*'*40)



