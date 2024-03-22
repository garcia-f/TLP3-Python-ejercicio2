
# Función que elimina los valores repetidos de una lista y retorna una nueva lista sin los valores repetidos.
def quitar_repetidos(lista):
    lista_sin_repetidos = list(set(lista))
    return lista_sin_repetidos

# Función que ordena los valores distintos de una lista y cuenta cuántos hay de cada uno.
# Retorna un diccionario donde las claves son los valores distintos y los valores son las cantidades de cada uno.
def contar_y_ordenar(lista):
    conteo = {}
    for elemento in lista:
        if elemento in conteo:
            conteo[elemento] += 1
        else:
            conteo[elemento] = 1
    
    # Ordenar el diccionario por los valores (cantidad de ocurrencias) en orden ascendente.
    conteo_ordenado = dict(sorted( conteo.items() ))
    
    return conteo_ordenado

# Ejemplo de uso:
lista_ejemplo = [1, 2, 3, 3, 2, 2, 4, 6, 7, 7, 7, 1]
lista_sin_repetidos = quitar_repetidos(lista_ejemplo)
conteo_ordenado = contar_y_ordenar(lista_ejemplo)

print("Lista sin valores repetidos:", lista_sin_repetidos)
print("Valores distintos ordenados y su cantidad de ocurrencias:", conteo_ordenado)
