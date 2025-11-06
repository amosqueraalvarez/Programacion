class Persoa:
    def __init__(self, nome, edade, dni, direccion, nacionalidade):
        self.nome = nome
        if self.comprobarEdade(edade):
            self.edade = edade
        else:
            edade = 0
        if self.comprobarDni(dni):
            self.dni = dni
        else:
            self.dni = '00000000X'
        self.direccion = direccion
        self.nacionalidade = nacionalidade

    def comprobarEdade(self, edade):
        if edade >= 0 and edade <= 150:
            return True
        else:
            return False

    def comprobarDni(self, dni):
        if len(dni) == 9:
            if dni[:-1].isdigit() and dni[-1:].isalpha():
                letrasDNI = 'TRWAGMYFPDXBNJZSQVHLCKE'
                resto = int(dni[:-1]) % 23
                if letrasDNI[resto] == dni[-1:].upper():
                    return True
                else:
                    return False
        else:
            return False

    def __str__(self):
        cadea = 'Nome: ' + self.nome + '\n'
        cadea = cadea + 'Edade: ' + str(self.edade) + '\n'
        cadea = cadea + 'DNI: ' + self.dni + '\n'
        cadea = cadea + 'Direccion: ' + self.direccion + '\n'
        cadea = cadea + 'Nacionalidade: ' + self.nacionalidade + '\n'
        return cadea

    def __eq__(self, outra):
        return self.dni == outra.dni

# comparo si una persona e mayor que outra
    def __gt__(self, outro):
        return self.edade > outro.edade

# comparo si una persona e menor que outra

    def __lt__(self, outro):
        return self.edade > outro.edade
