# 1. for i in range(len(variable))
# Uso típico: cuando variable es una lista, cadena o colección y necesitas los índices.
# len(variable) devuelve cuántos elementos tiene la variable.
# range(len(variable)) crea una secuencia de números desde 0 hasta len(variable) - 1.

# Ejemplo:
nombres = ["Ana", "Luis", "María"]

for i in range(len(nombres)):
    print(i, nombres[i])
# Salida:
# 0 Ana
# 1 Luis
# 2 María
# Cuándo usarlo: cuando necesitas tanto el índice (i) como el elemento (nombres[i]).


# for i in range(variable)
# Aquí variable debe ser un número entero.
# range(variable) genera una secuencia de enteros desde 0 hasta variable - 1.
# Ejemplo:
for i in range(5):
    print(i)
# Salida:
0
1
2
3
4
# Cuándo usarlo: cuando sabes cuántas veces quieres repetir algo (un bucle con contador).
# Si variable no es un número, dará error:
# for i in range("hola"):  # ❌ TypeError
#    ...


# for i in variable
# Aquí no se usa range().
# El bucle itera directamente sobre los elementos de variable.
# variable debe ser iterable (lista, tupla, string, conjunto, diccionario, etc.).
# Ejemplo:
nombres = ["Ana", "Luis", "María"]

for i in nombres:
    print(i)
# Salida:
# Ana
# Luis
# María
# Cuándo usarlo: cuando solo necesitas los elementos, no los índices.
# Funciona con listas, cadenas, etc.


# enumerate() es una forma elegante y más “pythónica” de recorrer una colección obteniendo el índice y el valor a la vez, sin usar range(len(...)).
# Sintaxis básica
for indice, valor in enumerate(variable):
    #    ...
    # indice → la posición del elemento (0, 1, 2, …)
    # valor → el elemento en esa posición
    # Ejemplo
numeros = [10, 20, 30]

for i, n in enumerate(numeros):
    print("Índice:", i, "→ Valor:", n)
# Salida:
# Índice: 0 → Valor: 10
# Índice: 1 → Valor: 20
# Índice: 2 → Valor: 30
#  Es equivalente a:
for i in range(len(numeros)):
    print("Índice:", i, "→ Valor:", numeros[i])
# …pero más limpio y legible.
# Ejemplo con cadenas
texto = "Hola"
for i, letra in enumerate(texto):
    print(i, letra)
# Salida:
# 0 H
# 1 o
# 2 l
# 3 a
# Consejo
# Puedes hacer que el índice empiece desde otro número:
for i, n in enumerate(numeros, start=1):
    print(i, n)
# Salida:
# 1 10
# 2 20
# 3 30
