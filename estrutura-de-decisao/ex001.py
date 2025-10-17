"""

Faça um programa que peça dois números e imprima o maior deles

"""

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

if n1 > n2:
    print(f"{n1} maior que {n2}")
elif n1 < n2:
    print(f"{n2} maior que {n1}")
else:
    print(f"{n1} igual á {n2}")