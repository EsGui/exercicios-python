'''
Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo
em vista que o desconto foi de 12%.
'''

print('Calculando desconto')
print('-'*30)

p = float(input('Digite o valor de um produto R$'))
print('\n')

d = p - (p * 12/100)

print(f'O valor do produto é R${p:.2f} e com desconto de 12% fica R${d:.2f}')
