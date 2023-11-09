
from enum import Enum


class Esintomas(Enum):
    # rojo
    Politraumatismo_grave = 0
    # naranja
    Coma = 1
    Convulsion = 2
    hemorragia_digestiva = 3
    Isquemia = 4
    # amarillo
    Cefalea_brusca = 5
    Paresia = 6
    Hipertension_arterial = 7
    Vertigo_con_afectacion_vegetativa = 8
    Sincope = 9
    Urgencia_psiquiatrica = 10
    # verde
    Otalgia = 11
    Odontalgia = 12
    Dolor_inespecifico_leve = 13
    Traumatismo = 14
    Esguince = 15
    # azul
    otro = 16


class Color(Enum):
    ROJO = 0
    NARANJA = 1
    AMARILLO = 2
    VERDE = 3
    AZUL = 4


class Paciente:
    def __init__(self, nombre: str, apellido: str, dni: str, sintomas: int):
        self.sintomas = Esintomas(sintomas)
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.prioridad = Color.AZUL
        self.tiempo_espera = 0

    def paso_tiempo(self):
        if self.tiempo_espera == 0:
            return
        # no puede haber tiempo negativo o prioridad mayor a rojo, no tiene sentido bajarle el tiempo
        self.tiempo_espera -= 5
        if self.tiempo_espera == 0:
            self.set_prioridad(Color.ROJO)
        elif self.tiempo_espera == 10:
            self.set_prioridad(Color.NARANJA)
        elif self.tiempo_espera == 60:
            self.set_prioridad(Color.AMARILLO)
        elif self.tiempo_espera == 120:
            self.set_prioridad(Color.VERDE)
        # En caso de que el tiempo de epsera supere al de su prioridad, se le cambia la misma

    def set_prioridad(self, prioridad: Color):
        self.prioridad = prioridad
        if prioridad == Color.NARANJA:
            self.tiempo_espera = 10
        elif prioridad == Color.AMARILLO:
            self.tiempo_espera = 60
        elif prioridad == Color.VERDE:
            self.tiempo_espera = 120
        elif prioridad == Color.AZUL:
            self.tiempo_espera = 240


class Medico:
    cantidad = 1
    # arranca en 1 porque la hora inicial es 00:00

    def __init__(self, nombre: str, apellido: str):
        self.nombre = nombre
        self.apellido = apellido
        self.ocupado = False
        self.tiempo_atencion = 0

    def set_ocupado(self):
        self.ocupado = not self.ocupado

    def atender(self, paciente: Paciente) -> bool:
        if self.ocupado:
            return True
        self.set_tiempo(paciente.prioridad)
        self.ocupado = True
        return False

    def paso_tiempo(self):
        if self.ocupado:
            self.tiempo_atencion -= 5
        if self.tiempo_atencion == 0:
            self.ocupado = False
        # solo funciona si el medico esta atendiendo

    def set_tiempo(self, urgencia: Color):
        if urgencia == Color.ROJO:
            # aux = random.randint(30, 45)
            # tiempo = aux - (aux % 5)
            tiempo = 5
        elif urgencia == Color.NARANJA:
            # aux = random.randint(20, 30)
            # tiempo = aux - (aux % 5)
            tiempo = 20
        elif urgencia == Color.AMARILLO:
            # aux = random.randint(15, 20)
            # tiempo = aux - (aux % 5)
            tiempo = 15
        elif urgencia == Color.VERDE:
            # aux = random.randint(10, 15)
            # tiempo = aux - (aux % 5)
            tiempo = 10
        else:
            # aux = random.randint(5, 1)
            # tiempo = aux - (aux % 5)
            tiempo = 5
        # dependiendo del color, se le asigna un tiempo a el tratamiento segun la gravedad del mismo
        # Ademas, para que los tiempos sean multiplos de 5, le sacamos el resto a cada numero random
        self.tiempo_atencion = tiempo


class Enfermero:

    def triage(self, paciente: Paciente) -> Color:
        # dependiendo del sintoma del paciente se le asigna una prioridad
        if paciente.sintomas == Esintomas.Politraumatismo_grave:
            return Color.ROJO
        elif (paciente.sintomas == Esintomas.Coma or paciente.sintomas == Esintomas.Convulsion or
              paciente.sintomas == Esintomas.hemorragia_digestiva or paciente.sintomas == Esintomas.Isquemia):
            return Color.NARANJA
        elif paciente.sintomas == Esintomas.otro:
            return Color.AZUL
        elif (paciente.sintomas == Esintomas.Otalgia or paciente.sintomas == Esintomas.Odontalgia or
              paciente.sintomas == Esintomas.Dolor_inespecifico_leve or paciente.sintomas == Esintomas.Traumatismo or
                paciente.sintomas == Esintomas.Esguince):
            return Color.VERDE
        return Color.AMARILLO


class Tiempo:
    minutos = 0
    horas = 0

    def avanzar(self, cola: list[Paciente], medico1, medico2, medico3, medico4, medico5):
        # actualizo el tiempo
        Tiempo.minutos += 5
        if Tiempo.minutos == 60:
            Tiempo.minutos = 0
            Tiempo.horas += 1
        if Tiempo.horas == 24:
            Tiempo.horas = 0
        if Tiempo.horas == 23:
            Medico.cantidad = 1
        elif Tiempo.horas == 6:
            Medico.cantidad = 2
        elif Tiempo.horas == 10:
            Medico.cantidad = 5
        elif Tiempo.horas == 16:
            Medico.cantidad = 3

        i = 0
        if len(cola) != 0:
            while i < len(cola):
                cola[i].paso_tiempo()
                i += 1

        medico1.paso_tiempo()
        medico2.paso_tiempo()
        medico3.paso_tiempo()
        medico4.paso_tiempo()
        medico5.paso_tiempo()

class Texto:
    def mostrar(self):
        file = open("final.txt", 'w')
        text = file.read()
        print(text)
