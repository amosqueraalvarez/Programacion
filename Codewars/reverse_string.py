def solution(string):
    reverse = ''
    for i in reversed(string):  # la funcion reversed itera sobre cada indice al reves
        reverse += i
    return reverse


print(solution('hola'))

# forma simple mas comun en la comunidad


def solution(str):
    return str[::-1]
