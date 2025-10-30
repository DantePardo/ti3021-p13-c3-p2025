class persona: 
    def __init__(self, rut, Nombre, apellido, fecha_nacimiento, cod_area, telefono):
        self.rut: int = rut
        self.Nombre: int = Nombre




















def __str__(self):
    return f"""
        rut:{self.rut}-{self.digito_verificador}
        Nombre Completo: {self.nombres} {self.apellidos}
        Fecha de nacimiento:{self.fecha_nacimineto}
        Numero de telefono: +{self.cod_area} {self.telefono}
    """