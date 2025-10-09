class participante:
    def __init__(self,rut: str ,nombre: str ,edad: int ):
        self._rut: str = rut
        self._nombre: str = nombre
        self._edad: int  = edad
    
    def presentarse(self) -> str:
        return f"hola mi nombre es {self._nombre} y mi edad es {self._edad}"
    
    def __str__(self):
        return f"{self._rut} {self._nombre} {self._edad}"

participante1 = participante (
    rut = "22072951-6",
    nombre = "dante",
    edad = 19
)
print(participante1.presentarse())


