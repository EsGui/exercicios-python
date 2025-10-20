"""

Faça um programa que leia um vetor de 5 números inteiros e mostre-os

"""

vetor = []

for c in range(1, 6):
    numeros = int(input(f"Digite o {c}° valor: "))
    vetor.append(numeros)

print(vetor)