class Alumno:
	def __init__(self, nombre, apellido, dni, legajo):
		self.nombre = nombre
		self.apellido = apellido
		self.dni = dni
		self.legajo = legajo

class Materia:
	def __init__(self, nombre, dia, profesor, horario="Noche"):
		self.nombre = nombre
		self.dia = dia
		self.profesor = profesor
		self.horario = horario

class Universidad:
	def __init__(self, nombre, carrera):
		self.nombre = nombre
		self.carrera = carrera

class Curso:
	def __init__(self, materia, año, alumnos):
		self.materia = materia
		self.año = año
		self.alumnos = alumnos

if __name__ == "__main__":
	#Creamos un par de materias
	edd = Materia(nombre="Estructura de Datos", dia= "Lunes", profesor = "Martin Santoro")
	par = Materia(nombre = "Paradigmas de Programacion", dia = "Viernes", profesor = "Leandro Colombo")
	arq = Materia(nombre = "Arquitectura de Computadoras", dia = "Lunes", profesor = "Martin Santoro")
	dlo = Materia(nombre = "Diagramacion Logica", dia = "Viernes", profesor = "Leandro Colombo")
	
	#Creamos las carreras en un diccionario con las materias adentro de una lista
	carreras = {"Analisis": [dlo,arq, par, edd]}
	
	#Creamos una universidad
	universidad = Universidad(nombre = "IFTS18", carrera = carreras)
	
	#Creamos algunos alumnos
	juan = Alumno("Juan", "Apellido1", 1, 1)
	pedro = Alumno("Pedro", "Apellido2", 2, 2)
	maga = Alumno("Magali", "Apellido3", 3, 3)
	jose = Alumno("Jose", "Apellido4", 4, 4)
	
	#Creamos un curso para tener de prueba
	par_2018 = Curso(materia = par, año = "2018", alumnos = [juan, pedro, maga, jose])
	print(par_2018.curso.alumnos)
	#Ahora verificamos que esto funciona
	print(f"El curso es: {par_2018.materia.nombre}")
	print(f"Se cursa el dia: {par_2018.materia.dia}")
	print(f"El Profesor es: {par_2018.materia.profesor}")
	print(f"Se cursa en turno: {par_2018.materia.horario}")
	
	
	
