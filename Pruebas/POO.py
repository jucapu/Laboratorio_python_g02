"""Programacion orienta a objetos"""


class Carro:

    """atributos"""

    ruedas = 4

    """Constructor: valores que van a tener pór defecto mi clase que se le instancia en una variable"""

    def __init__(self, color,  aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    """metodos: son las funciones de la clase"""

    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion


    def frena(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0
            self.velocidad = velocidad
"""instanciamos nuestra clase"""

carro_1 = Carro("Negro", 100)
print("El color del primer carro es: {}".format(carro_1.color))
print("La aceleracion del primer carro es: {}".format(carro_1.aceleracion))
print("cuantas ruedas tiene primer carro es: {}".format(carro_1.ruedas))

carro_2 = Carro("Negro", 100)

carro_2.marchas = 30000

print("cuantas ruedas tiene primer carro es: {}".format(carro_2.marchas))

print("cuantas ruedas tiene primer carro es: {}".format(carro_1.velocidad))

carro_1.acelerar()
carro_1.acelerar()

print("cuantas ruedas tiene primer carro es: {}".format(carro_1.velocidad))

carro_1.frena()

print("cuantas ruedas tiene primer carro es: {}".format(carro_1.velocidad))
