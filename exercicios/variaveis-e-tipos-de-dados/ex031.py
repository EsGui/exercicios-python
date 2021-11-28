'''
Leia um número inteiro e imprima o seu antecessor e o seu sucessor
'''

print('Antecessor e sucessor')
print('-'*30)

n = int(input('Digite um número: '))
print('\n')

a = n - 1
s = n + 1

print(f'''Antecessor: {a}
Sucessor: {s}''')
