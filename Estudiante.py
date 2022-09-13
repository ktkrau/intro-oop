from Persona import Persona

class Estudiante(Persona): #la clase a heredar es persona

    lista_estudiantes = []

    def __init__(self, nombre, apellido, email, edad, id):
        super().__init__(nombre, apellido, email, edad) #de mi clase SUPERior (persona) iniciar init y heredar estos atributos
        self.id = id #lo tengo que agregar porque este atributo no lo hereda del elemento superior (persona)
        Estudiante.lista_estudiantes.append(self)


    @classmethod
    def imprime_lista(cls):
        print("Total de estudiantes: ", len(cls.lista_estudiantes))
        for estudiante in cls.lista_estudiantes:
            print(estudiante.nombre)

#polimorfismo, consiste en que cada uno de las clases que este haciendo herencia, que tengan funciones metodos que funcionen completamente diferente
    """ def cumpleaños(self):
        self.edad += 2
        print("Sin festejo, a seguir estudiando!") #funcion solo para los que son estudiantes """

    def cumpleaños(self):
        super().cumpleaños() #Referencia a la funcion del superior y aparte ahacer algo mas
        print("a seguir estudiando")

    def que_haces(self):
        print("Estoy estudiando")

    def estudiar(self):
        print("hoy estamos estudiando python")