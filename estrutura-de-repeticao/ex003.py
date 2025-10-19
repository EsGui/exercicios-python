"""

Faça um programa que leia e valide as seguintes informações:

    - Nome: maior que 3 caracteres;
    - Idade: entre 0 e 150;
    - Salário: maior que zero;
    - Estado Civil: 's', 'c', 'v', 'd'

"""

while True:
    nome = str(input("Digite o seu nome: "))
    if len(nome) > 3:
        break
    else:
        print("O nome deve ter mais de três digitos")

while True:
    idade = int(input("Digite sua idade: "))
    if 0 < idade <= 150:
        break
    else:
        print("A idade deve estar entre 0 e 150")

while True:
    salario = int(input("Digite seu salário: "))
    if salario > 0:
        break
    else:
        print("O salario deve ser um valor maior do que 0")

while True:
    estado_civil = str(input("Digite seu estado civil: "))
    if estado_civil in "scvd":
        break
    else:
        print("Valor do estado civil esta inválido")



