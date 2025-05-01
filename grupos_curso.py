"""
Programa: Los alumnos de un curso se deben dividir en dos grupos [G1 y G2]
          esto se hará de aacuerdo al genero y al nombre. El grupo G1 debe
          estar formado por las mujeres cuyo nombre sea anterior a la letra
          M y los hombres con un nombre posterior a la N. El grupo G2, por
          el resto.
          Se debe generar el programa que pregunta al alumno su nombre y
          género y le muestre en pantalla el grupo que le corresponde
Autor: Josafat Montiel Ortiz
email: yeosafath@gmail.com
"""
from dataclasses import asdict

# Variable
nombreAlumno = None
generoAlumno = None

nombreAlumno = input("Nombre del Alumno: ")
generoAlumno = input("Género del Alumno: ")

if generoAlumno[0].capitalize() == 'M' and nombreAlumno[0].capitalize() > 'N' or \
   generoAlumno[0].capitalize() == 'F' and nombreAlumno[0].capitalize() < 'M':
    grupo = 'G1'
else:
    grupo = 'G2'

print ('El alumno pertence al grupo:' + grupo)