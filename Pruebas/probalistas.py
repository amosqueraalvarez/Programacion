# ejercicio 1:

lista_temperatura = []
for i in range(7):
    temperatura = int(input('Ingrese unha temperatura en grados Celsius: '))
    lista_temperatura.append(temperatura)

print(lista_temperatura)

# ejercicio 2:


def temperatura_media(temperaturas):
    media = sum(temperaturas)/len(temperaturas)
    return media


print('A temperatura media foi: ', temperatura_media(lista_temperatura))

# ejercicio 3:


def superior_media(temperaturas):
    numeros_dias_superior = 0
    for temperatura in temperaturas:
        if temperatura > temperatura_media(temperaturas):
            numeros_dias_superior += 1
    return numeros_dias_superior


print('A temperatura foi superior en ',
      superior_media(lista_temperatura), ' dias')

# ejercicio 4:

nome_dias = ['luns', 'martes', 'mercores',
             'xoves', 'venres', 'sabado', 'domingo']


def temp_dias(dias, lista, parametro):
    for i in range(len(lista)):
        dia = dias[i]
        temperatura = lista[i]
        if temperatura > parametro:
            print('La temnperatura en ', dia, 'es superior')
        else:
            print('La temperatura en ', dia, 'NO fue superior')


temp_dias(nome_dias, lista_temperatura, 25
          )
