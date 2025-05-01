

"""
Programa: Calcula el índice de masa corporal
Autor: Josafat Montiel Ortiz
"""

# variables
pesoStr = 0
alturaStr = 0
peso = 0
altura = 0
indiceMasaCorporal = 0

# Programa Principal

print ("Cálculo del Índice de Masa Corporal")
pesoStr = input("Peso (Kg): ")
alturaStr = input("Altura (m): ")

if pesoStr == '':
    peso = 0
else:
    peso = float(pesoStr)
    if peso < 0:
        peso = 0

if alturaStr == '':
    altura = 1
else:
    altura = float(alturaStr)
    if altura < 0:
        altura = 1

indiceMasaCorporal = peso / (altura ** 2)
print("El indice de masa corporal es: ",indiceMasaCorporal)

