# 13. Solicita o usuario un número n e debuxa un triángulo de base e altura n.
# Si o usuario teclea o número 4 o triángulo sería da seguinte forma:

# no lo hice yo, fue chat gpt
# Solicitar o número ao usuario
n = int(input("Introduce un número n: "))

# Debuxar o triángulo
for i in range(1, n + 1):
    # Imprimir espazos para aliñar o triángulo á esquerda
    print(" " * (n - i) + "*" * (2 * i - 1))
