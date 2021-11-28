'''
Leia um número inteiro e imprima a soma do sucessor de seu triplo com o sucessor de
seu dobro.
'''

print('Somando sucessores triplos e dobros')
print('-'*30)

n = int(input('Digite um número: '))
print('\n')

st = (n ** 3 + 1) + (n ** 2 + 1)

print(f'O resultado é {st}')
