"""

Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
imprima as consoantes.

"""

ctr = str(input("Digite no maximo 10 carectes: "))

qtd_consoante = 0
consoantes = []

if len(ctr) <= 10:
    for l in ctr:
        if l in "aeiou":
            qtd_consoante += 1
            consoantes.append(l)
    print(f"Quantidade de consoantes = {qtd_consoante} / Consoantes = {[x for x in consoantes]}")
else:
    print("Por favor, digite apenas 10 caracteres :)")




