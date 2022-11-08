# escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

valor = float(input('digite um valor em metros'))
centimetros = valor*100
milimetros = valor*1000
print('o valor tem {:.1f} centímetros e {:.1f} milímetros '.format(centimetros, milimetros))
