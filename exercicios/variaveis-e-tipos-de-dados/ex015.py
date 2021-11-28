'''
Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão
é: G = R * 180/TT, sendo G o ângulo em graus e r em radianos e TT = 3.14.
'''

print('Conversão de radianos para graus')
print('-'*30)

r = float(input('Digite um valor em radianos: '))
print('\n')

g = r * 180/3.14

print(f'A conversão de {r} radianos para graus fica {g} graus')
