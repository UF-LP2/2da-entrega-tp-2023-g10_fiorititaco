import csv
import PySimpleGUI as sg
from src.clases import *
import pygame


def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


def triageDyV(vector: list[Paciente]):
    # Funcion DyV que se encarga de retonar el paciente con mayor prioridad
    if len(vector) > 0:
        return mayor(vector, 1, len(vector))
    else:
        raise ValueError
    # en caso de que se pase una lista sin largo


def numcolor(color: Color):
    # Funcion que devuelve el enum convertido en int para evitar muchas condiciones innecesarias
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
    # Caso base que retorna al unico de la lista
    elif (fin-inicio) == 1:
        if numcolor(vector[inicio - 1].prioridad) < numcolor(vector[fin - 1].prioridad):
            return vector[inicio - 1]
        elif numcolor(vector[inicio - 1].prioridad) > numcolor(vector[fin - 1].prioridad):
            return vector[fin - 1]
        return vector[inicio - 1]
    # Caso base que devuelve el de mayor prioridad de una lista de 2, en caso de que tengan la misma, devuelvo al que
    # ingreso primero

    mitad: int = int(((fin - inicio) / 2) + inicio)
    aux1: Paciente = mayor(vector, inicio, mitad)
    aux2: Paciente = mayor(vector, mitad + 1, fin)
    # Caso recursivo

    if numcolor(aux1.prioridad) < numcolor(aux2.prioridad):
        return aux1
    elif numcolor(aux1.prioridad) > numcolor(aux2.prioridad):
        return aux2
    return aux1
# terminamos de comparar las prioridades de los dos mejores pacientes como en el caso base


def atencion(Cola: list[Paciente], medico1: Medico, medico2: Medico, medico3: Medico, medico4: Medico, medico5: Medico)\
        -> list[Paciente]:
    try:
        aux = triageDyV(Cola)
    except ValueError:
        return Cola

    # recibo el paciente con mayor prioridad

    # rebote: una variable booleana que sirve para ver si el paciente fue atendido o no
    rebote = medico1.atender(aux)
    if Medico.cantidad > 1 and rebote:
        rebote = medico2.atender(aux)
    if Medico.cantidad > 2 and rebote:
        rebote = medico3.atender(aux)
        if rebote:
            rebote = medico4.atender(aux)
    if Medico.cantidad > 4 and rebote:
        rebote = medico5.atender(aux)
    # las condiciones se basan en la cantidad de medicos disponibles y si fue atendido el paciente
    if not rebote:
        Cola.remove(aux)
    # solo en caso de que fue atendido el paciente, se lo borra de la lista

    return Cola


def imprimir(cola, tiempo):
    output_text = f"Pacientes en la cola de espera a las {tiempo.horas:02}:{tiempo.minutos:02}:\n"

    if len(cola) != 0:
        for i, paciente in enumerate(cola, start=1):
            output_text += f"{i}\t\t{paciente.nombre}\t\t{paciente.apellido}\t\t{paciente.dni}\t\t{paciente.prioridad.name}\n"
    else:
        output_text += "No hay pacientes en espera."

    return output_text


def main():
    tiempo = Tiempo()
    Cola = []
    enfermero = Enfermero()
    medico1 = Medico("Gandalf", "El Blanco")
    medico2 = Medico("Albus", "Dumbledore")
    medico3 = Medico("Qui-Gon", "Jinn")
    medico4 = Medico("Myrddin", "Wyllt")
    medico5 = Medico("Elessar", "Telcontar")

    layout = [
        [sg.Text("Manejo de pacientes según urgencia (Triage)", font=("Times New Roman", 20))],
        [sg.Button("Avanzar simulacion", key="-RUN-")],
        [sg.Multiline("", size=(80, 20), key="-OUTPUT-", autoscroll=True)]
    ]

    window = sg.Window("Triage DyV", layout, resizable=True, finalize=True)
    file = open("src/pacientes.csv")
    reader = csv.reader(file, delimiter=',')
    next(file, None)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        elif event == "-RUN-":
            line = next(reader, None)
            paciente = Paciente(line[1], line[2], line[3], int(line[0]))
            paciente.set_prioridad(enfermero.triage(paciente))
            Cola.append(paciente)
            Cola = atencion(Cola, medico1, medico2, medico3, medico4, medico5)
            tiempo.avanzar(Cola, medico1, medico2, medico3, medico4, medico5)
            window["-OUTPUT-"].update(imprimir(Cola, tiempo))

    window.close()
    file.close()


if __name__ == "__main__":
    song_path = "path_to_your_song.mp3"
    play_music("src/FNAF - #Five Nights at Freddy's 1 #Song By @The Living Tombstone # Animated by KoFFTLY & DivianSFM"
               " [mp3].mp3")
    main()
