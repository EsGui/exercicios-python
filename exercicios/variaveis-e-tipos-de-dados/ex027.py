'''
Leia um valor de área em hectares e apresente-o convertido em metros quadrados m².
A fórmula de conversão é: M = H * 10000, sendo M a área em metros quadrados e H
a área em hectares.
'''

print('Conversão de hectares para m²')
print('-'*30)

h = float(input('Digite um valor em hectares: '))
print('\n')

m = h * 10000

print(f'A conversão de {h} hectares para m² fica {m} m²')