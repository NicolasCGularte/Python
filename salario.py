salario = float(input('Informe o salário do funcionário: R$ '))
if salario <= 1250:
   novo = salario + (salario / 100*15)
else:
    novo = salario + (salario / 100*10)
print('O salário do funcionário aumentou de R${:.2f} para R${:.2f}'.format(salario, novo))


