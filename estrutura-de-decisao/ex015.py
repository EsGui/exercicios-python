"""

Faça um programa que peça os 3 lados de um triângulo. O programa
deverá informar se os valores podem ser um triângulo. Indique, caso
os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou 
escaleno

Dicas:

    - Três lados formam um triângulo quando a soma de quaisquer dois lados for 
    maior que o terceiro

    - Triângulo Equilátero: três lados iguais

    - Triângulo Isósceles: quaisquer dois lados iguais

    - Triângulo Escaleno: três lados diferentes

"""

l1 = int(input("Primeiro lado: "))
l2 = int(input("Segundo lado: "))
l3 = int(input("Terceiro lado: "))

if (l1 + l2) <= l3 or (l2 + l3) <= l1 or (l1 + l3) <= l2:
    print("Não é um triângulo")
elif l1 == l2 and l2 == l3:
    print("Equilátero")
elif l1 == l2 or l2 == l3 or l1 == l3:
    print("Isósceles")
elif l1 != l2 and l2 != l3 and l1 != l3:
    print("Escaleno")