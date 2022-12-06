#Escreva um programa que o usuário digite uma expressão matemática qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

parenteses = list()
expressao = str(input('Digite sua expressão: '))

for simbolo in expressao:
    if simbolo == '(':
        parenteses.append(simbolo)
    elif simbolo == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break
if len(parenteses) == 0:
    print('A expressão está CORRETA!')
else:
    print('A expressão está ERRADA!')
