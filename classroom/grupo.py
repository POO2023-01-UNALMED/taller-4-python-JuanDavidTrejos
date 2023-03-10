from classroom.asignatura import Asignatura

class Grupo:
    
    grado = 'Grado 12'

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        
        #if asignaturas is None:
        #    self._asignaturas = []
        #if estudiantes is None:
        #    self.listadoAlumnos = []
        

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:    
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
    
    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}"

    #@ classmethod
    #def asignarNombre(cls, nombre="Grado 10"):
    #    cls.grado = nombre

    #@ classmethod
    #def asignarNombre(cls, nombre="Grado 6"):
    #    cls.grado = nombre

    #@ classmethod
    #def asignarNombre(cls, nombre="Grado 4"):
    #    cls.grado = nombre
