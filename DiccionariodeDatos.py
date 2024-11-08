from fpdf import FPDF

# Crear un diccionario de datos para las tablas
data_dictionary = {
    "Usuarios": [
        ("ID_Usuario", "INT", "PK", "Identificador único del usuario"),
        ("Nombre", "VARCHAR(50)", "NOT NULL", "Nombre del usuario"),
        ("Apellido", "VARCHAR(50)", "NOT NULL", "Apellido del usuario"),
        ("Identificacion", "VARCHAR(20)", "UNIQUE NOT NULL", "Número de identificación"),
        ("Telefono", "VARCHAR(15)", "NULL", "Número de teléfono"),
        ("Correo", "VARCHAR(100)", "UNIQUE NOT NULL", "Correo electrónico"),
        ("Contraseña", "VARCHAR(255)", "NOT NULL", "Contraseña encriptada"),
        ("Fecha_Nacimiento", "DATE", "NULL", "Fecha de nacimiento"),
        ("Fecha_Registro", "TIMESTAMP", "DEFAULT CURRENT_TIMESTAMP", "Fecha de registro")
    ],
    "Fisioterapeutas": [
        ("ID_Fisioterapeuta", "INT", "PK", "Identificador único del fisioterapeuta"),
        ("Nombre", "VARCHAR(50)", "NOT NULL", "Nombre del fisioterapeuta"),
        ("Apellido", "VARCHAR(50)", "NOT NULL", "Apellido del fisioterapeuta"),
        ("Identificacion", "VARCHAR(20)", "UNIQUE NOT NULL", "Número de identificación"),
        ("Telefono", "VARCHAR(15)", "NULL", "Número de teléfono"),
        ("Correo", "VARCHAR(100)", "UNIQUE NOT NULL", "Correo electrónico"),
        ("Contraseña", "VARCHAR(255)", "NOT NULL", "Contraseña encriptada"),
        ("Especialidad", "VARCHAR(50)", "NULL", "Especialidad del fisioterapeuta"),
        ("Fecha_Registro", "TIMESTAMP", "DEFAULT CURRENT_TIMESTAMP", "Fecha de registro")
    ],
    "Citas": [
        ("ID_Cita", "INT", "PK", "Identificador único de la cita"),
        ("ID_Usuario", "INT", "FK", "Referencia a Usuarios"),
        ("ID_Fisioterapeuta", "INT", "FK", "Referencia a Fisioterapeutas"),
        ("Fecha_Cita", "DATE", "NOT NULL", "Fecha de la cita"),
        ("Hora_Cita", "TIME", "NOT NULL", "Hora de la cita"),
        ("Estado_Asistencia", "ENUM('Asistió', 'No asistió')", "DEFAULT 'No asistió'", "Estado de asistencia")
    ],
    "Historial_Intervenciones": [
        ("ID_Intervencion", "INT", "PK", "Identificador único de la intervención"),
        ("ID_Cita", "INT", "FK", "Referencia a Citas"),
        ("Descripcion", "TEXT", "NOT NULL", "Descripción de la intervención"),
        ("Fecha_Registro", "TIMESTAMP", "DEFAULT CURRENT_TIMESTAMP", "Fecha de registro")
    ],
    "Tratamientos_Asignados": [
        ("ID_Tratamiento", "INT", "PK", "Identificador único del tratamiento"),
        ("ID_Usuario", "INT", "FK", "Referencia a Usuarios"),
        ("ID_Fisioterapeuta", "INT", "FK", "Referencia a Fisioterapeutas"),
        ("Descripcion_Tratamiento", "TEXT", "NOT NULL", "Descripción del tratamiento"),
        ("Fecha_Asignacion", "TIMESTAMP", "DEFAULT CURRENT_TIMESTAMP", "Fecha de asignación")
    ],
    "Notificaciones": [
        ("ID_Notificacion", "INT", "PK", "Identificador único de la notificación"),
        ("ID_Usuario", "INT", "FK", "Referencia opcional a Usuarios"),
        ("ID_Fisioterapeuta", "INT", "FK", "Referencia opcional a Fisioterapeutas"),
        ("Mensaje", "TEXT", "NOT NULL", "Contenido de la notificación"),
        ("Fecha_Envio", "TIMESTAMP", "DEFAULT CURRENT_TIMESTAMP", "Fecha y hora de envío")
    ]
}

# Crear un PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Título del PDF
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Diccionario de Datos de la Base de Datos", ln=True, align="C")
pdf.ln(10)

# Añadir tablas al PDF
for table_name, fields in data_dictionary.items():
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, f"Tabla: {table_name}", ln=True)
    pdf.set_font("Arial", size=12)
    for field in fields:
        field_name, data_type, constraint, description = field
        pdf.cell(0, 8, f"- {field_name} ({data_type}, {constraint}): {description}", ln=True)
    pdf.ln(5)

# Guardar el PDF en la carpeta actual
output_path = "diccionario_datos_base_datos.pdf"
pdf.output(output_path)

print(f"PDF guardado en {output_path}")
