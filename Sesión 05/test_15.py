"""
    Programación orienta a objetos en Python
    Herencia
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


"""Aplicando Herencia"""
"""Creamos nuestra clase hija"""


class CarroVolador(Carro):

    ruedas = 6

    def __init__(self, color, aceleracion, estadoVolando = False):

        super().__init__(color, aceleracion)
        self.estadoVolando = estadoVolando

    def vuela(self):
        self.estadoVolando = True

    def aterriza(self):
        self.estadoVolando = False


carro_1 = Carro("Rojo", 50)
carro_volador = CarroVolador("Blanco", 70)

print("El color de mi carro volador es: {}".format(carro_volador.color))
print("El estado inicial de mi carro volador es: {}".format(carro_volador.aceleracion))

carro_volador.vuela()
carro_volador.acelerar()
carro_volador.acelerar()


print("La velocidad actual de mi carro volador es: {}".format(carro_volador.velocidad))

"""Esto no no puede suceder, porque la herencia es sólo sobre la clase HIJA"""
#print("El estado de vuelo de mi primer carro es: {}".format(carro_1.vuela()))
