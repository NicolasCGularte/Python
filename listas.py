#Escreva um programa que leia 5 valores e guarde-os dentro de uma lista. No final,
# mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
#Escreva um programa que o usuário escreverá vários valores  numéricos e
# cadastre-os em uma lista. Caso o número já exista lá dentro,
# ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
# e em ordem crescente.

valores = list()
maiores = list()
menores = list()
while True:
   for i in range(0, 10):
      valores.append(int(input(f"{i + 1}) Digite um valor: ")))
      for i in range(0, len(valores)):
         if valores == valores[i]:
            i += 1
         if i >= 1:
            print("Esse valor já existe na LISTA!")
         else:
            print("Valor adicionado com sucesso!!!")
      print("\n")
      if i == 0:
        maior = valores[i]
        menor = valores[i]
      else:
        if valores[i] > maior:
           maior = valores[i]
        if valores[i] < menor:
           menor = valores[i]
      resposta = str(input("Deseja continuar [S/N]? ")).upper().strip()
      while resposta not in 'SN':
         resposta = str(input("RESPOSTA INVÁLIDA!! Deseja continuar [S/N]? "))
      if resposta == 'N':
         break

   for posicao, valor in enumerate(valores):
      if valor == maior:
         maiores.append(posicao)
      if valor == menor:
         menores.append(posicao)

print(f"Você digitou os valores = {valores}")
print(f"O maior valor digitado foi {maior}, nas posições ", end="")
for i in range(0, len(maiores)):
   print(f"{maiores[i]}", end="...")

print(f"\nO menor valor digitado foi {menor}, nas posições ", end="")
for i in range(0, len(menores)):
   print(f"{menores[i]}", end="...")

