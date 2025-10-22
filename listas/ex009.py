"""

Faça um programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos
quadrados dos elementos vetor.

"""

a = []
soma = 0
quadrado = 0

for i in range(1, 11):
    n = int(input(f"Digite o {i}° valor: "))
    quadrado = n ** 2
    a.append(quadrado)

for v in a:
    soma += v

print(f"Soma dos quadrados igual a = {soma}")
