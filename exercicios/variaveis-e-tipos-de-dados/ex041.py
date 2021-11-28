'''
Faça um programa que leia o valor da hora de trabalho (em reais) e números de horas
trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre
o valor calculado.
'''

print('Calculando 10% a mais no salário')
print('-'*30)
print('\n')

h = float(input('Digite o valor por cada hora trabalhada R$'))
m = int(input('Digite o número de horas trabalhadas no mês: '))

s = h * m
d = s + (s * 10/100)

print(f'O salário do funcionário será de R${d}')

