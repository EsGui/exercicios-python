'''
Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume
de um cilindro circular é calculado por meio da seguinte fórmula: V = TT * raio² * altura,
onde TT = 3.141592.
'''

print('Calculando o volume de um cilindro')
print('-'*30)

a = float(input('Digite uma altura: '))
r = float(input('Digite um raio: '))
print('\n')

v = 3.141592 * (r ** 2 * a)

print(f'O valor referente ao volume do cílindro é {v}')

