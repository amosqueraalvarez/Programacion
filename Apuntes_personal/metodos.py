'''
1. Cadenas de texto(str)
• .upper() → Convierte todo a MAYÚSCULAS
• .lower() → Convierte todo a minúsculas
• .capitalize() → Primera letra en mayúscula
• .title() → Primera letra de cada palabra en mayúscula
• .strip() → Elimina espacios en los extremos
• .replace('a', 'b') → Sustituye un texto por otro
• .find('x') → Devuelve la posición donde aparece algo(o - 1)
• .split(',') → Divide el texto en partes(lista)
• .join(lista) → Une una lista en un string con un separador
• .startswith('x') → Comprueba si empieza con 'x'
• .endswith('y') → Comprueba si termina con 'y'
• .isdigit() → True si son solo números
• .isalpha() → True si son solo letras
• .isdecimal() → True si todos los caracteres son decimales

'''
texto = "  hola mundo  "

print(texto.upper())        # '  HOLA MUNDO  '
print(texto.lower())        # '  hola mundo  '
print(texto.capitalize())   # '  hola mundo  ' → solo primera letra del string
print(texto.title())        # '  Hola Mundo  '
print(texto.strip())        # 'hola mundo' → quita espacios de los extremos
print(texto.replace('a', 'o'))  # '  holo mundo  '
print(texto.find('m'))      # 7 → posición donde aparece 'm'
print(texto.split())        # ['hola', 'mundo'] → divide por espacios
print('-'.join(['uno', 'dos']))  # 'uno-dos'
print(texto.startswith('h'))  # False → porque empieza con espacio
print(texto.strip().startswith('h'))  # True
print("123".isdigit())      # True
print("abc".isalpha())      # True
print("abc123".isalnum())   # True


'''
2. Listas(list)
• .append(x) → Agrega un elemento al final
• .insert(i, x) → Inserta en una posición
• .remove(x) → Elimina la primera aparición de un valor
• .pop(i) → Elimina y devuelve el elemento
• .sort() → Ordena la lista en el mismo lugar(modifica la original) se puede combinar con reverse para invertir el orden
• .reverse() → Invierte el orden
• .index(x) → Devuelve posición de un valor
• .count(x) → Cuenta cuántas veces aparece
• .copy() → Copia la lista
• .clear() → Vacía la lista
. sorted(listanum) devuelve una lista nueva ordenada sin modificar la original
'''

nums = [3, 1, 2]

nums.append(4)         # [3, 1, 2, 4]
nums.insert(1, 99)     # [3, 99, 1, 2, 4]
nums.remove(99)        # [3, 1, 2, 4]
nums.pop()             # [3, 1, 2] → elimina el último
nums.sort()            # [1, 2, 3]
nums.reverse()         # [3, 2, 1]
print(nums.index(2))   # 1
print(nums.count(3))   # 1
nums2 = nums.copy()    # copia independiente
nums.clear()           # []

lista = [4, 2, 5]
print(sorted(lista))   # [2, 4, 5] (NO modifica la original)

'''
3. Tuplas(tuple)
• .count(x) → Cuenta cuántas veces aparece un valor
• .index(x) → Devuelve la posición de un valor
'''

t = (10, 20, 10, 30)

print(t.count(10))     # 2
print(t.index(20))     # 1

'''
4. Diccionarios(dict)
• .get(clave, defecto) → Obtiene el valor de forma segura
• .keys() → Devuelve todas las claves
• .values() → Devuelve todos los valores
• .items() → Devuelve lista de pares(clave, valor)
• .update({}) → Actualiza o agrega pares
• .pop(clave) → Elimina y devuelve el valor de una clave
• .clear() → Vacía el diccionario


5. Conjuntos(set)
• .add(x) → Agrega un elemento
.remove(x) → Elimina un elemento(error si no existe)
• .discard(x) → Elimina un elemento(sin error)
• .pop() → Elimina un elemento aleatorio
• .union(otro) → Une conjuntos
• .intersection(otro) → Devuelve los comunes
• .difference(otro) → Elementos que están en uno pero no en otro
• .symmetric_difference(otro) → Elementos no compartidos


6. Archivos(file)
• .read() → Lee todo el contenido
• .readline() → Lee una línea
• .readlines() → Lista con todas las líneas
• .write('texto') → Escribe en el archivo
• .writelines(lista) → Escribe varias líneas
• .close() → Cierra el archivo


7. Números(int, float)
• abs(x) → Valor absoluto
• round(x, n) → Redondea
• pow(x, y) → Potencia
• divmod(a, b) → Devuelve(cociente, resto)
'''

print(abs(-5))        # 5
print(round(3.1416, 2))  # 3.14
print(pow(2, 3))      # 8
print(divmod(9, 2))   # (4, 1)


'''
8. Funciones y Clases
• Funciones definidas con def no tienen métodos internos, pero sí atributos.
• Clases pueden definir métodos propios.
• Métodos especiales(dunder methods): __init__, __str__, __len__, __getitem__, __setitem__,
'''
