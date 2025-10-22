"""

Faça um prgrama que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os
números

"""

vetor = []
soma = 0
multiplicacao = 1

for i in range(6):
    n = int(input(f"Digite o {i}º valor: "))
    soma += n
    multiplicacao *= n
    vetor.append(n)

print(f"Soma dos valores = {soma}")
print(f"Multiplicacao dos valores = {multiplicacao}")

for l in vetor:
    print(l, end=" ")


