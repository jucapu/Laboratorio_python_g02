"""Usando las propiedades de cadenas o string"""

"""Métodos de string"""

cadena = "Python para la predicción de fraudes bancarios o de préstamos"

#cadena_sin_espacio = cadena.split(sep="a")
cadena_sin_espacio = cadena.split()

print("Cadena separada por espacios en blanco dentro del string: {}".format(cadena_sin_espacio))

for palabra in cadena_sin_espacio:
    print(palabra)
