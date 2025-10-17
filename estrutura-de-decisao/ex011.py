"""

As organizações tabajara resolveram dar um aumento de salário aos seus colaboradores
e lhe contrataram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o 
seguinte critério, baseado no salário atual:

    - Salário até R$ 280,00 (incluindo): aumento de 20%
    - Salário entre R$ 280,00 e R$ 700,00: aumento de 15%
    - Salário entre R$ 700,00 e R$ 1500,00: aumento de 10%
    - Salário de R$ 1500,00 em diante: aumento de 5% Após o aumento
    ser realizado, informa na tela:
        - O salário antes do reajuste;
        - O percentual de aumento aplicado
        - O valor do aumento;
        - O novo salário, após o aumento.

"""

salario = float(input("Digite o salário de um colaborador: R$"))

if salario <= 280.00:
    reajuste = (20/100) * salario
    print(f"Sálario até R$ 280,00 (incluindo): aumento de 20% = R${reajuste + salario}")
elif 280.00 < salario <= 700.00:
    reajuste = (15/100) * salario
    print(f"Salário entre R$ 280,00 e R$ 700,00: aumento de 15% = R${reajuste + salario}")
elif 700.00 < salario <= 1500.00:
    reajuste = (10/100) * salario
    print(f"Salário entre R$ 700,00 e R$ 1500,00: aumento de 10% = R${reajuste + salario}")
else:
    reajuste = (5/100) * salario
    print(f"Salário antes do reajuste = R${salario}\n "
          f"O percentual de aumento aplicado = 5% \n "
          f"Valor do aumento = {reajuste} \n"
          f"Novo salário, após aumento = R${reajuste + salario}")
