En Python, no es obligatorio usar setters y getters como en Java o C++, porque Python promueve un estilo más simple. Sin embargo, sí se pueden usar cuando quieres:
	•	Validar datos al asignarlos
	•	Proteger atributos internos
	•	Controlar el acceso a ciertas variables

La herramienta para hacerlo en Python es @property.

⸻

✅ Ejemplo básico sin getters/setters (Pythonic)

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p = Persona("Ana", 30)
print(p.edad)     # acceso directo
p.edad = 31       # modificación directa

Eso funciona, pero no protege ni valida nada.

⸻

✅ Ejemplo usando getters y setters con @property

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad  # convención: "_" indica atributo "protegido"

    @property
    def edad(self):
        """Getter: permite leer el atributo"""
        return self._edad

    @edad.setter
    def edad(self, valor):
        """Setter: valida antes de asignar"""
        if valor < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = valor


p = Persona("Ana", 30)
print(p.edad)  # llama al getter
p.edad = 35    # llama al setter


⸻

🔍 ¿Qué está pasando?

Acción	Python llama…	¿Qué ocurre?
p.edad	@property edad()	Devuelve _edad
p.edad = 35	@edad.setter	Valida y asigna


⸻

✔️ Ejemplo con solo getter (solo lectura)

class Circulo:
    def __init__(self, radio):
        self._radio = radio

    @property
    def area(self):
        return 3.1416 * self._radio**2

c = Circulo(10)
print(c.area)   # funciona
c.area = 20     # ❌ error: no tiene setter


⸻

🧠 Resumen
	•	Python evita getters/setters innecesarios.
	•	Si necesitas control, usa @property, no métodos manuales tipo get_edad().
	•	Es limpio, pythonic y mantiene el mismo acceso: obj.atributo.



Aquí tienes ejemplos más avanzados de getters y setters en Python con @property, junto con cuándo conviene usarlos y cuándo evitarlos.

⸻

🔥 EJEMPLOS AVANZADOS DE GETTERS Y SETTERS EN PYTHON

⸻

1️⃣ Propiedad calculada con caché (solo getter + almacenamiento interno)

Útil cuando el cálculo es costoso y deseas memorizarlo.

class Temperaturas:
    def __init__(self, datos):
        self._datos = datos
        self._promedio = None

    @property
    def promedio(self):
        if self._promedio is None:        # se calcula 1 sola vez
            print("Calculando promedio...")
            self._promedio = sum(self._datos)/len(self._datos)
        return self._promedio

Uso:

t = Temperaturas([10, 20, 30])
print(t.promedio)   # Calcula
print(t.promedio)   # Ya no calcula


⸻

2️⃣ Setter que normaliza o transforma datos

Muy útil para limpiar inputs.

class Usuario:
    def __init__(self, correo):
        self.correo = correo

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        self._correo = valor.strip().lower()   # normaliza

Uso:

u = Usuario("  TEST@MAIL.COM  ")
print(u.correo)   # "test@mail.com"


⸻

3️⃣ Validación compleja en setters

Por ejemplo, proteger objetos de estados inválidos.

class CuentaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo.")
        self._saldo = valor


⸻

4️⃣ Setter dependiente de otros atributos

Común en modelos científicos o gráficos.

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @property
    def area(self):
        return self.base * self.altura

    @area.setter
    def area(self, nueva_area):
        # Mantener base fija y ajustar altura
        self.altura = nueva_area / self.base


⸻

5️⃣ Propiedad de solo escritura (write-only)

Útil para contraseñas.

class Usuario:
    def __init__(self):
        self._hash = None

    @property
    def password(self):
        raise AttributeError("La contraseña no se puede leer")

    @password.setter
    def password(self, valor):
        import hashlib
        self._hash = hashlib.sha256(valor.encode()).hexdigest()


⸻

6️⃣ Propiedad que dispara eventos / acciones

Sirve para logs, actualización automática, triggers, etc.

class Sensor:
    def __init__(self):
        self._valor = 0

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, v):
        print(f"Nuevo valor del sensor: {v}")
        self._valor = v


⸻

7️⃣ Getters/Setters para atributos “privados” reales con __nombre

Python aplica name mangling.

class Persona:
    def __init__(self, edad):
        self.__edad = edad

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if not (0 <= valor <= 120):
            raise ValueError("Edad inválida")
        self.__edad = valor


⸻

📌 ¿CUÁNDO CONVIENE USAR GETTERS Y SETTERS EN PYTHON?

✔️ Úsalos cuando…

✅ 1. Necesitas validar datos

Ej.: edades, límites, emails, estados de objetos, etc.

✅ 2. Quieres ejecutar código al leer o escribir

Ej.: logs, triggers, cálculos, sincronizar valores.

✅ 3. Quieres mantener un atributo privado pero con acceso controlado

Evita que usuarios rompan el estado interno del objeto.

✅ 4. Debes protegerte de estados inválidos

Especialmente en modelos financieros, médicos, científicos, etc.

✅ 5. Necesitas compatibilidad hacia atrás

Si antes se usaba obj.x = valor y ahora necesitas validarlo, puedes introducir @property sin cambiar el API.

⸻

🚫 ¿CUÁNDO NO CONVIENE** usarlos?**

❌ 1. Cuando no agregan valor

No abuses: si no necesitas validación ni lógica extra, no pongas getters/setters.

❌ 2. Cuando vuelves el código más complejo sin motivo

Código innecesariamente verboso sin beneficios.

❌ 3. Cuando el atributo es completamente interno y no será accedido externamente

Mantén simple el diseño.

❌ 4. Cuando estás imitando Java por costumbre

Python no usa el patrón “getX() / setX()” a menos que sea necesario.

⸻

🧠 CONCEPTO CLAVE

Python promueve simplicidad primero, pero ofrece @property para extender funcionalidad solo cuando realmente hace falta.

