numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
numero = int(input('Digite um numero de 0 a 20:'))
while numero not in range(0, 21):
    numero = int(input('Tente novamente! Digite um número de 0 a 20: '))
print(f"Voçê digitou o nnúmero {numeros[numero]}!")
