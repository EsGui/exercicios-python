'''
Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que
ele recebeu um aumento de 25%.
'''

print('Calculando aumento')
print('-'*30)

s = float(input('Digite o salário atual do funcionário: R$'))
print('\n')

a = s + (s * 25/100)

print(f'O salário do funcionário era de R${s} e com aumento de 25% passará a ficar R${a:.2f}')