texto = 'Python'

nuevo_texto = texto[1:-1]
print(nuevo_texto)


# en funcion de manera simple

def esquinas_texto(text):
    return text[1:-1]  # me quita el primer [1] y el ultimo caracter [-1]


print(esquinas_texto('Hola mundo'))
