# definimos clase persoa
letras = {0: 'T', 1: 'R', 2: 'W', 3: 'A', 4: 'G', 5: 'M', 6: 'Y', 7: 'F', 8: 'P', 9: 'D', 10: 'X', 11: 'B',
          12: 'N', 13: 'J', 14: 'Z', 15: 'S', 16: 'Q', 17: 'V', 18: 'H', 19: 'L', 20: 'C', 21: 'K', 22: 'E'}


class Persoa:
    def __init__(self, nome, edade, direccion, dni, nacionalidade):
        self.nome = nome
        if self.comprobarIdade(edade):
            self.edade = edade
        else:
            edade = 0
        if self.comprobobarDni(dni):
            self.dni = dni
        else:
            self.dni = '00000000X'
        self.direccion = direccion
        self.nacionalidade = nacionalidade

    def toString(self, nome):
        if type(nome) == str:
            return True
        else:
            nome = 'aaaa'
        nomeString = 'O nome e: \n' + str(nome)
        return nomeString

    def comprobarIdade(self, edade):
        if edade > 0 and edade < 150:
            return True
        else:
            edade = 0

    def comprobarDni(self, dni):
        if len(dni) == 9:
            if dni[:-1].isdigt() and dni[-1:].isalpha():
                letra = int(dni[:-1]) % 23
                for i in letras.keys():
                    if i == letra:
                        return True
            else:
                dni_x = '00000000X'
                return dni_x
        else:
            return False

    def direcNome(self, direccion):
        nomeDireccion = 'A direccion e: \n' + direccion

    def zonaNacion(self, nacionalidade):
        nomeNacionalidade = 'A nacionalidade e: \n' + nacionalidade

    def __eq__(self, outra):
        return self.dni == outra.dni
