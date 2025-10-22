# Los bucles (for, while) repiten instrucciones varias veces.
# A veces queremos interrumpir o saltar parte del bucle según una condición.
# Ahí entran:
# 🔴 break → rompe completamente el bucle.
# 🟡 continue → salta al siguiente ciclo del bucle.
# 🔴 break — interrumpe el bucle
# Cuando Python encuentra break, sale del bucle inmediatamente, sin ejecutar lo que quede dentro.


# Ejemplo:
for numero in range(1, 6):
    if numero == 3:
        break
    print(numero)
print("Fin del bucle")
# 🖨️ Salida:
# 1
# 2
# Fin del bucle
# 📘 Explicación:
# El bucle empieza con numero = 1, luego 2.
# Cuando numero == 3, se ejecuta break.
# Python sale del bucle y pasa directamente a la línea siguiente (print("Fin del bucle")).
# ✅ Cuándo usarlo:
# Cuando quieres detener el bucle antes de que termine (por ejemplo, al encontrar un valor específico).
# 🟡 continue — salta a la siguiente iteración
# uando Python encuentra continue, no termina el bucle, sino que salta al siguiente ciclo, omitiendo el resto del código dentro del bucle para esa vuelta.


# Ejemplo:
for numero in range(1, 6):
    if numero == 3:
        continue
    print(numero)
print("Fin del bucle")
# 🖨️ Salida:
# 1
# 2
# 4
# 5
# Fin del bucle
# 📘 Explicación:
# Cuando numero == 3, se ejecuta continue.
# Python salta el print(numero) solo en esa iteración.
# Luego sigue con numero = 4 y numero = 5.
# ✅ Cuándo usarlo:
# Cuando quieres saltar un caso específico sin detener el bucle por completo.


# 🔹 Ejemplo con ambos
for i in range(1, 6):
    if i == 2:
        continue   # Salta el 2
    if i == 4:
        break      # Se detiene en el 4
    print(i)
# 🖨️ Salida:
# 1
# 3
# 📘 Explicación:
# Salta el 2 (por continue).
# Imprime 1 y 3.
# Cuando llega al 4, se ejecuta break y se termina el bucle.
