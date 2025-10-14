# 7. Escribir un programa que imprima por pantalla tódalas fichas de dominó, de unha por liña e sen repetir.

# Diccionario con todas las fichas de dominó
fichas_domino = {
    "ficha_1": (0, 0),
    "ficha_2": (0, 1),
    "ficha_3": (0, 2),
    "ficha_4": (0, 3),
    "ficha_5": (0, 4),
    "ficha_6": (0, 5),
    "ficha_7": (0, 6),
    "ficha_8": (1, 1),
    "ficha_9": (1, 2),
    "ficha_10": (1, 3),
    "ficha_11": (1, 4),
    "ficha_12": (1, 5),
    "ficha_13": (1, 6),
    "ficha_14": (2, 2),
    "ficha_15": (2, 3),
    "ficha_16": (2, 4),
    "ficha_17": (2, 5),
    "ficha_18": (2, 6),
    "ficha_19": (3, 3),
    "ficha_20": (3, 4),
    "ficha_21": (3, 5),
    "ficha_22": (3, 6),
    "ficha_23": (4, 4),
    "ficha_24": (4, 5),
    "ficha_25": (4, 6),
    "ficha_26": (5, 5),
    "ficha_27": (5, 6),
    "ficha_28": (6, 6)
}

# Imprimir todas las fichas
for nombre, ficha in fichas_domino.items():
    print(f"{nombre}: {ficha}")
