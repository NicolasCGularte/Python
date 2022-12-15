import time


def introducao():
    time.sleep(1.2)
    print('Nico Entertainment°')
    time.sleep(1.2)
    print('NoobMaster Productions...')
    time.sleep(1.2)
    print('*' * 50)
    print(f'{"Matadores de Dragão":^50}')
    print('*' * 50)
    time.sleep(1.2)
    print('\n')
    print('Press Strat')
    for i in range(0, 3):
        print('.', end='')
        time.sleep(1)
    print('\n')
    print('Bem vindo Nobre Cavaleiro! Vamos juntos nessa aventura de coragem e bravura?')



def escolha():
    nome = str(input('Não da pra te chamar de cavaleiro toda hora, então, qual é seu nome? ').upper().strip())
    nivel = int(input('Escolha o nível:\n'
                      '[1] Easy\n'
                      '[2] Mediun\n'
                      '[3] Hard\n'
                      '[4] Expert\n'))
    print('\n')
    if nivel == 1:
        vidadragao = 500
        vidacavaleiro = 500
        atakcavaleiro = 500
        atakdragao = 200
        danonodragao = vidadragao - atakcavaleiro
        danonocavaleiro = vidacavaleiro - atakdragao
        






#introducao()
