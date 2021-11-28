'''
Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A
fórmula de conversão é: C = K - 273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin.
'''

print('Conversão de Kelvin para Celius')
print('-'*30)

k = float(input('Digite uma temperatura em Kelvin: '))
print('\n')

c = k - 273.15

print(f'A conversão de {k} ºK para ºC fica {c}ºC')
