# boletin 6.4

curso = ['matematicas', 'fisica', 'quimica', 'historia', 'lingua']


for asignatura in range(len(curso)):
    print(curso[asignatura])
    nota_sacache = int(input('Que nota sacache: '))
    if nota_sacache < 5:
        print('tiene que repetir la asignatura ', curso[asignatura])
    elif nota_sacache >= 5:
        print('Asignatura aprobada ', curso[asignatura])
        curso.remove(curso[asignatura])
        print(curso)

# revisar que falla en la longitud de las lista porque al ir borrando disminuye su rango
