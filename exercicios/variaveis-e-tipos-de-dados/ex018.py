'''
Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros. A
fórmula de conversão é: L = 1000 * M, sendo L o volume em litros e M o volume em
metros cúbicos
'''

print('Conversão de m³ para litros')
print('-'*30)

m = float(input('Digite um volume em m³: '))
print('\n')

l = 1000 * m

print(f'A conversão de {m}m³ para litros fica {l} litros.')
