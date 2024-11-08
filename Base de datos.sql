CREATE DATABASE SistemaFisioterapia;
USE SistemaFisioterapia;

-- Tabla de Usuarios
CREATE TABLE Usuarios (
    ID_Usuario INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Identificacion VARCHAR(20) UNIQUE NOT NULL,
    Telefono VARCHAR(15),
    Correo VARCHAR(100) UNIQUE NOT NULL,
    Contraseña VARCHAR(255) NOT NULL,
    Fecha_Nacimiento DATE,
    Fecha_Registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Fisioterapeutas
CREATE TABLE Fisioterapeutas (
    ID_Fisioterapeuta INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Identificacion VARCHAR(20) UNIQUE NOT NULL,
    Telefono VARCHAR(15),
    Correo VARCHAR(100) UNIQUE NOT NULL,
    Contraseña VARCHAR(255) NOT NULL,
    Especialidad VARCHAR(50),
    Fecha_Registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Citas
CREATE TABLE Citas (
    ID_Cita INT AUTO_INCREMENT PRIMARY KEY,
    ID_Usuario INT,
    ID_Fisioterapeuta INT,
    Fecha_Cita DATE NOT NULL,
    Hora_Cita TIME NOT NULL,
    Estado_Asistencia ENUM('Asistió', 'No asistió') DEFAULT 'No asistió',
    FOREIGN KEY (ID_Usuario) REFERENCES Usuarios(ID_Usuario),
    FOREIGN KEY (ID_Fisioterapeuta) REFERENCES Fisioterapeutas(ID_Fisioterapeuta)
);

-- Tabla de Historial de Intervenciones
CREATE TABLE Historial_Intervenciones (
    ID_Intervencion INT AUTO_INCREMENT PRIMARY KEY,
    ID_Cita INT,
    Descripcion TEXT NOT NULL,
    Fecha_Registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ID_Cita) REFERENCES Citas(ID_Cita)
);

-- Tabla de Tratamientos Asignados
CREATE TABLE Tratamientos_Asignados (
    ID_Tratamiento INT AUTO_INCREMENT PRIMARY KEY,
    ID_Usuario INT,
    ID_Fisioterapeuta INT,
    Descripcion_Tratamiento TEXT NOT NULL,
    Fecha_Asignacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ID_Usuario) REFERENCES Usuarios(ID_Usuario),
    FOREIGN KEY (ID_Fisioterapeuta) REFERENCES Fisioterapeutas(ID_Fisioterapeuta)
);

-- Tabla de Notificaciones
CREATE TABLE Notificaciones (
    ID_Notificacion INT AUTO_INCREMENT PRIMARY KEY,
    ID_Usuario INT DEFAULT NULL,
    ID_Fisioterapeuta INT DEFAULT NULL,
    Mensaje TEXT NOT NULL,
    Fecha_Envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ID_Usuario) REFERENCES Usuarios(ID_Usuario),
    FOREIGN KEY (ID_Fisioterapeuta) REFERENCES Fisioterapeutas(ID_Fisioterapeuta)
);
