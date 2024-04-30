"""Usando las propiedades de cadenas o string"""

"""Replace"""

cadena = "Conexión a Base de Datos con Python"

cadena_2 = cadena.replace(cadena[0:6], "pppppppp")
print("Cadena con reemplazo, tiene el siguiente valor actualizado: {}".format(cadena_2))

"""Eliminación de espacion en blaco de mi cadena (después)"""
cadena_3 = "Conexión a Base de Datos con Python           "
cadena_4 = cadena_3.rstrip()
print(cadena_3)
print("Mi cadena actualizada sin espacios en blanco es la siguiente: {}".format(cadena_4))
