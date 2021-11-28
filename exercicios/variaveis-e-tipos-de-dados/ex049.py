'''
Faça um programa para leia o horário (hora, minuto e segundo) de início e a duração, em
segundos, de uma experiência biológica. O programa deve resultar com o novo horário
(hora, minuto e segundo) do termino da mesma.
'''

print('Experiência biológica')

print('Início')
print('-'*30)

h_i = int(input('Digite a hora: '))
m_i = int(input('Digite o minuto: '))
s_i = int(input('Digite o segundo: '))

print('\n')

d = int(input('Digite a duração: '))

print(f'A duração será de {d // 3600} horas {d // 60} minutos e {d} Segundos')

print(f'O terminio será de {(d // 3600) + h_i} horas {(d // 60) + m_i} minutos {(d) + s_i}')