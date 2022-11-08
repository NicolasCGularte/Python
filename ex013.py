# faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input('informe o preço do produto R$'))
preconovo = preco - (preco/100*5)
print('o valor de R${:.2f} agora com desconto de 5% é: R${:.2f}'.format(preco, preconovo))
