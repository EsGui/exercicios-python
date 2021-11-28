'''
Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:

    - O total a pagar com o desconto de 10%;
    - O valor de cada parcela, no parcelamento de 3x sem juros;
    - A comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com des-
    conto)
    - A comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
'''

print('Calculando o valor do produto')
print('-'*30)
print('\n')

p = int(input('Digite o valor do produto R$ '))

# Calculos do menu
dez = p - (p * 10/100)
par = p / 3
com_vista = dez * 5/100
com_par = p * 5/100

print(f'O total a pagar com 10% de desconto R${dez:.2f}')
print(f'O valor de cada parcela, no parcelamento de 3x sem juros R${par:.2f}')
print(f'A comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto) R${com_vista:.2f}')
print(f'A comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total) R${com_par:.2f}')

