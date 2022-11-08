'''Faça um programa que leia uma frase pelo teclado e mostre
- quantas vezes aparece a letra "A"
- em que posição ela aparece a primeira vez
- em que posição ela aparece a última vez'''

frase = str(input('Digite uma frase: ')).upper().strip()
print('Analisando a frase....')
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posição {}'.format(frase.find('A')))
print('A letra A apareceu pela última vez na posição {}'.format(frase.rfind('A')))


