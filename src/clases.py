
import random


class medico:
    cantidad = 0
    def __init__(self,ocupado,tiempo_atencion):
        self.ocupado = False
        self.tiempo_atencion = 0
    def set_ocupado(self):
        self.ocupado = not(self.ocupado)
    def set_tiempo(self,urgencia):
        tiempo = 0
        if urgencia == rojo:
            tiempo = random.randint(30,60)
        elif urgencia == naranja:
            tiempo = random.randint(30,50)
        elif urgencia == amarillo:
            tiempo = random.randint(20, 30)
        elif urgencia == verde:
            tiempo = random.randint(15, 20)
        else:
            tiempo = random.randint(5, 15)
        self.tiempo_atencion = tiempo

class enfermero: