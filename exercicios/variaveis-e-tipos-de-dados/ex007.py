'''
Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C = 5.0 * (F - 32.0) / 9.0, sendo C a temperatura em Celsius
e F a temperatura em Fahrenheit.
'''

print('Conversão de Fahrenheit para Celsius')
print('-'*30)

f = float(input('Digite uma temperatura em ºF: '))
print('\n')

c = 5.0 * (f - 32.0) / 9.0

print(f'A conversão de {f}ºF para ºC é {c}ºC')
