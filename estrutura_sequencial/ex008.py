"""

Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

"""

salario_por_hora = float(input("Digite quanto você recebe por hora: "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas"))

total_salario = salario_por_hora * horas_trabalhadas

print(f"Salário do mês = {total_salario}")