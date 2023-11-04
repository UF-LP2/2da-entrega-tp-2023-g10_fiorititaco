import csv
import tkinter as tk
from src.clases import Tiempo
from src.clases import Enfermero
from src.clases import Medico
from src.clases import Paciente
from src.clases import Color


def triageDyV(vector: list[Paciente]):
    if len(vector) > 0:
        return mayor(vector, 1, len(vector))
    else:
        raise ValueError

def numcolor(color:Color):
    if color == color.ROJO:
        return 0
    elif color == color.NARANJA:
        return 1
    elif color == color.AMARILLO:
        return 2
    elif color == color.VERDE:
        return 3
    else:
        return 4
def mayor(vector: list[Paciente], inicio: int, fin: int) -> Paciente:
    if fin - inicio == 0:
        return vector[inicio - 1]
    elif (fin-inicio) == 1:
        if numcolor(vector[inicio - 1].prioridad) < numcolor(vector[fin - 1].prioridad):
            return vector[inicio - 1]
        elif numcolor(vector[inicio - 1].prioridad) > numcolor(vector[fin - 1].prioridad):
            return vector[fin - 1]
        return vector[inicio - 1]

    mitad: int = int(((fin - inicio) / 2) + inicio)
    aux1: Paciente = mayor(vector, inicio, mitad)
    aux2: Paciente = mayor(vector, mitad + 1, fin)

    if numcolor(aux1.prioridad) < numcolor(aux2.prioridad):
        return aux1
    elif numcolor(aux1.prioridad) > numcolor(aux2.prioridad):
        return aux2
    return aux1

def atencion(Cola:list[Paciente], medico1: Medico, medico2: Medico, medico3:Medico, medico4: Medico, medico5: Medico) -> list[Paciente]:
    aux = triageDyV(Cola)

    rebote = medico1.atender(aux)
    if Medico.cantidad > 1 and rebote:
        rebote = medico2.atender(aux)
    if Medico.cantidad > 2 and rebote:
        rebote = medico3.atender(aux)
        if rebote:
            rebote = medico4.atender(aux)
    if Medico.cantidad > 4 and rebote:
        rebote = medico5.atender(aux)
    if not (rebote):
        Cola.remove(aux)

    return Cola
def main() -> None:
    tiempo = Tiempo()
    Cola = []
    enfermero = Enfermero()
    medico1 = Medico("Gandalf", "El Blanco")
    medico2 = Medico("Albus", "Dumbledor")
    medico3 = Medico("Qui-Gon", "Jinn")
    medico4 = Medico("Myrddin", "Wyllt")
    medico5 = Medico("Elessar", "Telcontar")
    line = []
    j = 0
    with open("src/pacientes.csv") as file:
        reader = csv.reader(file, delimiter=',')
        next(file, None)



        for line in reader:
            paciente = Paciente(line[1], line[2], line[3], int(line[0]))
            paciente.set_prioridad(enfermero.triage(paciente))
            Cola.append(paciente)

            Cola = atencion(Cola, medico1, medico2, medico3, medico4, medico5)

            tiempo.avanzar(Cola, medico1, medico2, medico3, medico4, medico5)



    while len(Cola) or medico5.ocupado or medico4.ocupado or medico2.ocupado or medico3.ocupado or medico1.ocupado:
        if len(Cola) != 0:
            Cola = atencion(Cola, medico1, medico2, medico3, medico4, medico5)
        tiempo.avanzar(Cola, medico1, medico2, medico3, medico4, medico5)


if __name__ == "__main__":
    main()
