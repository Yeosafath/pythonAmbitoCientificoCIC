"""
Problema: Programa que calcula el area de un triangulo
Autor: Josafat Montiel Ortiz
"""
base = input("Dame la base del triangulo: ")
altura = input("Dame la altura del triangulo: ")

print(base)

if base == '':
    base = 0
else:
    base = float(base)

if altura == '':
    altura = 0
else:
    altura = float(altura)

area_triangulo =  base * altura / 2
print ("El área del triangulo es: " + str(area_triangulo))
