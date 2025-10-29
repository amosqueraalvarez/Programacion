# Escribe un programa en Python que pida al usuario un número entero positivo y muestre todos los números primos comprendidos entre 0 y ese número (inclusive).

# Pedir un número al usuario
numero = int(input("Introduce un número entero positivo: "))

# Comprobar que el número sea mayor que 1
if numero < 2:
    print("No hay números primos menores que 2.")
else:
    print(f"Números primos entre 0 y {numero}:")

    # Recorrer todos los números desde 2 hasta el número introducido
    for n in range(2, numero + 1):
        es_primo = True  # Suponemos que es primo

        # Comprobamos si tiene algún divisor distinto de 1 y de sí mismo
        for i in range(2, n):
            if n % i == 0:
                es_primo = False
                break  # Ya sabemos que no es primo, salimos del bucle

        if es_primo:
            print(n, end=" ")


# Escribe un programa en Python que pida al usuario una frase y muestre cuántas veces aparece cada palabra.
# Usa un diccionario, donde las claves sean las palabras y los valores el número de veces que aparece cada una.

# Pedir la frase al usuario
frase = input("Introduce una frase: ")

# Convertimos todo a minúsculas para no diferenciar 'Hola' de 'hola'
frase = frase.lower()

# Dividir la frase en palabras usando split()
palabras = frase.split()

# Crear un diccionario vacío
contador = {}

# Recorrer cada palabra y contar cuántas veces aparece
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

# Mostrar el resultado
print("\nConteo de palabras:")
for palabra, veces in contador.items():
    print(f"{palabra}: {veces}")


# Pide tres números enteros al usuario y muestra cuál es el mayor.
# No uses funciones predefinidas como max().

# Pedimos tres números enteros al usuario
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

# Comparamos los números con condicionales
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

# Mostramos el resultado
print("El número mayor es:", mayor)


# Pide un número entero n y calcula la suma de todos los números pares desde 1 hasta n (inclusive).

# Pedir el número al usuario
n = int(input("Introduce un número entero positivo: "))

# Inicializar la variable suma
suma = 0

# Recorrer los números desde 1 hasta n
for i in range(1, n + 1):
    if i % 2 == 0:       # Comprobar si es par
        suma += i        # Sumarlo si lo es

# Mostrar el resultado
print("La suma de los números pares entre 1 y", n, "es:", suma)


# o con funciones y mas facil

def suma_pares(n):
    suma = 0
    for i in range(2, n + 1, 2):
        suma += i
    return suma


# Programa principal
numero = int(input("Introduce un número entero positivo: "))
print("La suma de los números pares entre 1 y",
      numero, "es:", suma_pares(numero))

'''
Pide al usuario 5 nombres y guárdalos en una lista.
Después, muestra:
Los nombres ordenados alfabéticamente
El nombre más largo
El número total de caracteres entre todos los nombres
'''

# Crear una lista vacía
nombres = []

# Pedir 5 nombres al usuario
for i in range(5):
    nombre = input(f"Introduce el nombre {i + 1}: ")
    nombres.append(nombre)

# Mostrar los nombres ordenados alfabéticamente
print("\nNombres ordenados alfabéticamente:")
for n in sorted(nombres):
    print(n)

# Encontrar el nombre más largo
nombre_mas_largo = max(nombres, key=len)

# Calcular el total de caracteres
total_caracteres = sum(len(n) for n in nombres)

# Mostrar resultados
print("\nEl nombre más largo es:", nombre_mas_largo)
print("Número total de caracteres:", total_caracteres)

'''
 Ejercicio 13: Media de una lista
Enunciado:
Crea una función que reciba una lista de números y devuelva su media.
Haz que el programa pida 5 números y use la función para mostrar el promedio.
'''

# Definimos la función


def calcular_media(lista_numeros):
    """Devuelve la media de una lista de números."""
    if len(lista_numeros) == 0:
        return 0  # Evita división entre cero
    return sum(lista_numeros) / len(lista_numeros)


# Programa principal
numeros = []

# Pedir 5 números al usuario
for i in range(5):
    num = float(input(f"Introduce el número {i + 1}: "))
    numeros.append(num)

# Llamar a la función y mostrar el resultado
media = calcular_media(numeros)
print("\nLa media de los números introducidos es:", media)
