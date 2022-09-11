class Persona:

    def __init__(self,nombre, apellido, email, edad): #a traves de init inicializamos nuestra instancia.SELF incluye toda la informacion sobre el objeto individual
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.edad = edad
        self.lineas_codigo = 0

    

    def cumpleaños(self): #self proque siempre nos vamos a estar refiriendo a la instancia de persona
        self.edad += 1 #va a aumentar la edad en 1
        print("Muchas felicidades!")

    
    def codificar(self, cantidad_lineas):
        self.lineas_codigo += cantidad_lineas
        
