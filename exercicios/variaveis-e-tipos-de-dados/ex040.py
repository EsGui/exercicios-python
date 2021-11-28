'''
Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite
o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser
paga, sabendo-se que são descontados 8% para imposto de renda.
'''

print('Calculando imposto de 8% sobre o salário')
print('-'*30)
print('\n')

f = int(input('Salário diário do funcionário: R$'))
s = f * 30
d = s - (s * 8/100)

print(f'O funcionário recebera a quantia líquida de R${d:.2f}')
