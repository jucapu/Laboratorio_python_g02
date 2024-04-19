
"""Diccionarios en Python"""

"""del: elmina un key y su valor correspondiente en el diccionario"""

var_1 = {"nombre": "Margaret", "edad": 27, "promedio": 16}

"""Para eliminar valores de nuestro diccionario usamos a del delante de la variable"""

del var_1["edad"]
del var_1["nombre"]

print("El diccionario actualizado tiene los siguientes valores: {}".format(var_1))
