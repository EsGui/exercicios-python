'''
Leia um valor de massa em libras e apresente-o convertido em quilogramas. A fórmula
de conversão é: K = L * 0.45, sendo K a massa em quilogramas e L a massa em libras.
'''

print('Conversão de libras para quilogramas')
print('-'*30)

l = float(input('Digite uma massa em libras: '))
print('\n')

k = l * 0.45

print(f'A conversãod de {l} libras para quilogramas fica {k} quilogramas.')
