lista = ['!', '@', '#', '$', '%', '*', '_']
lista2 = '!@#¢$*_'
contraseña = 'uhai#ihiu@a'


def elegir(lista, contra):
    for char in contra:
        if char == char in lista:
            return True


print(elegir(lista2, contraseña))
