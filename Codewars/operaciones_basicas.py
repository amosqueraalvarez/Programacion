# funcion que pide un operador +,-,*,/ y valor1 y valor2 para realizar el calculo


def basic_op(operator, value1, value2):
    if operator == '+':
        suma = value1 + value2
        return suma
    if operator == '-':
        resta = value1 - value2
        return resta
    if operator == '*':
        multiplicacion = value1*value2
        return multiplicacion
    if operator == '/':
        # podia ahorrarme crear la variable y simpplemente hacer return con la operacion
        division = value1/value2
        return division  # ej. explicacion anterior= value1/value2


print(basic_op('-', 9, 5))
print(basic_op('+', 9, 5))
print(basic_op('*', 9, 5))
print(basic_op('/', 9, 5))
