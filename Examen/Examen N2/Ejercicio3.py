def ingresar_datos():
    try:
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))
        return num1, num2
    except ValueError:
        print("Error: Ingresa un numero valido.")
        return ingresar_datos()

def division(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
        return None

def eval_suma(datos):
    try:
        suma = sum(datos)
        return suma
    except TypeError:
        print("Error: Los datos ingresados no son válidos para la suma.")
        return None

def obtener_indice(lista, indice):
    try:
        dato = lista[indice]
        return dato
    except IndexError:
        print("Error: El índice especificado no existe en la lista.")
        return None

def main():
    dato1, dato2 = ingresar_datos()
    resultado_division = division(dato1, dato2)
    if resultado_division is not None:
        print(f"Resultado de la división: {resultado_division}")

    n = int(input("Ingresa la cantidad de datos para la lista: "))
    datos_lista = []
    for _ in range(n):
        dato = float(input("Ingresa un dato para la lista: "))
        datos_lista.append(dato)

    suma_total = eval_suma(datos_lista)
    if suma_total is not None:
        print(f"Suma de los datos: {suma_total}")

    indice = int(input("Ingresa un índice para obtener un dato de la lista: "))
    dato_obtenido = obtener_indice(datos_lista, indice)
    if dato_obtenido is not None:
        print(f"Dato en el índice {indice}: {dato_obtenido}")

if __name__ == "__main__":
    main()
