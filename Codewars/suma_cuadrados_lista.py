def square_sum(numbers):
    suma = 0
    for i in numbers:
        suma += i**2
    return suma


print(square_sum([1, 3, 4]))

# version mas simple, resultado mas comun en la comunidad


def square_sum(numbers):
    return sum(x ** 2 for x in numbers)
