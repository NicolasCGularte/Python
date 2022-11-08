# faça um programa que leia a largura e a altura  de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la, sabendo de cada litro de tinta, pinta
# uma área de 2m2

largura = float(input('informe quantos metros de largura '))
altura = float(input('informe quantos metros de  altura '))
area = largura*altura
tinta = area/2
print('Sua parede tem a dimensão de {} x {}, e sua área é de {} '
      'então será necessário {} litros de tinta  '.format(largura, altura, area, tinta))

