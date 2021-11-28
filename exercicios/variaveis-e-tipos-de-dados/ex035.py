'''
Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = raiz de a² + b². Faça um programa que receba os valores de a e b e calcule
o valor da hipotenusa atravéz da equação. Imprima o resultado dessa operação.
'''

print('Calculando hipotenusa')
print('-'*30)

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
print('\n')

h = a ** 2 + b ** 2

print(f'O resultado da hipotenusa é {h}')
