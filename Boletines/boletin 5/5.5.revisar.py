# 5.Escribir un programa que reciba un número n por parámetro e imprima os primeiros n números triangulares,
# xunto co seu índice. Os números triangulares obteñense mediante a suma dos números naturales dende 1 ata n.
# É dicir, si se piden os primeros 5 números triangulares, o programa debe imprimir:


# resuelto con chat gpt
def numeros_triangulares(n):
    """
    Imprime los primeros n números triangulares junto con su índice.
    """
    for i in range(1, n + 1):
        triangular = i * (i + 1) // 2  # Fórmula para el número triangular
        print(f"{i}: {triangular}")


# Ejemplo de uso
n = int(input("Introduce la cantidad de números triangulares a mostrar: "))
numeros_triangulares(n)
