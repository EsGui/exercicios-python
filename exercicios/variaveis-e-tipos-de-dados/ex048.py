'''
Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
'''

print('Convertendo segundos para horas, minutos e segundos')
print('-'*30)
print('\n')

s = int(input('Digite um número em segundos: '))

m = s / 60
h = s / 3600

print(f'{int(h)} horas {int(m)} minutos {s} segundos')

