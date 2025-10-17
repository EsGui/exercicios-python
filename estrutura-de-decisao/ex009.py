"""

Faça um programa que leia três numéros e mostre-os em ordem crescente

"""


n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

print(f"{n1} {n2} {n3}")

if n1 < n2:
    sub = n1
    n1 = n2
    n2 = sub

if n2 < n3:
    sub = n2
    n2 = n3
    n3 = sub

print(f"{n1} {n2} {n3}")



