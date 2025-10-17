# sustituir acentos por letra

def acentos(letra):
    if letra == 'á':
        return letra.replace('á', 'a')
    if letra == 'é':
        return letra.replace('é', 'e')
    if letra == 'í':
        return letra.replace('í', 'i')
    if letra == 'ó':
        return letra.replace('ó', 'o')
    if letra == 'ú':
        return letra.replace('ú', 'u')


print(acentos('é'))

# sustituir acentos por palabra


def char_acentos(palabra):
    for char in palabra:
        if char == 'á':
            return palabra.replace('á', 'a')
        if char == 'é':
            return palabra.replace('é', 'e')
        if char == 'í':
            return palabra.replace('í', 'i')
        if char == 'ó':
            return palabra.replace('ó', 'o')
        if char == 'ú':
            return palabra.replace('ú', 'u')


print(char_acentos('frigorífico'))
