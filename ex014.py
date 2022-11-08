# faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15%
# de aumento

funcionario = input('informe o nome do funcionário ')
salario = float(input('informe o salário: R$ '))
aumento = salario + (salario/100*15)
print('o salario do funcionário(a) {} com o aumento de 15% é R${:.2f}'.format(funcionario, aumento))



