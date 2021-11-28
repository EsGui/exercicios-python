'''
Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.
A fórmula de conversão é: P = C / 2.54, sendo C o comprimento em centímetros e P o
comprimento em polegadas
'''

print('Conversão de centímetros para polegadas')
print('-'*30)

c = float(input('Digite um comprimento em centímetros: '))
print('\n')

p = c / 2.54

print(f'A conversão de {c} centímetros para polegadas fica {p} polegadas')