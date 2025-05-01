"""
Programa: Programa que pregunta al usuario
Autor: Josafat Montiel Ortiz
"""

# Variable
persona = {}
keyNombre = 'nombre'
keyEdad = 'edad'
keyDireccion = 'direccion'
keyCelular = 'celular'


# Programa Principal
print ("Ejercicio de Diccionario")
nombre = input("¿Puedes proporcionarme tu nombre?: ")
edad = input("¿Puedes ingresar tu edad?: ")
direccion = input("¿Puedes introducir tu dirección?: ")
celular = input("¿Cuál es tu número de celular?: ")

persona = {keyNombre:nombre,keyEdad:edad,keyDireccion:direccion,keyCelular:celular}

print("{} tiene {} años, vive en {} y su numero de telefono es {}".format(persona[keyNombre],persona[keyEdad],persona[keyDireccion],persona[keyCelular]))

