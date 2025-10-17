# sustituir acentos

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
