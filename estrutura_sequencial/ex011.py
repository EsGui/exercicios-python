"""

Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

    - O produto do dobro do primeiro com a metade do segundo.
    - A soma do triplo do primeiro com o terceiro
    - O terceiro elevado ao cubo

"""

n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
f3 = float(input("Digite o terceiro número inteiro: "))

calc1 = (n1 * 2) * (n2 / 2)
calc2 = (n1 * 3) + f3
calc3 = f3 ** 3

print(f"O produto do dobro do primeiro com a metade do segundo é {calc1}")
print(f"A soma do triplo do primeiro com o terceiro é {calc2}")
print(f"O terceiro valor elevado ao cubo é {calc3}")


