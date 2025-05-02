"""
Programa: Programa que solicita al usuario un numero e imprima la tabla de multiplicar de dicho numero
Autor: Josafat Montiel Ortiz
email: yeosafath@gmail.com
"""

# Input
baseTablaMultiplicar =  int(input('Indica la tabla de multiplicar que deseas visualizar: '))

for x in range(1,11):
    print(" {} x {} = {} ".format(baseTablaMultiplicar,x,baseTablaMultiplicar*x))
