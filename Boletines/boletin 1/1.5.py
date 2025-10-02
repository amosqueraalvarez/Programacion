# 5. Avaliar as seguintes espresións, tendo en conta que as variables  teñen os valores:

i = 3
j = 0
k = 1

primerEjercicio = i + k <= j - k * 3 and k >= 2
print(primerEjercicio)

i = 3
j = 2
k = (-1)

segundoEjercicio = i == 3 or j <= 2 and k > 0
print(segundoEjercicio)

tipo = 10.0
rede = 7.5

tercerEjercicio = tipo < rede + 1.5
print(tercerEjercicio)

ano = 1993

cuartoEjercicio = ano % 400 == 0
print(cuartoEjercicio)

quintoEjercicio = 3 == 2 or 5 > 1 + 1
print(quintoEjercicio)

sextoEjercicio = 5 - 2 > 4 and not (0.5 == 1/5)
print(sextoEjercicio)

a = 2
b = 5
c = 6
d = 10

septimoEjercicio = a >= b or a >= c and a < d
print(septimoEjercicio)

# utilizo los mismos valores de las variables a,b,c,d del ejercicio anterior

octavoEjercicio = a + b < c and a + c < d or 2 * a < a + b
print(octavoEjercicio)

novenoEjercicio = not (a * b < d) and not (a * b < c) or b + c <= d
print(novenoEjercicio)
