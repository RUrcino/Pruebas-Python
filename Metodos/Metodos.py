from Objetos.Objetos import Profesor
class MetodoProfesor:
    def __init__(self):
        pass
    def Agregar(self,nombre=None,apellidos=None,edad=None,ocupacion=None,turno=None,sexo=None,especialidad=None, salario=None):


            try:
                nombre = input("Nombre: ")
                apellidos = input("Apellidos: ")
                edad =int(input("Edad: "))
                ocupacion = input("Ocupacion: ")
                turno = input("Turno: ")
                sexo = input("Sexo: ")
                especialidad = input("Especialidad: ")
                salario= float(input("Salario: "))
                self.profesor = Profesor(nombre,apellidos,edad,ocupacion,turno,sexo,especialidad, salario)
            except ValueError:
                print("Este campo solo acepta Numeros")
                print("Revise sus datos e intente de nuevo")
                self.agregar()
            except Exception:
                print("Revise sus datos e intente de nuevo")


    def Mostrar(self):
        try:
            print(self.profesor)
        except AttributeError:
            print("No existen algun maestro para mostrar")

    def Modificar(self):

        self.Agregar()
        print("Maestro Modificado")





    def Eliminar(self):
        try:
            del(self.profesor)
            print("Profesor Eliminado")
        except AttributeError:
            print("No exite dicho profesor")
Rodrigo = MetodoProfesor()
Rodrigo.Agregar()
Rodrigo.Mostrar()
Rodrigo.Modificar()
Rodrigo.Mostrar()