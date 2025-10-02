# 3.Utiliza o programa anterior para xerar unha táboa de conversión
# de temperaturas, dende 0º F ata 120º F, de 10 en 10.


temperatura = 0
t = (0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120)

for i in (t):
    conversion = (9/5 * temperatura) + 32
    temperatura += 10
    print(conversion)
