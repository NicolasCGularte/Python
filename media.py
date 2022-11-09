import math

N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota: "))
M = (N1+N2)/2
print(M)
print("aprovado"if M > 7 else "reprovado")
