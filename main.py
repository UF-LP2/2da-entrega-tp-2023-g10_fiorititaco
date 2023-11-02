import csv
from src.clases import Tiempo
from src.clases import Enfermero
from src.clases import Medico
#from src.clases import Color
from src.clases import Esintomas
from src.clases import Paciente


def triageDyV(vector: list[Paciente]):
    if len(vector) > 0:
        return mayor(vector, 1, len(vector))
    else:
        raise ValueError


def mayor(vector: list[Paciente], inicio: int, fin: int) -> Paciente:
    if len(vector) == 1:
        return vector[0]
    elif (fin-inicio) == 1:
        if vector[0].prioridad < vector[1].prioridad:
            return vector[0]
        elif vector[0].prioridad > vector[1].prioridad:
            return vector[1]
        return vector[0]

    mitad: int = int(((fin - inicio) / 2) + inicio)
    aux1: Paciente = mayor(vector, inicio, mitad)
    aux2: Paciente = mayor(vector, mitad + 1, fin)

    if aux1.prioridad < aux2.prioridad:
        return aux1
    elif aux1.prioridad > aux2.prioridad:
        return aux2
    return aux1


def main() -> None:
    Cola = []
    medico1 = Medico("Gandalf", "El Blanco")
    medico2 = Medico("Albus", "Dumbledor")
    medico3 = Medico("Qui-Gon", "Jinn")
    medico4 = Medico("Myrddin", "Wyllt")
    medico5 = Medico("Elessar", "Telcontar")

    with open("src/pacientes.csv") as file:
        reader = csv.reader(file, delimiter=',')
        next(file, None)

        for line in reader:

            paciente = Paciente(line[1], line[2], line[3], Esintomas(line[0]))
            paciente.set_prioridad(Enfermero.triage(paciente))
            Cola.append(paciente)
            aux = triageDyV(Cola)
            Cola.remove(aux)

            rebote = medico1.atender(aux)
            if Medico.cantidad > 1 and rebote:
                rebote = medico2.atender(aux)
            if Medico.cantidad > 2 and rebote:
                rebote = medico3.atender(aux)
                if rebote:
                    rebote = medico4.atender(aux)
            if Medico.cantidad > 4 and rebote:
                rebote = medico5.atender(aux)

            Tiempo.avanzar(Cola, medico1, medico2, medico3, medico4, medico5)


if __name__ == "__main__":
    main()
