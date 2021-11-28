'''
Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).
Gere outro número formado pelos dígitos invertidos do número lido. Exemplo:

    - NúmeroLido = 123
    - NúmeroGerado = 321
'''

print('Invertendo ordem de um número')
print('-'*30)
print('\n')

n = int(input('Digite um número: '))

print(f'Número invertido {str(n)[::-1]}')

