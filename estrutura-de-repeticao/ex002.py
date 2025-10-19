"""

Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
nome de usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

"""

while True:
    usuario = str(input("Digite seu nome de usuário: "))
    senha = str(input("Digite sua senha: "))

    if usuario == senha:
        print("Erro, o nome de usuário não pode ser igual a senha!")
    else:
        break
