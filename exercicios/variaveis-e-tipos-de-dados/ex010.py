'''
Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s
(metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade em
km/h e M em m/s.
'''

print('Convertendo km/h para m/s')
print('-'*30)

k = float(input('Digite uma velocidade em km/h: '))
print('\n')

m = k / 3.6

print(f'A conversão de {k} km/h para m/s fica {m}m/s')
