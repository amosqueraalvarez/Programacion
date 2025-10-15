# 1.Escribir unha función que reciba unha tupla de elementos e indique si se encontran ordeados de menor
# a maior ou non.


def comparacion_maxmin(listanum):
    if listanum == sorted(listanum):
        return ('Los numeros estan ordenados')
    else:
        return ('Los numeros no estan ordenados')


print(comparacion_maxmin([37, 29, 30, 40, 84, 71, 46, 53, 97, 52]))
print(comparacion_maxmin([29, 30, 37, 40, 46, 52, 53, 71, 84, 97]))

# un detalle importante!!
# si uso print dentro de la funcion no necesito hacer print al llamarla asi evito que me devuelve NONE tambien
# sort() modifica la lista original y no devuelve una lista
# sorted(nombre_lista) no modifica la lista original y devuelve una nueva
