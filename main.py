from Estudiante import Estudiante
from Persona import Persona
from Estudiante import Estudiante

#Instancia de persona
elena = Persona("Elena", "De Troya", "elena@codingdojo.com", 30)
juana = Persona("Juana", "De Arco", "juana@codingdojo.com", 17)

print(elena.nombre)
print(juana.nombre)

elena.cumpleaños() #30+1
print(elena.edad)

print(elena.lineas_codigo)
print(juana.lineas_codigo)

elena.codificar(45)
print(elena.lineas_codigo)
elena.codificar(10)
print(elena.lineas_codigo)
print(juana.lineas_codigo)

print(elena.pais)

Persona.imprime_lista()
pablo = Persona("Pablo", "Picasso", "pablo@codingdojo.com", 50)
Persona.imprime_lista()

juana.cumpleaños()

juana.tomar_cerveza()

pablo.codificar(101)

elena.curso.agrega_calificacion(9)
elena.curso.agrega_calificacion(7)

print(elena.curso.calificaciones)

pedro = Estudiante("Pedro", "Páramo", "pedro@codingdojo.como",30, 1234)

print(pedro.id)

pedro.codificar(100)
print(pedro.lineas_codigo)#estudiante tambien hereda los metodos de persona

Persona.imprime_lista() #también imprime a pedro porque tambien es persona

Estudiante.imprime_lista()

pedro.cumpleaños()

#elena.que_haces()
pedro.que_haces()
pedro.estudiar()