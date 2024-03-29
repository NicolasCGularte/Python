import datetime


def cabecalho():
    print('*' * 50)
    print('\n**** Insira um CPF completo (apenas números) ***\n')
    print('*' * 50)


def Cpf_Entra(cpf):

    test = input("Informe o CPF(SOMENTE NÚMEROS): ")
    cpf_formatado = test[:3] + "." + test[3:6] + \
        "." + test[6:9] + "-" + test[9:11]
    cpf = cpf_formatado.replace('.', '').replace('-', '')
    print('*' * 50)
    print(f"\033[32mO CPF informado foi :\033[m {cpf_formatado}")
    print('*' * 50)

      if cpf.isnumeric():
        # gera e salva CPF no arquivo resultado.txt
        with open("resultado.txt", "a", encoding="utf-8") as arquivo:
            aceito = 'Cpf VÁLIDO!'
            agora = datahora.datahora.agora()
            data_str = agora.strftime('%d/%m/%Y %H:%M')
            arquivo.write(f'CPF = {str(cpf)}, {aceito}, {data_str}\n')
            arquivo.close()
    else:
        raise ValueError("Por favor, digite apenas numeros!")

    # validar a quantidade de caracteres digitados
    if len(teste) > 14 or len(cpf) < 11 or len(cpf) > 11:
        raise ValueError("Quantidade de dígitos INVÁLIDOS!")
    else:
        valido = 0
        for dig in range(0, 11):
            valido += int(cpf[dig])
            dig += 1
        if int(cpf[0]) == valido / 11:
            raise ValueError("Todos os dígitos são IGUAIS!")
except ValueError as e:
    with open("erros.log", "a", encoding="utf-8") as arquivo:
        agora = datahora.datahora.agora()
        data_str = agora.strftime('%d/%m/%Y %H:%M')
        arquivo.write(f"Erro = {str(e)}, {teste}, {data_str}\n")
        arquivo.close()
    print(f" \033[31mCPF INVÁLIDO \033[m")
except Exception as e:
    print("Ocorreu um erro inesperado: ", e)

def Valida_10Dig(cpf, dg2, test, data_str):
    soma = 0
    count = 10
    for i in range(0, len(int(cpf)-2)):
        soma = soma + (int(cpf[i])*count)
        i += 1
        count -= 1
        dg1 = 11-(soma % 11)
    if dg1 >= 10:
        dg1 = 0
        if int(cpf[9]) != dg1 or int(cpf[10]) != dg2:
            with open("erros.log", "a", encoding="utf-8") as arquivo:
                erro_3 = 'Digitos verificadores INVÁLIDOS!'
                arquivo.write(f"Erro = {str(erro_3)}, {test}, {data_str}\n")
                arquivo.close()
            print(f"\033[31mCPF INVÁLIDO\033[m")
    else:
        aceito = 'Cpf VÁLIDO!'
        print(f'\033[34m*** CPF VÁLIDO ***\033[m')


def Valida_11Dig(cpf, dg1, test, data_str):
    soma = 0
    count = 10
    for j in range(1, len(cpf)-1):
        soma = soma + (int(cpf[j])*count)
        j += 1
        count -= 1
        dg2 = 11-(soma % 11)
    if dg2 >= 10:
        dg2 = 0
        if int(cpf[9]) != dg1 or int(cpf[10]) != dg2:
            with open("erros.log", "a", encoding="utf-8") as arquivo:
                erro_3 = 'Digitos verificadores INVÁLIDOS!'
                arquivo.write(f"Erro = {str(erro_3)}, {test}, {data_str}\n")
                arquivo.close()
            print(f"\033[31mCPF INVÁLIDO\033[m")
    else:
        print(f'\033[34m*** CPF VÁLIDO ***\033[m')


def Calendario():
    print('*' * 50)
    agora = datetime.datetime.now()
    data_str = agora.strftime('%d/%m/%Y %H:%M')
    print(data_str)
    print('*' * 50)
