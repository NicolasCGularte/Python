#Escreva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#1)	Quantas vezes apareceu o valor 9;
#2)	Em que posição foi digitado o primeiro valor 3;
#3)	Quais foram os números pares.
#Lembrando que, se o usuário digitar uma valor que não esteja na tupla, precisa retornar erro.

valor = (int(input('Digite um valor: ')), int(input('Digite um valor')), int(input('Digite um valor: ')), int(input('Digite um valor: ')))
print(f'O número 9 apareceu {valor.count(9)} vezes!')
if 3 in valor:
    print(f'O número 3 foi digitado na posição {valor.index(3)}')
else:
    print('O valor 3 não foi digitado!')
print("Os valor pares digitados são: ")
for i in valor:
    if i % 2 == 0:
        print(i)

