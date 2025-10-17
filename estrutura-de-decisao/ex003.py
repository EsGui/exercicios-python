"""

Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:

    - F - Feminino
    - M - Masculino
    - Sexo inválido

"""

genero = input("Digite M ou F: ").lower()

if genero == "m":
    print("Masculino")
elif genero == "f":
    print("Feminino")
else:
    print("Sexo inválido")