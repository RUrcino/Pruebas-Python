class Persona:
    def __init__(self,nombre,apellidos,edad,ocupacion,turno,sexo):
        self.nombre = nombre
        self. apellidos = apellidos
        self.edad = edad
        self.ocupacion = ocupacion
        self.turno = turno
        self.sexo = sexo






class Alumno(Persona):
    def __init__(self,nombre,apellidos,edad,ocupacion,turno,sexo,semestre, carrera):
        super().__init__(nombre,apellidos,edad,ocupacion,turno,sexo)
        self.semestre= semestre
        self.carrera = carrera

class Profesor(Persona):
    def __init__(self,nombre,apellidos,edad,ocupacion,turno,sexo,especialidad, salario):
        super().__init__(nombre,apellidos,edad,ocupacion,turno,sexo)
        self.especialidad = especialidad
        self.salario = salario
    def __str__(self):
        return "\n----Datos del Profesor-----\nNombre> {}\nApellidos> {} \nEdad> {}\nOcupacion> {}\nTurno> {}\nSexo> {}\nEspecialidad> {}\nSalario> {}".format(
            self.nombre,self.apellidos,self.edad,self.ocupacion,self.turno,self.sexo,self.especialidad,self.salario)







