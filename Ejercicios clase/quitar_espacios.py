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
