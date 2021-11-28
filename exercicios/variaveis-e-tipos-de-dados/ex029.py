'''
Leia quatro notas, calcule a média aritmética e imprima o resultado.
'''

print('Média aritmética')
print('-'*30)

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
print('\n')

media = (n1 + n2 + n3 + n4) / 4

print(f'A média aritmética das notas informadas é igual á {media}')