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
        return True
    return False

def recupera_primeiro_digito(cpf):
    numDV1 = 0
    numCheckDV1 = int(cpf[9:10])
    for i in range(1, 10):
        numDV1 = numDV1 + int(cpf[i-1:i]) * i
    numDV1 = numDV1 % 11
    if (numDV1 == 10):
        numDV1 = 0
    if numDV1 != numCheckDV1:
        return False
    return True

def recupera_segundo_digito(cpf, numDV1):
    numDV2 = 0
    numCheckDV2 = int(cpf[10:11])
    for i in range(2, 11):
        numDV2 = numDV2 + int(cpf[i-1:i]) * (i-1)
        numDV2 = numDV2 % 11
    if (numDV2 == 10):
        numDV2 = 0
    if numDV2 != numCheckDV2:
        return False
    return True

if __name__ == '__main__':
    try:
        print('Informe o CPF')
        cpf = str(input())
        if cpf_valido(cpf):
            print('CPF é válido.')
            with open("valid_cpf.txt", "a") as valid_file:
                valid_file.write(cpf + "\n")
        else:
            print('CPF inválido')
            with open("invalid_cpf.txt", "a") as invalid_file:
                invalid_file.write(cpf + "\n")

        agora = datetime.datetime.now()
        data_str = agora.strftime('%d/%m/%Y %H:%M')
        print(data_str)
    except Exception as e:
        with open("errors.txt", "a") as error_file:
            error_file.write("Error: " + str(e) + \n)
