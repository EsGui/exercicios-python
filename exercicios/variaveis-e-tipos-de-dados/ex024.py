'''
Leia um valor de área em metros quadrados m² e apresente-o convertidos em acres. A
fórmula de conversão é: A = M * 0,000247, sendo M a área em metros quadrados e A
a área em acres.
'''

print('Conversão de m² para acres')
print('-'*30)

m = float(input('Digite uma área em metros: '))
print('\n')

a = m * 0.000247

print(f'A conversão de {m} m² para acres fica {a}')
