import csv
from src.clases import tiempo
from src.clases import enfermero
from src.clases import medico
from src.clases import Color
from src.clases import Esintomas
from src.clases import paciente


def triageDyV(vector: list[paciente]):
  if len(vector) > 0:
    return mayor(vector, 1, len(vector))
  else:
    raise ValueError


def mayor(vector: list[paciente], inicio: int, fin: int) -> paciente:
  if len(vector) == 1:
    return vector[0]
  elif (fin-inicio) == 1:
    if vector[0].prioridad < vector[1].prioridad:
      return vector[0]
    elif vector[0].prioridad > vector[1].prioridad:
      return vector[1]
    else:
      return vector[0]

  mitad: int = int(((fin - inicio) / 2) + inicio)
  aux1: paciente = mayor(vector, inicio, mitad)
  aux2: paciente = mayor(vector, mitad + 1, fin)

  if aux1.prioridad < aux2.prioridad:
    return aux1
  elif aux1.prioridad > aux2.prioridad:
    return aux2
  else:
    return aux1


def main() -> None:
  Cola = []
  with open("src/pacientes.csv") as file:
    reader = csv.reader(file, delimiter=',')
    next(file, None)

    for line in reader:
      Paciente = paciente(line[1], line[2], line[3], Esintomas(line[0]))
      Paciente.set_prioridad(enfermero.triage(Paciente))
      Cola.append(Paciente)
      aux = triageDyV(Cola)
      Cola.remove(aux)






if __name__ == "__main__":
  main()
