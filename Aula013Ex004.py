#Escreva um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros
# aleatoriamente. Seu programa tem  que analisar todos os valores e dizer qual deles é o maior.

def linha(comprimento, opcao):
    c = comprimento
    if opcao == 1:
        print('*' * c)
    if opcao == 2:
        print(f"{'<Resultados!>':=^{c}}")


def erro(saida):
    c = 50
    txt = 'Resposta Invalida!'
    t = len(txt) * 4
    txt1 = 'Isso não é um número. Tente outra vez...'
    txt2 = 'Isso não é uma letra. Tente outra vez...'
    txt3 = 'Opção não existe. Tente outra vez...'

    if saida == 1:
        print(f"{'*' * c}\n{txt:^{t}}\n{txt1:^{t}}\n{'*' * c}")
    if saida == 2:
        print(f"{'*' * c}\n{txt:^{t}}\n{txt2:^{t}}\n{'*' * c}")
    if saida == 3:
        print(f"{'*' * c}\n{txt:^{t}}\n{txt3:^{t}}\n{'*' * c}")

def maior(lista):
    linha(50, 2)
    print(f"Você entrou com os valores: {lista}.")
    print(f"No total são {len(lista)} valores.")
    print(f"O maior valor que você entrou foi {max(lista)}")
    linha(50, 1)

valores = list()

while True:
    i = input("Entre com um valor: ")
    while not i.isnumeric():
        erro(1)
        i = input("Entre com um valor: ")

    i = int(i)
    valores.append(i)

    r = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    while r not in 'SN':
        erro(3)
        r = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]

    if r == 'N':
        break

maior(valores)
