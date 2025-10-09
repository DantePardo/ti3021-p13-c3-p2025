
#clases de diagrama uml
class Dueño:
    def __init__(self,nombre: str,apellido: str, edad: int, mascotaRegistrada: str):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._mascotaRegistrada = mascotaRegistrada
    @property
    def nombre(self):
        return self._nombre
    @property
    def apellido(self):
        return self._apellido
    @property
    def edad(self):
        return self._edad
    @property
    def mascotaregistrada(self):
        return self._mascotaRegistrada

class Mascota:
    def __init__(self, nombre: str, edad: int, especie: str, historialMedico: str, dueño: str):
        self.__nombre = nombre
        self.__edad = edad
        self.__especie = especie
        self._historialMedico = historialMedico
        self._dueño = dueño
    #obtenedores
    @property
    def dueño(self):
        return self._dueño
    @property
    def historialmedico(self):
        return self._historialMedico
#mascota
nuevaMascota = Mascota(
    nombre="jorge",
    edad= 10,
    especie="perro",
    historialMedico="vacunas",
    dueño="antonia"
)
nuevoDueño = Dueño(
    nombre= "antonia",
    apellido="yañez",
    edad= 18,
    mascotaRegistrada= "jorge"
)
print(nuevaMascota.historialmedico)

print(nuevoDueño.nombre)