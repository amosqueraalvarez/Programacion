#sentencias condicionales 

#ejemplo esquema apuntes

temp = 24
porcNubes = 30
precipitacion = 2

''' todo esto es una expresion logica
'''
if temp >16 and porcNubes < 40 and precipitacion == 0:
    print('collo toalla')
    print('poño bañador')
    print('vou a praia')
# si se cumple esta condicion de if devuelve lo que esta a continuacion
else:
    print('collo chuvasqueiro')
    print('vou a casa de un amigo')
# si no se cumplio me va a devolver el else


print('volto a casa')
print('ceo')
print('cama')



#otra posibilidad simple

if precipitacion > 0:
    print('collo paraguas')

# se imprime el if si se cumple, si no se ignora y continua el programa

print('volto a casa')
print('ceo')
print('cama')

#encadenadas feas

if temp < 0:
    print('vai un frio de carallo')
else:
    if temp > 0 and temp < 10:
        print('vai moito frio')
    else:
        if temp>10 and temp> 20:
            print('vai fresco')
        else:
            if temp >20 and temp<30:
                print('isto templase')
            else:
                print('vai un calor de carallo')


# mismo que arriba con elif

if temp < 0:
    print('vai un frio de carallo')
elif temp > 0 and temp < 10:
    print('vai moito frio')
elif temp>10 and temp> 20:
    print('vai fresco')
elif temp >20 and temp<30:
    print('isto templase')
else:
    print('vai un calor de carallo')


#otro ejemplo

if temp >15:
    valoracionAtmosferica = 'calor'
else:
    valoracionAtmosferica = 'frio'

#operador ternario

valoracionAtmosferica = 'calor' if temp>15 else 'frio'

