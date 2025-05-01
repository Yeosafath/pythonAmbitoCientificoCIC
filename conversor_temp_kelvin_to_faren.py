"""
Programa: Conviertre temperatura de °K a °C y °F
Autor: Josafat Montiel Ortiz
"""

# variables
gradosKelvinStr = 0
gradosKelvin = 0
gradosCentigrados = 0
gradosFarenheit = 0

# Programa Principal

print ("Convierte la temperatura de Grados Kelvin a °Centrigrados y °Farenheit")
gradosKelvinStr = input("Temperatura en °K: ")

if gradosKelvinStr == '':
    gradosKelvin = 0
else:
    gradosKelvin = float(gradosKelvinStr)

gradosCentigrados = round(gradosKelvin - 273.15,2)
gradosFarenheit = round(gradosCentigrados * 9 /5 + 32,2)

print("La temperatura: ", gradosKelvin, "°K, corresponde a:", gradosCentigrados, "°C")
print("La temperatura: ", gradosKelvin, "°K, corresponde a:", gradosFarenheit, "°F")


