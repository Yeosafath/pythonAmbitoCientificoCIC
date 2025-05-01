"""
Programa: Obtener el maximo de 3 numeros
Autor: Josafat Montiel Ortiz
email: yeosafath@gmail.com
"""

# Variable
max = None

num1 = int(input('Captura el 1er número: '))3
num2 = int(input('Captura el 2o número: '))
num3 = int(input('Captura el 3er número: '))

if num1 < num2:
    max = num2
else:
    max = num1

if num3 > max:
    max = num3

print ("El máximo de los números {}, {}, {} es: {}".format(num1,num2,num3,max))