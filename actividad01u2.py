class Dueño:
    def __init__(self,nombre: str,apellido: str, edad: int, mascotaRegistrada: str):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._mascotaRegistrada = mascotaRegistrada

class Mascota:
    def __init__(self, nombre: str, edad: int, especie: str, historialMedico: str, dueño: str):
        self.__nombre = nombre
        self.__edad = edad
        self.__especie = especie
        self._historialMedico = historialMedico
        self._dueño = dueño

