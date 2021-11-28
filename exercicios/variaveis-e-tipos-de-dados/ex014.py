'''
Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão
é: R = G * TT/180, sendo G o ângulo em graus e R em radianos e TT = 3.14.
'''

print('Conversão de graus para radianos')
print('-'*30)

g = float(input('Digite um ângulo em graus: '))
print('\n')

r = g * 3.14/180

print(f'A conversão de {g} graus para radinos fica {r} radianos')
