print('*'*40)
print(f"{'PAR ou IMPAR':^40}")
print('*'*40)

import random
import time



soma = 0
i = 0
continua = 'S'

while continua =='S':
    while True:
        PC = random.randint(1, 100)
        PI = str(input('[ P ] - PAR\n[ I ] - IMPAR\nQual sua opção:')).upper().strip()
        while PI not in 'PI':
            print('Opção INVÁLIDA! Tente novamente...')
            PI = str(input('[ P ] - PAR\n[ I ] - IMPAR\nQual sua opção:')).upper().strip()
        N = int(input('Digite um número: '))
        for p in range(0, 3):
            print('.', end='')
            time.sleep(1)
        print('Sua escolha foi: {}'.format(N))
        soma = PC + N
        print('A escolha do computador foi {}!'.format(PC))
        print('A soma dos números foi  {}'.format(soma))
        if (PI == 'P' and soma % 2 == 0) or (PI == 'I' and soma % 2 == 1):
            print('Parabéns! Voçê venceu!')
            i += 1
        else:
            print('Que pena, voçê perdeu!')
            break

    print('*' * 40)
    print(f"{'GAME OVER':^40}")
    print('*' * 40)
    print('Voçê tem {} vitórias consecutivas!'.format(i))
    print('*' * 40)

    continua = str(input('Deseja um novo desafio [S/N]?')).upper().strip()
    while continua not in 'SN':
        print()

print('Não consegue né Moisés?')