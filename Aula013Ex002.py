#Escreva um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
# e mostre uma mensagem com tamanho adaptável aos tamanho do texto. Faça isso quantas vezes o usuário quiser.

def escreva(txt):
    t = len(txt) + 4
    print('#' * 30)
    print(f"{txt:^{t}}")
    print('#' * 30)

def invalida():
    txt = 'Erroooouuu!!!'
    t = len(txt) + 6
    print(f"\033[31m{txt:^{t}}\033[m")

while True:
    msg = str(input('Por favor, digite sua mensagem: ')).strip()
    escreva(msg)

    r = str(input('Deseja continuar [S/N]? ')).upper().strip()
    while r not in 'SN':
        invalida()
        r = str(input('Deseja continuar [S/N]? ')).upper().strip()
    if r == 'N':
        break

print("> Terminou! <")

