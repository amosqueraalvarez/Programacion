def limpiadorCadenas(cadea):
    for c in cadea:
        if c == ' ':
            cadea = cadea[1:]
        else:
            break
    for i in range(len(cadea)-1, -1, -1):
        if cadea[i] == ' ':
            cadea = cadea[:i]
        else:
            break
    return cadea


limpa = limpiadorCadenas('   pepipto monero  ')
print(limpa)


# forma simple de hacer lo mismo

def limpiadorCadenas(cadea):
    inicio = 0
    fin = len(cadea)

    while inicio < fin and cadea[inicio] == ' ':
        inicio += 1
    while fin > inicio and cadea[fin - 1] == ' ':
        fin -= 1
    return cadea[inicio:fin]
    
'''
Ejercicio en pseudocodigo
para cada índice desde el final hasta el principio:
    si es espacio, recorto
    si no, me detengo
'''