import csv
from src.clases import tiempo
from src.clases import enfermero
from src.clases import medico
from src.clases import Color
from src.clases import Esintomas
from src.clases import paciente

def main() -> None:
  with open("src/Pacientes.csv") as file:
    reader = csv.reader(file, delimiter=',')
    next(file, None)

    for line in reader:

if __name__ == "__main__":
  main()
