import pytest
from src.clases import Enfermero
from src.clases import Medico
from src.clases import Tiempo
from src.clases import Paciente
from src.clases import Color


def test_prioridad():
    enfermero = Enfermero()
    paciente = Paciente("Wiliam", "Afton", "46352745", 4)
    assert enfermero.triage(paciente) == Color.NARANJA
    paciente.set_prioridad(Color.NARANJA)
    assert paciente.tiempo_espera == 10


if __name__ == '__main__':
    pytest.main()
