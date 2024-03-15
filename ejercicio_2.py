
# dada una lista de numeros, quitar los repetidos.
listas = [ 1, 2, 3, 3, 2, 2, 4, 6, 7, 7, 7, 1 ]

def clean_list( num ):
    lista = set(num)          # un set no puede tener datos repetidos
    return list( lista )

print( clean_list( listas ) )


# dada una lista de numeros, cuantos repetidos hay.

def repetidos( num ):
    if len( num ) == len( set( num ) ):
        print('No hay repetidos')
    else:
        print('Hay repetidos')

repetidos( listas ) 