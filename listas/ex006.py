"""

Faça um programa que peça as quatros notas de 10 alunos, calcule e armazene num vetor a
média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0

"""


vetor_media = []
soma_notas = 0

for alunos in range(1, 11):
    print(f"{alunos}° aluno")
    for notas in range(1, 5):
        n = float(input(f"Digite a {notas}° nota: "))
        soma_notas += n
    vetor_media.append(soma_notas / 4)
    soma_notas = 0

for n in vetor_media:
    if n >= 7.0:
        print(n)
