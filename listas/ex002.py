"""

Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa

"""

vetor = [5, 7, 9, 3, 2, 4, 60, 85, 90, 8, 15]
vetor_inverse = []

for i in range(len(vetor) - 1, -1, -1):
  vetor_inverse.append(vetor[i])

print(vetor_inverse)