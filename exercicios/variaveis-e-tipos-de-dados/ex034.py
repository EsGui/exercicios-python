'''
Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente.
A área do círculo é TT * raio², considere TT = 3.141592.
'''

print('Calculando área do círculo')
print('-'*30)

r = float(input('Digite o valor do raio: '))
print('\n')

a = 3.141592 * (r ** 2)

print(f'A área do círculo é igual á {a}')
