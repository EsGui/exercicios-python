"""

Faça um programa que leia 4 notas, mostre as notas e a média na tela

"""

vetor = []
soma = 0
media = 0

for i in range(1, 5):
    nota = float(input(f"Digite a {i}° nota: "))
    vetor.append(nota)

for soma_notas in vetor:
     soma += soma_notas

print("\nNotas\n ")
for notas in vetor:
    print(notas)

media = soma / len(vetor)

print("\nMédia\n ")
print(f"{media:.2f}")




