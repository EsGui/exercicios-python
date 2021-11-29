'''
Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido pro-
porcionalmente ao valor que cada deu para a realização da aposta. Faça um programa
que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um
ganharia do prêmio com base no valor investido.
'''

print('Divisão de prêmio!')
print('-'*30)

amigo1 = int(input('1º aposta: '))
amigo2 = int(input('2º aposta: '))
amigo3 = int(input('3º aposta: '))
v_aposta = amigo1 + amigo2 + amigo3

p_amigo1 = v_aposta * (amigo1 * 100 / v_aposta)

print(int(p_amigo1))










