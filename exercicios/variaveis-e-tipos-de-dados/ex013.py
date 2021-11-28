'''
Leia uma distância em quilômetros e apresente-a convertida em milhas. A fórmula de
conversão é: M = k / 1.61 sendo K a distância em quilômetros e M em milhas.
'''

print('Conversão de quilômetros para milhas')
print('-'*30)

k = float(input('Digite uma distância em quilômetros: '))
print('\n')

m = k / 1.61

print(f'A conversão de {k} quilômetros para milhas fica {m} milhas')
