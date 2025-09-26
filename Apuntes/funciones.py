# funciones
'''
def crearMenu():
    print('De que figura quieres calcular el area:')
    print('[1] Triagunlo')
    print('[2 Cuadrado]')
    print('[3] Circulo')
    print('[4] Elija una opcion: ')

'''
'''
crearMenu()
crearMenu()

# creando una funcion solo tengo que llamarla despues para utilizarla

# solo se ejecuta si lo llamo como en las lineas 11 y 12


def calcularAreaTriangulo(base, altura):
    area = (base*altura)/2
    return area

# calculo es area del triangulo y me devuelve el area


areaTriangulo = calcularAreaTriangulo(4, 3)
print(areaTriangulo)
'''

'''
def crearMenu():
    print('De que figura quieres calcular el area:')
    print('[1] Rectangulo')
    print('[2] Triangulo')
    print('[3] Circulo')
    print('[4] Elija una opcion: ')


def calcularAreaRectangulo(base, altura):
    return base * altura


def calcularAreaTriangulo(base, altura):
    area = (base * altura)/2
    return area


def calculoAreaCirculo(radio):
    areaCirculo = (radio ** 2)*3.14
    return areaCirculo


def recollerParametros(opcion):
    if opcion == 1 or opcion == 2:
        base = float(input('Escribe la base: '))
        altura = float(input('Escribe la altura: '))
        return base, altura
    elif opcion == 3:
        radio = float(input('Escribe el radio: '))
        return radio


def ejercicioBoletin():
    opcion = 0
    while opcion != 4:
        crearMenu()
        opcion = (int(input('Ingrese una opcion: ')))
        if opcion > 0 and opcion < 5:
            if opcion == 1 or opcion == 2:
                base, altura = recollerParametros(opcion)
            if opcion == 1:
                area = calcularAreaRectangulo(base, altura)
                print('El area de rectangulo es: ', area)
            if opcion == 2:
                area = calcularAreaTriangulo(base, altura)
                print('El area del triangulo es: ', area)
        elif opcion == 3:
            radio = recollerParametros(opcion)
            area = calculoAreaCirculo(radio)
            print('El area del circulo es: ', area)


ejercicioBoletin()

'''

# utilizo una funcion y le paso parametros indefinidos para despues poderlo añadir


def suma(n1, n2, *outrosNumeros):
    suma = n1 + n2
    for n in outrosNumeros:
        suma = suma + n
    return suma


print(suma(3, 4, 6, 7))
