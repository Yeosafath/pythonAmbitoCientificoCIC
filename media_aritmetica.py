"""
Programa: Obtiene la media aritmética de dos números
Autor: Josafat Montiel Ortiz
"""

# variables
numStr1 = 0
numStr2 = 0
num1 = 0
num2 = 0
mediaAritmetica = 0

# Programa Principal

numStr1 = input("Dame el valor del 1er número: ")
numStr2 = input("Dame el valor del 2o número: ")

if numStr1 == '':
    num1 = 0
else:
    num1 = float(numStr1)

if numStr2 == '':
    num2 = 0
else:
    num2 = float(numStr2)

mediaAritmetica = (num1+ num2)/2
print("La media de los dos núemros es: ",mediaAritmetica)

