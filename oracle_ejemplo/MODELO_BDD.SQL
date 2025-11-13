/*
DUEÑO
IdDueño PRIMARY KEY,
RUT int not null,
Nombre varchar(50),
Apellido varchar(50),
MascotaRegistrada,
Edad int


MASCOTA
IdMascota PRIMARY KEY,
Nombre varchar(50),
Especie varchar(30) not null,
Historial medico varchar(40) not null,
FOREIGN KEY (IdDeuño) REFERENECE (DUEÑO)

PERRO
HistorialVacuna varchar (100)


Gato
EstaEsterilizado BOOLEAN,


AVE
ControlDeVuelo varchar(50),
Jaula varchar(30)
