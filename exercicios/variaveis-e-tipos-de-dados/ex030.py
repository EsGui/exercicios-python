'''
Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente
em dólares.
'''

print('Cotação do dólar')
print('-'*30)

real = float(input('Digite um valor em reais: '))
print('\n')

dolar = real / 5.54

print(f'A conversão de R${real} para dólar fica ${dolar}')
