"""

Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do imposto de Renda, que depende
do sálario bruto (conforme a tabela abaixo) e 3% para o Sindicato
e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
(é a empresa que deposita). O Salário Líquido corresponde ao Sálario Bruto
menos os descontos. O programa deveá pedir ao usuário o vaor da sua hora
e a quantidade de horas trabalhadas no mês

Desconto do IR: 
    - Salário bruto até 900 (inclusive) - isento
    - Salário bruto até 1500 (inclusive) - desconto de 5%
    - Salário bruto até 2500 (inclusive) - desconto de 10%
    - Salário bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de horas é 220

Salario Bruto: (5 * 220)                       : R$ 1100,00
(-) IR (5%)                                    : R$ 55,00
(-) INSS (10%)                                 : R$ 110,00
FGTS (11%)                                     : R$ 121,00
Total de descontos                             : R$ 165,00
Salário Liquido                                : R$ 935,00
"""

valor_hora = float(input("Quanto vale a sua hora de trabalho? "))
valor_mes = float(input("Quantas horas você trabalhou no mês? "))

salario_bruto = valor_hora * valor_mes

if salario_bruto <= 900:
    inss = (10/100) * salario_bruto
    fgts = (11/100) * salario_bruto
    total_desconto = inss
    salario_liquido = salario_bruto - total_desconto
    print(f"Salário Bruto: R${salario_bruto}"
          f"IR: Isento"
          f"INSS: R${inss}"
          f"FGTS: R${fgts}"
          f"Total de descontos: R${total_desconto}"
          f"Salário liquido: R${salario_liquido}")
elif 900 <= salario_bruto <= 1500:
    ir = (5/100) * salario_bruto
    inss = (10/100) * salario_bruto
    fgts = (11/100) * salario_bruto
    total_desconto = ir + inss
    salario_liquido = salario_bruto - total_desconto
    print(f"Salário Bruto: R${salario_bruto}"
          f"IR: R${ir}"
          f"INSS: R${inss}"
          f"FGTS: R${fgts}"
          f"Total de descontos: R${total_desconto}"
          f"Salário liquido: R${salario_liquido}")
elif 1500 <= salario_bruto <= 2500:
    ir = (10/100) * salario_bruto
    inss = (10/100) * salario_bruto
    fgts = (11/100) * salario_bruto
    total_desconto = ir + inss
    salario_liquido = salario_bruto - total_desconto
    print(f"Salário Bruto: R${salario_bruto}"
          f"IR: R${ir}"
          f"INSS: R${inss}"
          f"FGTS: R${fgts}"
          f"Total de descontos: R${total_desconto}"
          f"Salário liquido: R${salario_liquido}")
elif salario_bruto > 2500:
    ir = (20/100) * salario_bruto
    inss = (10/100) * salario_bruto
    fgts = (11/100) * salario_bruto
    total_desconto = ir + inss
    salario_liquido = salario_bruto - total_desconto
    print(f"Salário Bruto: R${salario_bruto}"
          f"IR: R${ir}"
          f"INSS: R${inss}"
          f"FGTS: R${fgts}"
          f"Total de descontos: R${total_desconto}"
          f"Salário liquido: R${salario_liquido}")


