# ficheros

# ficheros txt

# leer y escribir fichero
"""
txt_file = open("Inicios_POO/POO_Personaje/ficheros.txt",
                "w+")  # leer y escribir, si uso ¡a¡ puedo añadir texto sin sobreescribir
txt_file.write("adrian \n mosquera \n33")
# print(txt_file.read())
# print(txt_file.read(10))  # 10 primeros caracteres
# print(txt_file.readline())  # leer linea a linea
# for line in txt_file.readlines():
# print(line)  # un listado de elementos con salto de linea

# escribir algo en un fichero

txt_file.write("\n Mi lenguaje favorito es Python")

txt_file.close()  # cerrar el fichero
"""

# otra forma de hacerlo con with sin borrar datos o usar append

with open("fichero.txt", "a") as archivo:  # se usa as para nombrar a la variable de esa manera
    archivo.write("Nueva linea de texto \n")

# ficheros .json file

import json  # para poder usar json necesito siempre importar la libreria
# crea un fichero json y lo abre es como un diccionario clave, valor
json_file = open("fichero.json", "a")

json_text = {"name": "Adrian", "surname": "Mosquera",
             "age": "33", "alias": "Cattaclish"}

# asi añado datos dentro del json, uso la funcion propia de json.dump(nombre de la variable que contiene
json.dump(json_text, json_file)
# los datos que quiero añadir, nombre del fichero donde se añaden los datos)
# puedo usar despues de los dos parametros la palabra indent= numero para tener identacion en el fichero
