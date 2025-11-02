usuContra = [['Manuel', 'canMorto9!'], ['Pepe', 'usuaya']]

nome = input('Escribe o nome de usuario: ')
contrasinal = input('Ingrese o contrasinal: ')
lista = []
lista.append([nome, contrasinal])

# parte1


def comprobarUsuario(usuarioContrasinal, list):
    existeUsuario = False
    for i in usuarioContrasinal:
        if i == i in list:
            existeUsuario = True
    return existeUsuario


print(comprobarUsuario(usuContra, lista))

# parte 2


def comprobarLonxitude(contrasinal):
    if len(contrasinal) > 8:
        return True
    else:
        return False


print(comprobarLonxitude(contrasinal))


def comprobar_mayusculas(contrasinal):
    for char in contrasinal:
        if char == char.upper() and char.isalpha():
            print('tiene mayusculas', char)


comprobar_mayusculas(contrasinal)


def comprobar_numero(contrasinal):
    numeros = '0123456789'
    for i in contrasinal:
        if i == i in numeros:
            print('tiene numero', i)


comprobar_numero(contrasinal)


def comprobar_caracteres(contrasinal):
    caracteres = '!"··$%&/()=?;:.'
    for elemento in contrasinal:
        if elemento == elemento in caracteres:
            print('tiene un caracter especial')


comprobar_caracteres(contrasinal)


def engadirUsuario(usuContra, nome, contrasinal):
    contrasinalCorrecto = True
    if not comprobarLonxitude(contrasinal):
        contrasinalCorrecto = False
        print('Maior de 8')
    if not comprobar_mayusculas(contrasinal):
        contrasinalCorrecto = False
        print('Non ten maiusculas')
    if not comprobar_caracteres(contrasinal):
        contrasinalCorrecto = False
        print('Ten caracteres especiales')
    if not comprobar_numero(contrasinal):
        contrasinalCorrecto = False
        print('Non ten numeros')
