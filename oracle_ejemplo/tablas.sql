CREATE TABLE DUEÑO(
    IdDueño INT PRIMARY KEY,
    RUT INT NOT NULL,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Edad INT,
    MascotaRegistradas VARCHAR(100)

)

CREATE TABLE MASCOTA(
    IdMascota INT PRIMARY KEY,
    Nombre VARCHAR(50),
)