# main.py

# Importar la clase desde el archivo mi_clase.py
from myCLASE import MiClase
from classBESTPRACTICESOOP import Alumno

# Crear una instancia de la clase
objeto = MiClase("Mundo")

# Llamar al método de la clase
objeto.saludar()


#instancias de la clase Alumno
registro_alumnos = {}

#ciclo para capturar los registros
for i in range(3):
    alumno = Alumno()
    alumno.set_nombre(input("Introduce el nombre del alumno: "))
    alumno.set_apellido_paterno(input("Introduce el apellido paterno: "))
    alumno.set_apellido_materno(input("Introduce el apellido materno: "))
    alumno.set_no_control(input("Introduce el No. de Control del alumno: "))
    alumno.set_semestre(int(input("Introduce el semestre: ")))

    registro_alumnos[i] = alumno

#ciclo para capturar los nombres de los registros
for i in range(3):
    print(f"Nombre: {registro_alumnos[i].get_nombre()}")

registro_alumnos[0] = alumno
