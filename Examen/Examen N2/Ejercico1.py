"""clase llamada Persona"""
class Persona:

    """atributos deben ser nombre,
    edad, saldo y de nacionalidad peruana"""
    def __init__(self, nombre, edad, saldo, nacionalidad="peruana"):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        self.nacionalidad = nacionalidad

    """un método para solicitar su nombre y edad."""
    def solicitar_nombre_edad(self):
        try:
            self.nombre = input("Ingresa tu nombre: ")
            self.edad = int(input("Ingresa tu edad: "))

        except ValueError:
            print("Dato incorrecto (número entero).")

    """Metodo de cumpleaños"""
    def cumple(self):
        self.edad += 1

"""Crear una función que retorne solamente la fecha, hora y minuto"""
def obtener_fecha_hora():
    import datetime
    tiempo = datetime.datetime.now()
    return tiempo.strftime("%Y-%m-%d %H:%M")

"""Crear la instancia de la clase Persona"""
persona1 = Persona(nombre="", edad=0, saldo=0, nacionalidad="peruana")
persona2 = Persona(nombre="", edad=0, saldo=0, nacionalidad="peruana")

"""Solicitar nombre y edad para ambas personas"""
persona1.solicitar_nombre_edad()
persona2.solicitar_nombre_edad()

""""y usar su método cumpleaños para
incrementar su edad (mínimo instanciar la clase 2 veces,"""
persona1.cumple()
persona1.cumple()
persona2.cumple()
persona2.cumple()

"""Mostrar la edad actualizada"""
print(f"{persona1.nombre} tiene {persona1.edad} años.")
print(f"{persona2.nombre} tiene {persona2.edad} años.")

"""Mostrar la fecha y hora de registro"""
print(f"Fecha y hora de registro: {obtener_fecha_hora()}")