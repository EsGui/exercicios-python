"""

Faça um programa que leia 20 números inteiros e armazene-os num vetor. Armazene os
números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores

"""

vetor = []
vetor_par = []
vetor_impar = []

for n in range(1, 21):
    numero = int(input(f"Digite o {n}° valor: "))
    vetor.append(numero)
    if numero % 2 == 0:
        vetor_par.append(numero)
    else:
        vetor_impar.append(numero)

print(f"Vetor = {vetor}\n Vetor Par = {vetor_par}\n Vetor Impar = {vetor_impar}")
