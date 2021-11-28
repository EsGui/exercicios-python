'''
Leia um valor de área em acres e apresente-o convertido em metros quadrados m². A
fórmula de conversão é: m = a * 4048.58, sendo M a área em metros quadrados e A a
área em acres.
'''

print('Conversão de acres para m²')
print('-'*30)

a = float(input('Digite um valor em acres: '))
print('\n')

m = a * 4048.58

print(f'A conversão de {a} acres para m² fica {m} m²')
