# Crear un programa que sume todos los numeros anteriores a num

def sumation(num):
    suma = 0
    for i in range(num):
        suma += i  # asi consigo sumar todos los valores anterior a num// si pongo +1 tambien lo incluiria
    return suma


print(sumation(5))
