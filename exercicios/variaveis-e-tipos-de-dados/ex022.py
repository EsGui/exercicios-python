'''
Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula
de conversão é: M = 0,91 * J, sendo J o comprimento em jardas e M o comprimento
em metros.
'''

print('Conversão de jardas para metros')
print('-'*30)

j = float(input('Digite um comprimento em jardas: '))
print('\n')

m = 0.91 * j

print(f'A conversão de {j} jardas para metros fica {m} metros')
