class participante:
    def __init__(self,rut: str ,nombre: str ,edad: int ):
        self._rut: str = rut
        self._nmbre: str = nombre
        self._edad: int  = edad
    
    def presentarse(self) -> str:
        return f"hola mi nombre es {self._nombre} y mi edad es {self._edad}"

participante1: participante = participante("22072951-6", "Dante", 19) 
print(participante1.presentarse())