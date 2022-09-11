from Persona import Persona

#Instancia de persona
elena = Persona("Elena", "De Troya", "elena@codingdojo.com", 30)
juana = Persona("Juana", "De Arco", "juana@codingdojo.com", 20)

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

