# 2.Escribir un programa que converta un valor dado en grados Fahrenheit a grados Celsius.
# Recordade que a fórmula para a conversión é: F = 9/5 * C + 32.

temperatura = float(input('Ingrese una temperatura en grados Fahrenheit: '))
conversion = (9/5 * temperatura) + 32
print('Su temperatura en Celsius es: ' + str(conversion))
