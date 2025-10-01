'''
1. Escribir o resultado das seguintes expresións:

a) ((3 + 2) % 2 – 15) / 2 * 5= 
b) (6 + (6) / 7) + 35 / 2 -8 * 5 / 4 * 2 =
c) 3 + 6 * 14 % 3 =
d) 8 + 7 * 3 + 4 * 6 /2 % 4 =
e) 27 % 4 +15 / 4 = 
f) 37 / 42  - 2 =
g) 9 * 2 / 3 * 25 * 3 =
h) (7 * 3 – 4 * 4) * 2 / 4 * 2 =

'''

a = ((3 + 2) % 2 - 15) / 2 * 5
b = (6 + (6) / 7) + 35 / 2 - 8 * 5 / 4 * 2
c = 3 + 6 * 14 % 3
d = 8 + 7 * 3 + 4 * 6 / 2 % 4
e = 27 % 4 + 15 / 4
f = 37 / 42 - 2
g = 9 * 2 / 3 * 25 * 3
h = (7 * 3 - 4 * 4) * 2 / 4 * 2

print('El resultado de a es: ' + str(a))
print('El resultado de b es: ' + str(b))
print('El resultado de c es: ' + str(c))
print('El resultado de d es: ' + str(d))
print('El resultado de e es: ' + str(e))
print('El resultado de f es: ' + str(f))
print('El resultado de g es: ' + str(g))


# 2. Cales dos seguintes nomes de variables non son válidos?

# a) Salto- mortal , salto_mortal, salto + mortal, 2salto, “salto”
# b) cantidade total, cant_total, cant5, cantidadeTotal


print('Los nombres de variables validos en a) es salto_mortal y en b) es cantidadeTotal')


# 3. Expresar, utilizando operadores aritméticos, as seguintes expresións
'''
Declaro valor a cada letra para probar los resultados asignando a cada nueva variable el
resultado de las variables del ejercicio anterior
'''

m = a
n = b
p = c
r = d
s = e
q = f
ca = g
t = 1
# el valor de i es una constante
I = (-1)**0.5

a3 = (m+n)/n
b3 = ((m+n)/p)/((p-r)/s)
c3 = (m+4)/p-q
d3 = ca*r*t/100
e3 = (m+n)/p+(q/r)
f3 = (m/n)*(p+q)
g3 = n*(1+I)**t*I/(1+I)**t-1

print(a3)
print(b3)
print(c3)
print(d3)
print(e3)
print(f3)
print(g3)


# 4. Avalia as seguintes expresións:

a4 = True and True == False
b4 = not False == True
c4 = (True and True) or False == True
d4 = (False or False) and False != True
e4 = (not (True and False)) == False
f4 = '12' + '12' == '24'
g4 = '34' + '43' == '3443'

print(a4)
print(b4)
print(c4)
print(d4)
print(e4)
print(f4)
print(g4)

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
