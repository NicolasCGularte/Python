#Escreva um programa que leia nome, ano de nascimento e carteira de trabalho e
# cadastre-os (com idade) em um dicionário se por acaso a CTPS
# (Carteira de Trabalho e Previdência Social) for diferente de ZERO,
# o dicionário receverá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# (Considere 35 anos de colaboração para se aposentar)

import datetime

pessoa = dict()

r = "RESPOSTA INVÁLIDA!"

pessoa['Nome'] = str(input('Digite seu nome: ')).title().strip()
ano = input('Ano de Nascimento: ').strip()

while not ano.isnumeric() or len(ano) != 4:
    print(f"\033[34m{r}\033[m\n'Formato do tipo: aaaa")
    ano = input('Ano de Nascimento: ').strip()

ano = int(ano)
pessoa['Idade'] = datetime.datetime.now().year - ano

pessoa['CTPS:'] = input('CTPS [0 = não tem]: ')


