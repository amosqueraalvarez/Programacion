class Instante:
    def __init__(self,segundos,minutos,horas):
        if segundos >0 and segundos <60:
            self.segundos= segundos
        else:
            print('Segundos invalidos')
        
        if minutos >0 and minutos <60:
            self.minutos= minutos
        else:
            print('Minutos invalidos')

        if horas <0 and horas <24:
            self.horas= horas
        else:
            print('Hora invalida')
        
    def instanteTiempo(self):
        if self.horas == 0 or self.horas <7:
            print('Es de madrugada')
        elif self.horas >7 or self.horas <12:
            print('Es de mañana')
        
