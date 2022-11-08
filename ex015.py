#Escreva um programa que converta uma temperatura digitando em graus celsius e converta para graus fahrenheit

c = float(input('informe a temperatura em °C: '))
f = 9*c/5+32
print('a temperatura de {}°C corresponde a {}°F'.format(c, f))
