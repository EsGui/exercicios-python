"""

Faça um programa que pergunte em que turno você estuda. Peça para digitar:

    - M - Masculino
    - V - Vespertino
    - N - Noturno

Imprima a mensagem "Bom dia!", "Boa Noite!" ou "Valor Inválido", conforme o caso

"""

turno = input("Em qual turno você estuda, M/V/N? ").lower()

if turno == "m" or turno == "matutino":
    print("Bom dia!")
elif turno == "v" or turno == "vespertido":
    print("Boa tarde!")
elif turno == "n" or turno == "noturno":
    print("Boa noite!")
else:
    print("Valor inválido")