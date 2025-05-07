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

"""
Desglose de llamados as la función Fibonacci:
    Init Call:  fibonacci(10,0,1)
    1Call:      0<10
                fibonacci(10,0+1,0)
    2Call:      1<10
                fibonacci(10,1+0,1)
    3Call:      1<10
                fibonacci(10,1+1,1)
    4Call:      2<10
                fibonacci(10,2+1,2)
    5Call:      3<10
                fibonacci(10,3+2,3)
    6Call:      5<10
                fibonacci(10,5+3,5)
    7Call:      8<10
                fibonacci(10,8+5,8)
    8Call:      13<10
                #Termina la función y termina el llamado recurrente
                #Regresando el control a la función llamadora, en este caso
                #a la función del 7Call
    Continuación flujo 7Call: print(sumaFibonacci) => print(8), termina flujo 7Call, regresa llamado a 6Call
    Continuación flujo 6Call: print(sumaFibonacci) => print(5), termina flujo 6Call, regresa llamado a 5Call
    Continuación flujo 5Call: print(sumaFibonacci) => print(3), termina flujo 5Call, regresa llamado a 4Call
    Continuación flujo 4Call: print(sumaFibonacci) => print(2), termina flujo 4Call, regresa llamado a 3Call
    Continuación flujo 3Call: print(sumaFibonacci) => print(1), termina flujo 3Call, regresa llamado a 2Call
    Continuación flujo 2Call: print(sumaFibonacci) => print(1), termina flujo 2Call, regresa llamado a 1Call
    Continuación flujo 1Call: print(sumaFibonacci) => print(0), termina flujo 1Call y termina toda la función, sale. 
"""

def fibonacci(limiteSerie, sumaFibonacci, auxFibonacci):
    if sumaFibonacci < limiteSerie:
        fibonacci(limiteSerie, sumaFibonacci + auxFibonacci, sumaFibonacci)
        print(sumaFibonacci)

def fibonacciLista(limiteSerie, sumaFibonacci, auxFibonacci,listaFibonacci):
    if sumaFibonacci < limiteSerie:
        fibonacciLista(limiteSerie, sumaFibonacci + auxFibonacci, sumaFibonacci,listaFibonacci)
        listaFibonacci.append(sumaFibonacci)
        return listaFibonacci

limiteSerieFibonacci=int(input("Introduce el límite del Cálculo de la Serie Fibonacci: "))

# Impresión por cada ciclo
fibonacci(limiteSerieFibonacci,0,1)

# Impresión una sola linea
listaFibonacci = fibonacciLista(limiteSerieFibonacci,0,1,[])
listaFibonacci.reverse()
print(listaFibonacci)


