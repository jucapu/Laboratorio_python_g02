"""Programacion Funcional"""

var_1 = 50
var_2 = 250



"""Input: Dos variables que pasaran por paramentro de la funcion"""

"""a, v: parametro de la funcion : sumar"""


def sumar(a, b):
    suma = a + b
    return suma

resultado = sumar(var_1, var_2)

print(resultado)


def sumar2(c, d):
    return c + d

print(sumar2(100, 200))


def multiplicacion(a, b, c=100):
    return a * b * c

print("El resulado de  mi funcion es: {}".format(multiplicacion(100, 200)))


num1 = int(input("Introduce primer numero: "))
num2 = int(input("Introduce segundo numero: "))
num3 = int(input("Introduce tercero numero: "))
num4 = int(input("Introduce cuarto numero: "))

def num_mayor(z, x, v, n):
    if z > x and z > n and z > v:
        return z
    if x > z and x > v and x > n:
        return x
    if v > z and v > x and v > n:
        return v
    else:
        return n

print(num_mayor(num1, num2, num3, num4))

print(num_mayor(num1, num2, num3, num4)**3)