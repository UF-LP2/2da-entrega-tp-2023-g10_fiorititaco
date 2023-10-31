
from enum import Enum
import random


class Esintomas(Enum):
    #rojo
    Politraumatismo_grave = 0
    #naranja
    Coma = 1
    Convulsion = 2
    hemorragia_digestiva = 3
    Isquemia = 4
    #amarillo
    Cefalea_brusca = 5
    Paresia = 6
    Hipertension_arterial = 7
    Vertigo_con_afectacion_vegetativa = 8
    Sincope = 9
    Urgencia_psiquiatrica = 10
    #verde
    Otalgia = 11
    Odontalgia = 12
    Dolor_inespecifico_leve = 13
    Traumatismo = 14
    Esguince = 15
    #azul
    otro = 16


class Color(Enum):
    ROJO = 0
    NARANJA = 1
    AMARILLO = 2
    VERDE = 3
    AZUL = 4


class tiempo:
    minutos = 0
    horas = 0

    def avanzar(self):
        tiempo.minutos += 5
        if tiempo.minutos == 60:
            tiempo.minutos = 0
            tiempo.horas += 1
        if tiempo.horas == 24:
            tiempo.horas = 0
        if tiempo.horas == 23:
            medico.cantidad = 1
        elif tiempo.horas == 6:
            medico.cantidad = 2
        elif tiempo.horas == 10:
            medico.cantidad = 5
        elif tiempo.horas == 16:
            medico.cantidad = 3

#vivo:bool, respirando:bool, consciente:bool


class paciente:
    def __init__(self, nombre: str, apellido: str, dni: str, prioridad: Color, sintomas: Esintomas):
        self.prioridad = prioridad
        self.sintomas = sintomas
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni


class medico:
    cantidad = 1

    def __init__(self, ocupado: bool, tiempo_atencion: int):
        self.ocupado = False
        self.tiempo_atencion = 0

    def set_ocupado(self):
        self.ocupado = not(self.ocupado)

    def set_tiempo(self, urgencia: Color):
        tiempo = 0
        if urgencia == Color.ROJO:
            aux = random.randint(30, 60)
            tiempo = aux - (aux % 5)
        elif urgencia == Color.NARANJA:
            aux = random.randint(30, 50)
            tiempo = aux - (aux % 5)
        elif urgencia == Color.AMARILLO:
            aux = random.randint(20, 30)
            tiempo = aux - (aux % 5)
        elif urgencia == Color.VERDE:
            aux = random.randint(15, 20)
            tiempo = aux - (aux % 5)
        else:
            aux = random.randint(5, 15)
            tiempo = aux - (aux % 5)
        self.tiempo_atencion = tiempo


class enfermero:

    def triage(self, Paciente:paciente) -> Color:
        if Paciente.sintomas == 0:
            return Color.ROJO
        elif (Paciente.sintomas == Esintomas.Coma or Paciente.sintomas == Esintomas.Convulsion or
              Paciente.sintomas == Esintomas.hemorragia_digestiva or Paciente.sintomas == Esintomas.Isquemia):
            return Color.NARANJA
        elif (Paciente.sintomas == Esintomas.Cefalea_brusca or Paciente.sintomas == Esintomas.Paresia or
              Paciente.sintomas == Esintomas.Hipertension_arterial or
              Paciente.sintomas == Esintomas.Vertigo_con_afectacion_vegetativa or
              Paciente.sintomas == Esintomas.Sincope or Paciente.sintomas == Esintomas.Urgencia_psiquiatrica):
            return Color.AMARILLO
        elif (Paciente.sintomas == Esintomas.Otalgia or Paciente.sintomas == Esintomas.Odontalgia or
              Paciente.sintomas == Esintomas.Dolor_inespecifico_leve or Paciente.sintomas == Esintomas.Traumatismo or
                Paciente.sintomas == Esintomas.Esguince):
            return Color.VERDE
        return Color.AZUL

        #if(Paciente.vivo == False)
        #    raise ValueError
        #elif(Paciente.respirando == False or Paciente.consciente == False)
        #        return Color.ROJO
        #elif(aciente.consciente == False)




