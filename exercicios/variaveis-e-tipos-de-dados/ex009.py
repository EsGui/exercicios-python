'''
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A
fórmula de conversão é: K = C + 273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin.
'''

print('Conversão de Celsius para Kelvin')
print('-'*30)

c = float(input('Digite uma temperatura em Kelvin: '))
print('\n')

k = c + 273.15

print(f'A conversão de {c}ºC para ºK fica {k}ºK')
