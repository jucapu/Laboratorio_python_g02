"""Entradas y salidas"""
"""Referencias a dos o más variables"""

var_1 = input("Ingrese nombre de usuario: ")
var_2 = input("Ingrese su nombre: ")
var_3 = input("Ingrese su edad: ")

#usuario = var_1
#nombre = var_2
#edad = var_3

usuario, nombre, edad = var_1, var_2, var_3

print("Su nombre de usuario es: {} y tiene {} años".format(usuario, edad))
