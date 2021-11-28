'''
A importância de R$ 780.000,00 será dívidada entre três ganhadores de um concurso.
Sendo que da quantia total:

    - O primeiro ganhador receberá 46%;
    - O segundo ganhador receberá 32%;
    - O terceiro ganhador receberá o restante;

    Calcule e imprima a quantia ganha por cada um dos ganhadores
'''

print('Dividindo prêmio')
print('-'*30)
print('\n')

p = 780.000 - (780.000 * 46/100)
s = 780.000 - (780.000 * 32/100)
t = 780.000 - (p + s)

print(f'O primeiro ganhador vai receber R${p:.2f}')
print(f'O segundo ganhador vai receber R${s:.2f}')
print(f'O terceiro ganhador vai receber R${t:.2f}')

