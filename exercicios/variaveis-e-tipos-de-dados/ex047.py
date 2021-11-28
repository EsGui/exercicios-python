'''
Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha
'''

print('Imprimindo 1 dígito por linha na tela')
print('-'*30)
print('\n')

n = int(input('Digite um número inteiro: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print(m)
print(c)
print(d)
print(u)