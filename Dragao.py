import linha, play, jogo


import time

def linha():
    t = 50
    print('*' * t)


def play():
    time.sleep(1.2)
    print('Nico Entertainment°')
    time.sleep(1.2)
    print('NoobMaster Productions...')
    time.sleep(1.2)
    print('*'*50)
    print(f'{"Matadores de Dragão":^50}')
    print('*'*50)
    time.sleep(1.2)
    print('\n')
    print('Press Strat')
    for i in range(0,3):
        print('.', end='')
        time.sleep(1)





castelo = """
─────────█▄██▄█──────────────────█▄██▄█─────────
█▄█▄█▄█▄█▐█ ██▌█▄█▄█▄█▄██▄█▄█▄█▄█▐█ ██▌█▄█▄█▄█▄█
███ █████▐████▌████ ███┼┼███ ████▐████▌█████ ███
█████████▐████▌████████┼┼████████▐████▌█████████
"""




dragao = """
░▄▄▄▄░
▀▀▄██►
▀▀███►
░▀███► ░█►
▒▄████▀▀
"""




tanque = """.(҂`_´)
             <,︻╦̵̵̿╤─ ҉     ~  •
            █۞███████]▄▄▄▄▄▄▄▄▄▄▃ ●●●
            ▂▄▅█████████▅▄▃▂…
            [███████████████████]
            ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙
            """






def jogo():
    v_d = int(2000)
    m_a = int(500)
    a_d = int(500)
    m_v = int(2000)
    m_d = int(5000)
    d_d = int(5000)
    dano_d = (v_d - m_a)
    meu_d = (m_v - a_d)
    d_d_dragao = (d_d - m_a)
    d_m_defesa = (m_d - a_d)


    print('\n')
    print('Bem vindo Nobre Cavaleiro! Vamos juntos nessa aventura de coragem e bravura?')
    print('Vamos cavaleiro! Venha lutar ao meu lado contra o dragão para salvar a princesa do alto da Torre!!')
    nome = input('Não da pra te chamar de cavaleiro toda hora, então, qual é seu nome? ').upper().strip()
    print(f'Certo {nome} vamos lutar contra o dragão')
    print(f'-{nome} ataca-')
    time.sleep(1.2)
    print(f"Boa, conseguimos diminuir a defesa dele!!! {d_d_dragao}")
    print('Bom trabalho! Conseguimkos derrubar a defesa da Fera!!!')
    time.sleep(1.2)
    print('-O dragão ataca-')
    print(f'Oh não, ele conseguiu atingir sua defesa, tenha CUIDADO!!! {d_m_defesa}')
    print('-O dragão ataca-')
    time.sleep(1.2)
    print('Precisamos acabar com isso agora, estamos sem defesa!!!')
    time.sleep(1.2)
    print(f'Agora você esta a beira da morte, esta só com {meu_d} de vida, você vai ter que dar o golpe final')
    time.sleep(1.2)
    print(f'Boa, estamos quase vencendo esta batalha contra essa Fera!!! {dano_d}')
    print('Precisamos acabar com isso AGORA!!!')
    print(f'-{nome} ataca-')
    print('-Golpe duplo-')
    print(f'-{nome} com um golpe final arranca a cabeça do dragão! Vencemos!\n Agora aprincesa está à salvo graças a você')




linha()
print(f'\033[42m{"Matadores de Dragão":^50}\033[m')
linha()
print(f"{castelo:^50}")
linha()
play()
jogo()
print(f"{dragao:^50}")

