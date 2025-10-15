# 10. Deseña un programa que calcule o área dun rectángulo cuxa base e altura pides por teclado.
# Asegúrate que estes valores sexan positivos, para eso valida os datos.

elegir = int(input('''Elija una opcion entre 1 y 3 donde:
1] es el resultado con condicionales
[2] es el resultado con un bucle while
[3] es el resultado combinada de de un bucle while con un condicional dentro de una funcion
'''))

if elegir == 1:
    # resultado con condicionales
    base = int(input('Ingrese la base del triangulo: '))
    altura = int(input('Ingrese la altura del triangulo: '))

    if base < 0:
        print('La base no puede ser negativa')
        base = int(input('Ingrese la base del triangulo: '))
    if altura < 0:
        print('La altura no puede ser negativa')
        altura = int(input('Ingrese la altura del triangulo: '))
    calculo_area = (base*altura)/2

    resultado = calculo_area
    print('El area del triangulo es: ', resultado, 'opcion 1.')
if elegir == 2:
    # prueba con bucles

    base = int(input('Ingrese la base del triangulo: '))
    altura = int(input('Ingrese la altura del triangulo: '))

    while base < 0:
        base = int(input('Ingrese la base del triangulo: '))
    while altura < 0:
        altura = int(input('Ingrese la altura del triangulo: '))

    calculo_area = (base*altura)/2
    resultado = calculo_area
    print('El area del triangulo es: ', resultado, 'opcion 2.')

if elegir == 3:
    # prueba con funciones
    base = int(input('Ingrese la base del triangulo: '))
    altura = int(input('Ingrese la altura del triangulo: '))

    def area_triangulo(base, altura):
        while base < 0:
            base = int(input('Ingrese la base del triangulo: '))
        while altura < 0:
            altura = int(input('Ingrese la altura del triangulo: '))
        calculo_area = (base * altura)/2
        return calculo_area

    resultado = area_triangulo(base, altura)
    print('El area del triangulo es: ', resultado, 'opcion 3.')
