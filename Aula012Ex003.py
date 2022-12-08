import datetime

pessoa = dict()

f = "Fim do Programa!!"
r = "RESPOSTA INVÁLIDA!"
t = 30

pessoa['Nome'] = str(input('Digite seu nome: ')).title().strip()
ano = input('Ano de Nascimento: ').strip()
print()
print('$'*t)
print()
while not ano.isnumeric() or len(ano) != 4:
    print("\033[31m{}\033[m\nFormato do tipo: aaaa".format(r))
    ano = input('Ano de Nascimento: ').strip()
ano = int(ano)
pessoa['Idade'] = datetime.datetime.now().year - ano
pessoa['CTPS'] = input('CTPS [0 = não tem]: ').strip()
while not pessoa['CTPS'].isnumeric() or len(pessoa['CTPS']) != 8:
    print("\033[31m{}\033[m\nCTPS deve conter 8 digitos!".format(r))
    pessoa['CTPS'] = input('CTPS [0 = não tem]: ').strip()
pessoa['CTPS'] = int(pessoa['CTPS'])
print()
print('$'*t)
if pessoa['CTPS'] == 0:
    for key, value in pessoa.items():
        print(f"{key:<{len(r) * 2}}{value:<{len(r) - 16}}")
    print("\033[31m>{}<\033[m".format(r))
else:
      pessoa['Ano de Contratação'] = input('Ano de Contratação: ').strip()
      print()
      print('$' * t)
while not pessoa['Ano de Contratação'].isnumeric() or len(pessoa['Ano de Contratação']) != 4 or int(pessoa['Ano de Contratação']) - ano <= 16:
    if not pessoa['Ano de Contratação'].isnumeric():
        print("\033[35m>{}[35m, este valor não é um número! Tente Novamente...<".center(t).format(r))
    elif len(pessoa['Ano de Contratação']) != 4:
        print("\033[31m>{}[35m Formato Inválido: aaaa <".center(t).format(r))
    elif int(pessoa['Ano de Contratação']) - ano <= 16:
        print("\033[31m{}[31m É preciso ter maior idade por Lei!".format(r))

    pessoa['Ano de Contratação'] = input('Ano de Contratação: ')
pessoa['Ano de Contratação'] = int(pessoa['Ano de Contratação'])
pessoa['Aposentadoria'] = pessoa['Ano de Contratação'] + 35
'''pessoa['Ano Vigente de Contibuição'] = datetime.datetime.now().year
pessoa['Ano Vigente de Contibuição'] = pessoa['Ano Vigente de Contibuição'] - pessoa['Ano de Contratação']
pessoa['Tempo para Aposentadoria'] = pessoa['Aposentadoria'] - pessoa['Ano de Contratação']'''

print()
print('$'*t)
pessoa['Salário'] = float(input('Salário: R$'))
print()
print('$'*t)
for key, value in pessoa.items():
    print(f"{key:<{len(r) * 2}}{value:<{len(r) - 16}}")
print(f"\033[31m{'>FIM DO PROGRAMA!<':=^30}\033[m")