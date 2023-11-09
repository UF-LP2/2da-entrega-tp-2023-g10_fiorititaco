import csv
import tkinter as tk
from src.clases import Tiempo
from src.clases import Enfermero
from src.clases import Medico
from src.clases import Paciente
from src.clases import Color


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


def imprimir(cola):
    i = 0
    print("Paciente en la cola de espera a las ", str(Tiempo.horas), ":", str(Tiempo.minutos), " :")
    if len(cola) != 0:
        while i < len(cola):
            print(i, cola[i].nombre, "\t", cola[i].apellido, "\t", cola[i].dni, "\t", cola[i].prioridad)
            i += 1
    else:
        print("No hay pacientes en espera.")


def main() -> None:
    tiempo = Tiempo()
    Cola = []
    enfermero = Enfermero()
    medico1 = Medico("Gandalf", "El Blanco")
    medico2 = Medico("Albus", "Dumbledor")
    medico3 = Medico("Qui-Gon", "Jinn")
    medico4 = Medico("Myrddin", "Wyllt")
    medico5 = Medico("Elessar", "Telcontar")
    # inicializo los objetos que van a utilizarse

    # abrimos el archivo y lo leemos linea por linea
    with open("src/pacientes.csv") as file:
        reader = csv.reader(file, delimiter=',')
        next(file, None)
        print("Paciente \t Nombre \t Apellido \t DNI \t Prioridad \n")
        for line in reader:
            paciente = Paciente(line[1], line[2], line[3], int(line[0]))
            paciente.set_prioridad(enfermero.triage(paciente))
            # a partir de del triage del enfermero sobre el paciente, al ultimo se le asigna su prioridad

            Cola.append(paciente)
            # lo agrego a la cola
            Cola = atencion(Cola, medico1, medico2, medico3, medico4, medico5)

            tiempo.avanzar(Cola, medico1, medico2, medico3, medico4, medico5)
            # avanzo el tiempo cada 5 minutos y actualizo los tiempos de cada objeto
            imprimir(Cola)

    while len(Cola) or medico5.ocupado or medico4.ocupado or medico2.ocupado or medico3.ocupado or medico1.ocupado:
        # sirve para seguir atendiendo a los pacientes incluso despues de leer todos los pacientes del archivo
        if len(Cola) != 0:
            # solo en caso de que siga habiendo pacientes en espera
            Cola = atencion(Cola, medico1, medico2, medico3, medico4, medico5)

        tiempo.avanzar(Cola, medico1, medico2, medico3, medico4, medico5)
        imprimir(Cola)
        # el avance del tiempo es inevitable, en caso de que ya no haya cola de espera, falta que los medicos terminen
        # de atender


if __name__ == "__main__":
    pass
    app = tk.Tk()
    app.geometry("2000x700")
    app.title("Triage DyV")
    app.configure(background="pink")
    titulo = tk.Label(app, text="Manejo de pacientes segun urgencia (Triage)", bg="pink", font=("Times New Roman", 30))
    titulo.pack()
    boton1 = tk.Button(app, text="Ejecutar simulacion", font=("Times new roman", 15), bg="#fcc861", fg="black",
                       width=15, height=1, command=lambda: main())
    boton1.pack()

    app.mainloop()
