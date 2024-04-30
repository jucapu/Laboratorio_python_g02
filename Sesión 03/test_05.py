"""Uso del flujo condicional: if"""

edad = int(input("Ingrese su edad: "))

if 0 < edad < 18:
    print("Usted es menor de edad")
elif 18 <= edad < 65:
    print("Usted es una persona adulta")
elif 100 >= edad > 65:
    print("Usted es una persona adulta de la tercera edad")
else:
    print("Usted ha ingresado una edad incorrecta")
