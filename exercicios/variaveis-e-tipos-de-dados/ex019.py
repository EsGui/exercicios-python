'''
Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m³. A
fórmula de conversão é: M = l / 1000, sendo L o volume em litros e M o volume em metros
cúbicos.
'''
print('Convertendo litros para m³')
print('-'*30)

l = float(input('Digite um volume em litros: '))
print('\n')

m = l / 1000

print(f'A conversão de {l} litros convertido para m³ fica {m}m³')
