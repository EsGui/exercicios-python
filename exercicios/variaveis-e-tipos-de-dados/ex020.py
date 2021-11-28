'''
Leia um valor de massa em quilôgramas e apresente-o convertido em libras. A fórmula
de conversão é: L = K / 0.45, sendo K a massa em quilogramas e L a massa em libras.
'''

print('Conversão de quilôgramas para libras')
print('-'*30)

k = float(input('DIgite uma massa em quilogramas: '))
print('\n')

l = k / 0.45

print(f'A conversão de {k} quilogramas para libras fica {l} libras')