'''
Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de
conversão é: K = 1,61 * M, sendo K a distância em quilômetros e M em milhas.
'''

print('Conversão de milhas para quilômetros')
print('-'*30)

m = float(input('Digite uma distância em milhas: '))
print('\n')

k = 1.61 * m

print(f'A conversão de {m} milhas para quilômetros fica {k} quilômetros')
