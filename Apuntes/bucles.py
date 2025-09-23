#bucles
'''
temp= 13
while temp<100:
    print(' medir temperatura do sensor')
    temp = temp +10
    print(temp)
    print('Resistencia calefactora acendida')
    print('outra operacion')

contador= 0
while contador<20:
    print(contador)
    contador = contador + 1
    
'''
# break y continue
contador= 0
while True:
    contador= contador +1
    if contador>20:
        break
    if contador%3 != 0:
        continue
    print(contador)



