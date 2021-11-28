'''
Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de
sua idade e do ano atual.
'''

print('Calculando idade')
print('-'*30)
print('\n')

ano_n = int(input('Digite o ano atual: '))
i = int(input('Digite a sua idade: '))

calc = ano_n - i

print(f'Você nasceu em {calc}')