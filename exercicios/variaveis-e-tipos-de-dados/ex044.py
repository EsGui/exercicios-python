'''
Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir
seu objetivo.
'''

print('Calculando objetivo do usuário')
print('-'*30)
print('\n')

d = float(input('Digite a altura de cada degrau: '))
a = float(input('Digite altura que deseja alcançar: '))

calc = d * a

print(f'Para o usuário atingir seu objetivo ele deverá subir {calc} degraus')