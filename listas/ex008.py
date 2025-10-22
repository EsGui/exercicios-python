"""

Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu
respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

"""

vetor_idade = []
vetor_altura = []

for pessoas in range(1, 6):
    print(f"{pessoas}° pessoa: ")
    for data in range(1):
        idade = int(input("Digite sua idade: "))
        altura = float(input("Digite sua altura: "))
        vetor_idade.append(idade)
        vetor_altura.append(altura)

for i in range(len(vetor_idade) - 1, -1, -1):
    print(vetor_idade[i], end=" ")
    print(vetor_altura[i])



