class Alumno:
	def __init__(self, nombre, apellido, dni, legajo):
		self.nombre = nombre
		self.apellido = apellido
		self.dni = dni
		self.legajo = legajo
	def Inscribir (self, curso):
		curso.alumnos.append(self)
	#def Inscribir(self, curso):
	#	par_2018.alumnos.append(self.apellido)

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
	def imprimirLista(self):
		for recorrer in self.alumnos:
			print(recorrer.nombre + " " + recorrer.apellido + f"    DNI: {recorrer.dni}     Legajo: {recorrer.legajo}" )
		print(f"TOTAL DE ALUMNOS INSCRIPTOS: {len(self.alumnos)}")
			


#if __name__ == "__main__":
	#Creamos un par de materias
edd = Materia(nombre="Estructura de Datos", dia= "Lunes", profesor = "Martin Santoro")
par = Materia(nombre = "Paradigmas de Programacion", dia = "Viernes", profesor = "Leandro Colombo")
arq = Materia(nombre = "Arquitectura de Computadoras", dia = "Lunes", profesor = "Martin Santoro")
dlo = Materia(nombre = "Diagramacion Logica", dia = "Viernes", profesor = "Leandro Colombo")
	
	#Creamos las carreras en un diccionario con las materias adentro de una lista
carreras = {"Analisis": [dlo,arq, par, edd]}
	
	#Creamos una universidad
universidad = Universidad(nombre = "IFTS18", carrera = carreras)
"""	
	#Creamos algunos alumnos
juan = Alumno("Juan", "Apellido1", 1, 1)
pedro = Alumno("Pedro", "Apellido2", 2, 2)
maga = Alumno("Magali", "Apellido3", 3, 3)
jose = Alumno("Jose", "Apellido4", 4, 4)
	
"""
	
	
	#Creamos un curso para tener de prueba
dlo_2018 = Curso(materia = dlo, año = 2018, alumnos = [])
par_2018 = Curso(materia = par, año = 2018, alumnos = [])
arq_2018 = Curso(materia = arq, año = 2018, alumnos = [])
edd_2018 = Curso(materia = edd, año = 2018, alumnos = [])


print(f"{universidad.nombre}")
print("INSCRIPCION A MATERIAS DE LA CARRERA DE ANALISTA DE SISTEMAS\n\n")
flag = "Y"

while(flag == "Y"):
	nombre = input("Ingrese nombre: ")
	apellido = input("Ingrese apellido: ")
	dni = int(input("Ingrese DNI: "))
	legajo = int(input("Ingrese Legajo: "))

	alumnonuevo = Alumno(nombre, apellido, dni, legajo)


	print("\n\nSeleccione la materia a inscribirse\n")
	print(f"{dlo.nombre}: dlo\n" f"{par.nombre}: par\n" f"{arq.nombre}: arq\n" f"{edd.nombre}: edd\n")

	opcion = input()


	if(opcion=="dlo"):
		alumnonuevo.Inscribir(dlo_2018)
	
	if(opcion=="par"):
		alumnonuevo.Inscribir(par_2018)

	if(opcion=="arq"):
		alumnonuevo.Inscribir(arq_2018)

	if(opcion=="edd"):
		alumnonuevo.Inscribir(edd_2018)
	flag=input("Inscribir otro alumno? (Y / N): ")

#Borrar la pantalla.
import os
os.system('cls')

flag2 = "Y"
while(flag2 == "Y"):

	print("IMPRIMIENDO LISTA DE ALUMNOS POR MATERIA\n")

	print(f"{dlo.nombre}: dlo_2018\n" f"{par.nombre}: par_2018\n" f"{arq.nombre}: arq_2018\n" f"{edd.nombre}: edd_2018\n")
	lista=input("Ingrese la materia a imprimir listado de alumnos: ")


	if(lista=="dlo_2018"):
		dlo_2018.imprimirLista()
			
	if(lista=="par_2018"):
		par_2018.imprimirLista()

	if(lista=="arq_2018"):
		arq_2018.imprimirLista()

	if(lista=="edd_2018"):
		edd_2018.imprimirLista()
	
	flag2 = input("Imprimir otro curso? (Y / N)")
	
"""	
	#Ahora verificamos que esto funciona
print(f"El curso es: {par_2018.materia.nombre}")
print(f"Se cursa el dia: {par_2018.materia.dia}")
print(f"El Profesor es: {par_2018.materia.profesor}")
print(f"Se cursa en turno: {par_2018.materia.horario}")


	#gabi = Alumno("gabi", "minces", 4, 4)

	

	
	
	
	
	
nombre = input("Pone el nombre del alumno: ")
apellido = input("Pone el apeliido del alumno: ")
dni = int(input("Pone el DNI del alumno: "))
legajo = int(input("Pone el legajo del alumno: "))
alumnonuevo = Alumno(nombre,apellido,dni,legajo)
par_2018.alumnos.append(alumnonuevo)

flag = "HOLA"
print("Si desea imprimir un alumno ponga Y sino N: ")
n = input()
if (n == "Y"):
	while (flag != "BASTA"):
		nombre = input("Pone el nombre del alumno: ")
		apellido = input("Pone el apellido del alumno: ")
		dni = int(input("Pone el DNI del alumno: "))
		legajo = int(input("Pone el legajo del alumno: "))
		alumnonuevo = Alumno(nombre,apellido,dni,legajo)
		par_2018.alumnos.append(alumnonuevo)
		flag = input("desea seguir parar de agregar ponga BASTA")

print(alumnonuevo.nombre)
par_2018.alumnos.append(alumnonuevo)

gabi.Inscribir(par_2018)
print(len(par_2018.alumnos))
	#print(par_2018.alumnos[4].apellido)

	
#print(carreras["Analisis"][0].nombre)
	
	"""
	

