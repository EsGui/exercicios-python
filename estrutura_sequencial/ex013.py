"""

Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes, usando a seguinte fórmula:

    - Para Megabytes: Gigabytes * 1024
    - Para Kilobytes: Gigabytes * 1024 * 1024

Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes.

"""

arquivo = float(input("arquivo: "))

mega_bytes = arquivo * 1024

kilo_bytes = arquivo * 1024 * 2

print(f"Conversão Megabytes = {mega_bytes}")
print(f"Conversão Kilobytes = {kilo_bytes}")

