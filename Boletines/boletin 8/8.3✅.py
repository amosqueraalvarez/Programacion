# 3.Escribir unha función que reciba unha tupla con nomes e para cada nome imprima unha mensaxe ‘Estimado don/dona Nome’

lista_nombres = ('Jacobo', 'Ramon', 'Julian', 'Marta', 'Roberto')


def saludos(lista_nombres):
    for nombre in lista_nombres:
        print('Estimado don/dona ', nombre)


saludos(lista_nombres)
