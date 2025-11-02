# 8.Escribir unha función que reciba unha lista de tuplas (Apelido, Nome, Inicial_segundo_nome)
# e devolte unha lista de cadenas onde cada unha conteña primero o nome, logo a inicial cun punto, e logo o apelido.

datos = [['Adrian', 'Mosquera', 'A'], ['Noelia', 'Lombardia', 'F']]

nome = 0
apelido = 1
inicial = 2

cadea1 = []
for dato in datos:
    for dat in range(len(dato)):
        if dat == nome:
            cadea1.append(dato)
        if dat == inicial:
            cadea1.append(dato)
        if dat == apelido:
            cadea1.append(dato)

print(cadea1)
