"""
Programa: La serie de Fibonacci es una sucesión de números ordenados, descrita por el
          matemático italiano Leonardo de Pisa, la serie inicia con los números 0, 1 y cada
          número subsecuente es la suma de los dos elementos anteriores, p.e.,
          0, 1, 1, 2, 3, 5, 8, ....

          Escriba una función que reciba un número que representa un límite e imprima los
          números de fibonacci menores que el límite.
autor: Josafat Peniel Montiel Ortiz
email: yeosafath@gmail.com
"""

def fibonacci(limiteSerie, sumaFibonacci, auxFibonacci):
    if sumaFibonacci < limiteSerie:
        fibonacci(limiteSerie, sumaFibonacci + auxFibonacci, sumaFibonacci)
        print(sumaFibonacci)


fibonacci(50,0,1)

