entero = 5
decimal = 6.7
real = 0.1e-3
complejo = 4+5j
print(real)
#"todos" queda fuera de la variable porque esta fuera de las comillas
#cadenas = "hola a "todos""

otraCadena = ' hola a "todos"'
print(type(complejo))

#enteros
#coma flotante = 64 bits
#compejos = 64 + 64
#string = variable
#bool = 8 bits

# declaracion de booleano
booleano = True
print(type(booleano))
#sale como bool en la consola

#numero hexadecimal
numHexadecimal = 0x15a
print(type(numHexadecimal))
#sale como numero int en la consola

numOctal = 0o3457
print(numOctal)
#el valor mostrado por consola es el resultado en decimal o entero etc

numBinario = 0b0011101
print(numBinario)
#lo guardo en binario y por defecto me lo muestra decimal o entero etc

numBinario2 = 0b100110
print(numBinario2)
print(~numBinario2) #invierte el resultado
#utilizo 0b seguido del numero en binario para calcular mi numero en decimal

