class Curso:

    def __init__(self, nombre_curso):
        self.nombre_curso =  nombre_curso
        self.calificaciones = []

    def agrega_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)