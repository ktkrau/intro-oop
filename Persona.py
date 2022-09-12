class Persona:

    pais = "Chile" #atributo de toda la clase
    lista_personas = [] #Lista de todas las instancias de personas
    total_lineas_codigo = 0 #Total de lineas de codigo de TODOS

    def __init__(self,nombre, apellido, email, edad): #a traves de init inicializamos nuestra instancia.SELF incluye toda la informacion sobre el objeto individual
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.edad = edad
        self.lineas_codigo = 0
        Persona.lista_personas.append(self)#estoy agregando la instancia (juana, elena, pablo)a la lista

    

    def cumpleaños(self): #self proque siempre nos vamos a estar refiriendo a la instancia de persona
        self.edad += 1 #va a aumentar la edad en 1
        print("Muchas felicidades!")

    
    def codificar(self, cantidad_lineas):
        self.lineas_codigo += cantidad_lineas
        Persona.total_lineas_codigo += cantidad_lineas
        
#si quiero hacer una funcion que no es de una persona en especifico tengo que hacerlo con toda la clase

    @classmethod #la funcion que voy a realizar corresponde a toda mi clase
    def imprime_lista(cls): #cls en vez de self, corresponde a todo(mi clase completa) 
        print("Total de personas:", len(cls.lista_personas))
        for persona in cls.lista_personas: # cls = Persona
            print(persona.nombre) #VARIABLE persona NO LA CLASE

    
