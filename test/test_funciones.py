import pytest
from main import triageDyV
from src.clases import Enfermero
from src.clases import Paciente
from src.clases import Color


def test_prioridad():
    enfermero = Enfermero()
    paciente = Paciente("Wiliam", "Afton", "46352745", 4)
    assert enfermero.triage(paciente) == Color.NARANJA


def testdyv():
    cola = []
    enfermero = Enfermero()
    pacienterojo = Paciente("Alan", "Lopez", "45581328", 0)
    pacientenaranja = Paciente("Fede", "Fioriti", "5555555", 2)
    pacienteazul = Paciente("Maia", "Gomez", "4444444", 16)
    pacienteverde = Paciente("lol", "ooo", "44444444", 12)

    pacientenaranja.set_prioridad(enfermero.triage(pacientenaranja))
    pacienterojo.set_prioridad(enfermero.triage(pacienterojo))
    pacienteazul.set_prioridad(enfermero.triage(pacienteazul))
    pacienteverde.set_prioridad(enfermero.triage(pacienteverde))

    cola.append(pacientenaranja)
    cola.append(pacienteazul)
    cola.append(pacienterojo)
    cola.append(pacienteverde)

    aux = triageDyV(cola)
    assert aux == pacienterojo


def test_doblerojo():
    cola = []
    enfermero = Enfermero()
    pacienterojo = Paciente("Alan", "Lopez", "45581328", 0)
    pacienterojo2 = Paciente("loco", "lol", "44444444", 0)

    pacienterojo.set_prioridad(enfermero.triage(pacienterojo))
    pacienterojo2.set_prioridad(enfermero.triage(pacienterojo2))

    cola.append(pacienterojo)

    cola.append(pacienterojo2)

    aux = triageDyV(cola)
    assert aux == pacienterojo


def testiempoespera():

    enfermero = Enfermero()

    pacienterojo = Paciente("Alan", "Lopez", "45581328", 0)
    pacientenaranja = Paciente("Fede", "Fioriti", "5555555", 2)
    pacienteamarillo = Paciente("JJ", "kk", "jjjjjj", 5)
    pacienteazul = Paciente("Maia", "Gomez", "4444444", 16)
    pacienteverde = Paciente("lol", "ooo", "44444444", 12)

    pacientenaranja.set_prioridad(enfermero.triage(pacientenaranja))
    pacienterojo.set_prioridad(enfermero.triage(pacienterojo))
    pacienteazul.set_prioridad(enfermero.triage(pacienteazul))
    pacienteverde.set_prioridad(enfermero.triage(pacienteverde))
    pacienteamarillo.set_prioridad(enfermero.triage(pacienteamarillo))

    assert pacienteamarillo.tiempo_espera == 60
    assert pacienterojo.tiempo_espera == 0
    assert pacientenaranja.tiempo_espera == 10
    assert pacienteverde.tiempo_espera == 120
    assert pacienteazul.tiempo_espera == 240


if __name__ == '__main__':
    pytest.main()
