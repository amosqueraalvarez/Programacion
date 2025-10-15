# basico


nombre = 'Nicolas'
apellido = 'Schurmann'
nombre_completo = nombre + ' ' + apellido
print(nombre_completo)

# operador de formateo de strings
# una forma mas elegante de concatenar el codigo

apellido = 'Schurmann'
nombre_completo = f"{nombre} {apellido}"
print(nombre_completo)


nombre_completo = f"{nombre[0]} {2 + 5}"
print(nombre_completo)


# metodos


animal = 'chanCHito feliz'

# metodo .upper pone todo en mayusculas
print(animal.upper())

# .lower todo minusculas
print(animal.lower())

# .capitalize la primera letra de cada palabra en mayusculas
print(animal.capitalize())

# .title parecido a .capitalize pero pasa la primera a mayuscula y el resto a minuscula de cada palabra
animal = 'ChAnchitO fELIZ'
print(animal)
print(animal.title())

# strings


a = 2
a = 3
animo = 'a'

nombre_curso = 'Ultimate Python'
descripcion_curso = '''
Ultimate Python
este curso contempla todos los detalles
que necesitas aprender para enocntrar
un trabajo como programador
'''

print(descripcion_curso)

# funcion len

len(descripcion_curso)
print(len(nombre_curso))

# para acceder a un caracter especifico usamos [] dentro del parentesis de la variable.


print(nombre_curso[0])

print(nombre_curso[0:8])
print(nombre_curso[0:])
print(nombre_curso[:8])
