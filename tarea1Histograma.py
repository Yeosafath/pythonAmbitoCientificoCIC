"""
Programa: Programa que imprime el Histograma de frecuencias de una serie de datos.
          El programa preguntará al usuario el número de series a graficar,
          Pedirá el nombre y la frecuencia de cada serie e
          Imprimirá el Histograma de esas series
          Se usará el asterisco (*) para representar cada histograma
Autor: Josafat Montiel Ortiz
email: yeosafath@gmail.com
"""

# Variables
totalHistogramas = 0
listaHistogramas = []

# Programa Principal
totalHistogramas = int(input("Introduce el número de Histogramas a representar: "))

for hist in range(totalHistogramas):
    diccionarioHistograma = {
        'nombre': input("Nombre del Histograma {} : ".format(hist+1)),
        'frecuencia': int(input("Frecuencia del Histograma {} : ".format(hist+1)))
    }
    listaHistogramas.append(diccionarioHistograma)

for hist in range(len(listaHistogramas)):
    print(listaHistogramas[hist]['nombre']+' '*(15-len(listaHistogramas[hist]['nombre']))+'*'*listaHistogramas[hist]['frecuencia'])
