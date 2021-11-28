'''
Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-
se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso,
ele paga 7% de imposto sobre o salário-base.
'''

print('Calculando 5% de gratificação e 7% de imposto do salário')
print('-'*30)
print('\n')

sb = int(input('Digite o seu salário base R$ '))
g = sb + (sb * 5/100)
i = g - (g * 7/100)

print(f'O salário do funcionário será de R${i}')
