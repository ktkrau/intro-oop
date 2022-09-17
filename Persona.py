from Curso import Curso

class Persona:

    pais = "Chile" #atributo de toda la clase
    lista_personas = [] #Lista de todas las instancias de personas
    total_lineas_codigo = 0 #Total de lineas de codigo de TODAS las instancias de personas

    def __init__(self,nombre, apellido, email, edad): #a traves de init inicializamos nuestra instancia.SELF incluye toda la informacion sobre el objeto individual
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.edad = edad
        self.lineas_codigo = 0
        Persona.lista_personas.append(self)#estoy agregando la instancia (juana, elena, pablo)a la lista
        self.curso = Curso("Bootcamp Python")#definiendo una nueva instancia de la clase curso
    

    def cumpleaños(self): #self proque siempre nos vamos a estar refiriendo a la instancia de persona
        self.edad += 1 #va a aumentar la edad en 1
        print("Muchas felicidades!")
        if Persona.mayoria_edad(self.edad):
            print("Eres mayor de edad!")

    
    def codificar(self, cantidad_lineas):
        self.lineas_codigo += cantidad_lineas
        Persona.total_lineas_codigo += cantidad_lineas
        if Persona.experto(self.lineas_codigo):
            print("Eres un/a experto/a codificando,", self.nombre)
        
#si quiero hacer una funcion que no es de una persona en especifico tengo que hacerlo con toda la clase

    @classmethod #la funcion que voy a realizar corresponde a toda mi clase
    def imprime_lista(cls): #cls en vez de self, corresponde a todo(mi clase completa) 
        print("Total de personas:", len(cls.lista_personas))
        for persona in cls.lista_personas: # cls = Persona
            print(persona.nombre) #VARIABLE persona NO LA CLASE



    
    @staticmethod #quiero que si cumpleaños y tiene mayoria de edad imprima algo
    def mayoria_edad(edad):
        if edad >=18:
            return True
        else:
            return False

    @staticmethod
    def experto(lineas): # recibo un numero
        if lineas > 100: #si el numero es mayor a 100 entonces es experto
            return True
        else:
            return False # no es experto aun
            # no se a quien corresponde las lines de codigo, solo recibo un numero, luego lo comparo con el metodo codificar()

    def tomar_cerveza(self): #self = juana (linea38)
        if Persona.mayoria_edad(self.edad): #le envío la edad de juana (18)
            print("Aquí va tu cerveza", self.nombre)
        else: 
            print("Lo siento no puedes tomar", self.nombre )

    def que_haces(self):
        raise NotImplementedError #cuando a la persona le pregunten que_haces no va a decir nada
#pero podriamos implementarla en estudiantes
#NotImplementedError para hacer el metodo sin que funcione, para hacer la comparacion de polimorfismo