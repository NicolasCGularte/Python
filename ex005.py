# faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ele.

var1 = input('escreva algo ')
print('o tipo primitivo desse valor é ', type(var1))
print('só tem espaços? ', var1.isspace())
print('é um número? ', var1.isnumeric())
print('é alfabético? ', var1.isalpha())
print('é alfanumérico? ', var1.isalnum())
print('está em maiúsculas? ', var1.isupper())
print('esta é minúsculas? ', var1.islower())
print('está capitalizada? ', var1.istitle())

