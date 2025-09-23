#suma, resta, multiplicacion y division
#* multiplicacion **elevado a
# /division //

print(7/3) #division
print(7//3) #me da la division entera
print(7%3) #me da el resto

#100110 binario es 38 en decimal
# ~ invierte el numero en binario
# >> desplaza los bits hacia la derecha
#tenia 100110 uso >>100110= 010011 que vale 19

# << desplaza los bits hacia la izquierda
#en binario si desplazo a la derecha divido entre dos, si desplazo hacia la izquierda multiplico por 2

#operacion clasicas logicas and,or,xor
#

print(0b10 & 0b11) #and
print(0b10 | 0b11) #or
print(0b10 ^ 0b11) #xor

#operadores booleanos (and, or, not)

#and, da verdadero si los dos operados son verdaderos
#or, es verdadero si uno de los dos es verdadero
#not, si era verdadero pasa a falso y si era falso pasa a verdadero

#comparacion de valores

# == (igual)comparacion, no confundir con la asignacion =
# != distinto
# > mayor que
# < menor que
# >= mayor o igual que
# <= menor o igual que

print('4==6 ' +  str(4==6))
print('4!=6 ' +  str(4!=6))
print('4<=6 ' +  str(4<=6))
print('4>=6 ' +  str(4>=6))
print('4<6 ' +  str(4<6))
print('4>6 ' +  str(4>6))

si =  True
no = False
print(si and no)
print(si or no)
print(not si)