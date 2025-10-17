
# 1. **Índices en *strings***

# Los *strings* son secuencias de caracteres, así que puedes acceder a cada carácter por su **posición (índice)**.
texto = "Python"

print(texto[0])   # P → primer carácter
print(texto[1])   # y
print(texto[-1])  # n → último carácter (índice negativo)


# Los índices en Python **empiezan en 0**.
# Los índices negativos cuentan desde el final:
texto[-1]  # → último,
texto[-2]  # → penúltimo, etc.

# 🔹 *Slicing* (rebanado)

# Permite obtener una parte del string:


print(texto[0:3])  # 'Pyt' (del índice 0 al 2)
print(texto[:4])   # 'Pyth' (inicio por defecto = 0)
print(texto[2:])   # 'thon' (hasta el final)
print(texto[::-1])  # 'nohtyP' (reversa)


# 2. **Índices en *listas***

# Las listas son **mutables**, pero el acceso por índice es igual que en strings:


numeros = [10, 20, 30, 40, 50]

print(numeros[0])   # 10
print(numeros[-2])  # 40


# También puedes modificar elementos:

numeros[1] = 25
print(numeros)  # [10, 25, 30, 40, 50]


# Y usar *slicing* igual:


print(numeros[1:4])  # [25, 30, 40]


# 🧱 3. **Índices en *tuplas***

# Las tuplas son **inmutables**, pero su acceso por índice es igual al de las listas:

coordenadas = (4, 7, 9)

print(coordenadas[0])  # 4
print(coordenadas[-1])  # 9


# No se puede hacer `coordenadas[0] = 5` → generará un error (`TypeError`).


# "Índices" en *DICCIONARIOS

# Los diccionarios **no usan índices numéricos**, sino **claves (keys)** para acceder a los valores.


persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}

print(persona["nombre"])  # Ana
print(persona["edad"])    # 25


# Puedes modificar o agregar elementos:


persona["edad"] = 26
persona["profesion"] = "Ingeniera"


# Y obtener todas las claves o valores:


print(persona.keys())    # dict_keys(['nombre', 'edad', 'ciudad', 'profesion'])
print(persona.values())  # dict_values(['Ana', 26, 'Madrid', 'Ingeniera'])


# Resumen rápido
'''
| Tipo     | Cómo se accede         | Ejemplo            | Modificable |
| -------- | ---------------------- | ------------------ | ----------- |
| `string` | `texto[índice]`        | `"hola"[1] → 'o'`  | ❌ No        |
| `list`   | `lista[índice]`        | `[1,2,3][0] → 1`   | ✅ Sí        |
| `tuple`  | `tupla[índice]`        | `(5,6,7)[-1] → 7`  | ❌ No        |
| `dict`   | `diccionario['clave']` | `{"a":1}["a"] → 1` | ✅ Sí        |
'''
