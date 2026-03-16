class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self. inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":")
        print("• Fuerza:",  self.fuerza)
        print("• Inteligencia:", self. inteligencia)
        print("• Defensa:", self.defensa)
        print("- Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self. nombre, "ha muerto")

    def daño(self, enemigo):
        return self. fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño,
              "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()


""" Herencia """


class Guerrero(Personaje):

    def __init__(self,  nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elige una opcion, 1 = 10 espada, 2 = 9 espada"))
        if opcion == 1:
            self.espada = 10
        elif opcion == 2:
            self.espada = 9
        else:
            print("La opcion no esta disponible")

    def atributos(self):
        super().atributos()
        print("Espada: ", self.espada)

    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa


class Mago(Personaje):

    def __init__(self,  nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def cambiar_arma(self):
        opcion = int(input("Elige una opcion, 1 = 12 libro, 2 = 3 libro"))
        if opcion == 1:
            self.libro = 10
        elif opcion == 2:
            self.libro = 9
        else:
            print("La opcion no esta disponible")

    def atributos(self):
        super().atributos()
        print("Libro: ", self.libro)

    def daño(self, enemigo):
        return self.fuerza*self.libro - enemigo.defensa


goku = Personaje("Goku", 20, 10, 15, 100)
guts = Guerrero("Guts", 10, 20, 20, 100, 3)
jana = Mago("Jana", 3, 15, 4, 100, 7)

goku.atacar(guts)
guts.atacar(jana)
jana.atacar(goku)

goku.atributos()
guts.atributos()
jana.atributos()


def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        print(">>> Acción de ", jugador_2.nombre, ":", sep="")
        jugador_2.atacar(jugador_1)
        turno = turno + 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")


personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

personaje_1.atributos()
personaje_2.atributos()

combate(personaje_1, personaje_2)
