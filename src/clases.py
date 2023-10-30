
from enum import Enum
import random

class Color(Enum):
    ROJO = 0
    NARANJA = 1
    AMARILLO = 2
    VERDE = 3
    AZUL = 4

class paciente:
    def __init__(self, prioridad:Color, vivo:bool, respirando:bool,):



class medico:
    cantidad = 0
    def __init__(self,ocupado:bool ,tiempo_atencion:int):
        self.ocupado = False
        self.tiempo_atencion = 0
    def set_ocupado(self):
        self.ocupado = not(self.ocupado)
    def set_tiempo(self,urgencia:Color):
        tiempo = 0
        if urgencia == 0:
            tiempo = random.randint(30,60)
        elif urgencia == 1:
            tiempo = random.randint(30,50)
        elif urgencia == 2:
            tiempo = random.randint(20, 30)
        elif urgencia == 3:
            tiempo = random.randint(15, 20)
        else:
            tiempo = random.randint(5, 15)
        self.tiempo_atencion = tiempo

class enfermero:
