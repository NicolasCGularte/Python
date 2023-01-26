import datetime

def cpf_valido(cpf):
    cpf = cpf.replace('.', '').replace('-', '')
    if len(cpf) != 11 or not cpf.isnumeric() or todos_numeros_iguais(cpf):
        return False
    numDV1 = recupera_primeiro_digito(cpf)
    numDV2 = recupera_segundo_digito(cpf, numDV1)
    if numDV1 == int(cpf[9]) and numDV2 == int(cpf[10]):
        return True
    else:
        return False

def todos_numeros_iguais(cpf):
    numIG = 0
    for i in range(0, 11):
        numIG += int(cpf[i])
        i += 1
    if int(cpf[0]) == numIG / 11:
        print('CPF inválido!')

def recupera_primeiro_digito(cpf):
    numDV1 = 0
    numCheckDV1 = int(cpf[9:10])
    for i in range(1, 10):
        numDV1 = numDV1 + int(cpf[i-1:i]) * i
    numDV1 = numDV1 % 11
    if (numDV1 == 10):
        numDV1 = 0
    if numDV1 != numCheckDV1:
        print('Digito 1 inválido!')
    return numDV1

def recupera_segundo_digito(cpf, numDV1):
    numDV2 = 0
    numCheckDV2 = int(cpf[10:11])
    for i in range(2, 11):
        numDV2 = numDV2 + int(cpf[i-1:i]) * (i-1)
        numDV2 = numDV2 % 11
    if (numDV2 == 10):
        numDV2 = 0
    if numDV2 != numCheckDV2:
        print('Digito 2 inválido!')
    return numDV2

if __name__ == '__main__':
    print('Informe o CPF')
    cpf = str(input())
    if cpf_valido(cpf):
        print('CPF é válido.')
    else:
        print('CPF inválido')
    agora = datetime.datetime.now()
    data_str = agora.strftime('%d/%m/%Y %H:%M')
    print(data_str)
