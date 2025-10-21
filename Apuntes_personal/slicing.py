'''
El slicing (del inglés slice, que significa “rebanada” o “porción”) es una técnica en programación que permite obtener 
una parte (subconjunto o sub-secuencia) de una estructura de datos secuencial, como una lista, una cadena de texto,
una tupla, o incluso un array en algunos lenguajes.

En pocas palabras: slicing = seleccionar un rango de elementos dentro de una secuencia sin necesidad de usar bucles.

'''
# ⁉️ IMPORTANTE

# CORCHETES se usan para acceso o slicing de secuencias
# PARENTESIS Agrupacion y definicion de tuplas/ llamadas a funciones

# La sintaxis general es:

# secuencia[inicio:fin:paso]

# •	inicio → índice donde comienza el corte (incluido).
# •	fin → índice donde termina el corte (excluido).
# •	paso → salto entre elementos (opcional).


# 🔹 Ejemplos básicos

# 1. Con listas:

nums = [0, 1, 2, 3, 4, 5, 6]
print(nums[2:5])      # [2, 3, 4]  (toma desde índice 2 hasta 4)
print(nums[:3])       # [0, 1, 2]  (desde el inicio hasta antes del índice 3)
print(nums[4:])       # [4, 5, 6]  (desde el índice 4 hasta el final)
print(nums[::2])      # [0, 2, 4, 6] (salta de 2 en 2)


# 2. Con cadenas:

texto = "Python"
print(texto[1:4])     # 'yth'
print(texto[::-1])    # 'nohtyP'  (inversión de la cadena)


# 3. Con tuplas (inmutables, pero se puede leer igual):

t = (10, 20, 30, 40, 50)
print(t[1:4])   # (20, 30, 40)


# ⚙️ Características importantes
# •	No modifica la secuencia original (retorna una copia).
# •	Funciona con índices negativos:

nums[-3:-1]  # los dos últimos elementos: [4, 5]


# •	Muy útil para:
# •	Copiar listas o cadenas (lista[:])
# •	Invertir secuencias (lista[::-1])
# •	Procesar datos por bloques

# DIFERENCIA ENTRE 1,2 Y 3 ARGUMENTOS

# secuencia[inicio:fin:paso]


# 1️⃣ Un solo argumento → [inicio:] o [:fin]


nums = [0, 1, 2, 3, 4, 5, 6]

print(nums[2:])   # [2, 3, 4, 5, 6]  desde el índice 2 hasta el final
print(nums[:4])   # [0, 1, 2, 3]     desde el inicio hasta antes del índice 4

# 👉 Si omites el primer valor, se asume 0.
# 👉 Si omites el segundo, se asume hasta el final.


# 2️⃣ Dos argumentos → [inicio:fin]

# Selecciona desde el índice inicio (incluido) hasta el fin (excluido).


nums = [0, 1, 2, 3, 4, 5, 6]
print(nums[2:5])  # [2, 3, 4]

# 📌 Observa: el índice 5 no se incluye.


# 3️⃣ Tres argumentos → [inicio:fin:paso]

# El tercer valor (el paso) indica cada cuántos elementos se toma uno.


nums = [0, 1, 2, 3, 4, 5, 6]
print(nums[1:6:2])   # [1, 3, 5]   → de 1 a 5, saltando de 2 en 2
print(nums[::2])     # [0, 2, 4, 6] → todos los pares (inicio y fin omitidos)


# 4️⃣ Uso de valores negativos
# •	Índices negativos cuentan desde el final hacia atrás.
# •	Pasos negativos invierten la secuencia.


nums = [0, 1, 2, 3, 4, 5, 6]

print(nums[-3:])     # [4, 5, 6]  → últimos 3 elementos
print(nums[::-1])    # [6, 5, 4, 3, 2, 1, 0] → lista invertida
print(nums[5:2:-1])  # [5, 4, 3]  → de 5 hacia 3 bajando de a 1


# 🧩 Resumen visual

# Forma	Significado	Ejemplo (nums = [0,1,2,3,4,5,6])	Resultado
# [inicio:]	Desde “inicio” hasta el final	nums[3:]	[3,4,5,6]
# [:fin]	Desde el inicio hasta antes de “fin”	nums[:4]	[0,1,2,3]
# [inicio:fin]	Desde “inicio” hasta antes de “fin”	nums[2:5]	[2,3,4]
# [inicio:fin:paso]	Desde “inicio” hasta antes de “fin”, saltando de “paso” en “paso”	nums[1:6:2]	[1,3,5]
# [::paso]	Toda la lista con salto “paso”	nums[::-1]	[6,5,4,3,2,1,0]
