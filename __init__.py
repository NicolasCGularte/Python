def titulo(txt):

    """
    Função cahamda para inserir um título ou cabeçalho de início do programa!
    """
    t = len(txt) + 6
    print('#' * t)
    print(f"{txt:^{t}}")
    print('#' * t)


def aumentar(preco):

    """Função chamada para realizar o calculo de
       aumento do valor inserido pelo usuário em 10%.
    """

    aumento =  (preco * 10) / 100
    print(f"==> Aumentado 10%, temos R${aumento:.2f}!")


def diminuir(preco):
    diminui = preco * 0.13
    print(f"==> Com desconto de 13%, temos R${diminui:.2f}!")


def dobro(preco):
    mult = preco * 2
    print(f"==> O dobro de R${preco:.2f} vale R${mult:.2f}!")


def metade(preco):
    div = preco / 2
    print(f"==> A metade de R${preco:.2f} vale R${div:.2f}!")


def rodape(txt):
    t = len(txt) + 6
    print('#' * t)
    print(f"{txt:^{t}}")
    print('#' * t)


