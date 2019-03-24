class Persona:
    def __init__(self,nombre,apellidos,edad,ocupacion,turno,sexo):
        self.nombre = nombre
        self. apellidos = apellidos
        self.edad = edad
        self.ocupacion = ocupacion
        self.turno = turno
        self.sexo = sexo


    def __setnombre(self,nombre):
        self.nombre = nombre

    def __getnombre(self):
        return self.nombre

    def __setapellidos(self, apellidos):
        self.apellidos = apellidos

    def __getapellidos(self):
        return self.apellidos


    def __setedad(self,edad):
        self.edad = edad

    def __getedad(self):
        return self.edad
    persona = property(__getnombre,__setnombre)



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




Rodrigo = Profesor("Rodrigo","Urcino",23,"Pre-Venta","M",'M',"Redes",10.500)

print("Nombre: ",Rodrigo.persona.nombre)