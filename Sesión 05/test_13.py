"""
    Programación orienta a objetos en Python
    Atributos
"""

class Carro:
    """Atributos"""
    ruedas = 4

    """Constructor: Valores que van a tener por defecto mi clase que se le instancia en una variable"""

    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    """Métodos: So las funciones de la clase"""

    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0
        self.velocidad = velocidad


carro_1 = Carro("Blanco", 70)

print("El color de mi primer carro es: {}".format(carro_1.color))

carro_2 = Carro("Rojo", 90)
carro_2.marchas = 300000

print("El número de marchas de mi segundo carro es: {}".format(carro_2.marchas))

"""IMPORTANTE"""
"""No es posible llamar a un atributo de datos que se la ha asignado a otra instancia de la clase"""
#print(carro_1.marchas)

