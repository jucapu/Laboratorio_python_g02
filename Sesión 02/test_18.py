
"""Listas en  Python"""

"""Listas (del): Eliminar un valor indicando el índice del valor en la lista"""

paises = []
paises.append("Perú")
paises.append("Brasil")
paises.append("Canadá")
paises.append("Chile")
paises.append("España")
paises.append("Francia")

print("Los valores de mi lista son: {}".format(paises))

del paises[2]
print(paises)
