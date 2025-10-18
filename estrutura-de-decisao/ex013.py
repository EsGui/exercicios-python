"""

Faça um programa que leia um número e exiba o dia 
correspondente da semana (1-Domingo, 2-Segunda, 3-Terça,
4-Quarta, 5-Quinta, 6-Sexta, 7-Sábado)

"""

n = int(input("Digite um número de 1 a 7: "))

if n == 1:
    print("Domingo")
elif n == 2:
    print("Segunda")
elif n == 3:
    print("Terça")
elif n == 4:
    print("Quarta")
elif n == 5:
    print("Quinta")
elif n == 6:
    print("Sexta")
elif n == 7:
    print("Sábado")
else:
    print("Valor inválido")
