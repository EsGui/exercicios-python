'''
Leia um valor de comprimento em metros e apresente-o convertido em jardas. A fórmulça
de conversão é: J = M / 0.91, sendo J o comprimento em jardas e M o comprimento em
metros.
'''

print('Converção de metros para jardas')
print('-'*30)

m = float(input('Digite um comprimento em metros: '))
print('\n')

j = m / 0.91

print(f'A conversão de {m} metros para jardas fica {j} jardas')

