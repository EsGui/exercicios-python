"""

Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa

"""

vetor = []

for c in range(1, 11):
    numeros = int(input(f"Digite o {c}° valor: "))
    vetor.append(numeros)

vetor_inverso = []

for i in range(len(vetor) - 1, -1, -1):
  vetor_inverso.append(vetor[i])

print(vetor_inverso)