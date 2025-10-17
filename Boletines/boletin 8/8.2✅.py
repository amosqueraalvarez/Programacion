# 2.Escribir unha función que indique si duas fichas de dominó encaixan ou non.
#  As fichas son recibidas en duas tuplas, por exemplo: (3,4) e (5,4).
#  A función devolta un booleano co resultado do encaixe.


def encajar_fichas(tpl1, tpl2):
    if tpl1[0] == tpl2[0]:
        return ('encajan')
    if tpl1[0] == tpl2[1]:
        return ('encajan')
    if tpl1[1] == tpl2[0]:
        return ('encajan')
    if tpl1[1] == tpl2[1]:
        return ('encajan')
    else:
        return ('no encajan')


print(encajar_fichas((3, 4), (2, 4)))
