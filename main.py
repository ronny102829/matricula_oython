# """
# - registrar alumnos 
# - generar fichas de matricula
# - mostrar la lista de todos los matriculas 
# - filtrar matriculas por programa de estudio
# """
# lista_alumno=[{},{},{},{}]
# nombre=input("ingresar el nombre del alumno: ")
# apellido=input("ingresar el apellido del alumno: ")
# nombre2=input("ingresar el nombre del alumno: ")
# apellido2=input("ingresar el apellido del alumno: ")
# alumno={
#     "nombre":npmbre
#     "apellido":apelido
# }
# alumno={
#     "nombre":npmbre2
#     "apellido":apelido2
# }
# print(lista_alumno)
# print(lista_alumno)
# lista_alumno.append(nombre)
# lista_alumno.append(apellido)


# tarea viernes 11
# Obtener datos del estudiante
# dni = input("Ingrese su DNI: ")
# while not dni:  # Verificar si el DNI está vacío
#     dni = input("Ingrese su DNI (campo obligatorio): ")

# nombre = input("Ingrese su nombre: ")
# while not nombre:  # Verificar si el nombre está vacío
#     nombre = input("Ingrese su nombre (campo obligatorio): ")

# apellido = input("Ingrese su apellido: ")
# while not apellido:  # Verificar si el apellido está vacío
#     apellido = input("Ingrese su apellido (campo obligatorio): ")

# programa_estudio = input("Ingrese su programa de estudio: ")
# while not programa_estudio:  # Verificar si el programa de estudio está vacío
#     programa_estudio = input("Ingrese su programa de estudio (campo obligatorio): ")

# ciclo = input("Ingrese su ciclo: ")
# while not ciclo:  # Verificar si el ciclo está vacío
#     ciclo = input("Ingrese su ciclo (campo obligatorio): ")

# nacionalidad = input("Ingrese su nacionalidad: ")
# while not nacionalidad:  # Verificar si la nacionalidad está vacía
#     nacionalidad = input("Ingrese su nacionalidad (campo obligatorio): ")

# fecha_nacimiento = input("Ingrese su fecha de nacimiento (AAAA-MM-DD): ")
# while not fecha_nacimiento:  # Verificar si la fecha de nacimiento está vacía
#     fecha_nacimiento = input("Ingrese su fecha de nacimiento (AAAA-MM-DD) (campo obligatorio): ")

# numero_celular = input("Ingrese su número de celular: ")
# while not numero_celular:  # Verificar si el número de celular está vacío
#     numero_celular = input("Ingrese su número de celular (campo obligatorio): ")

# email = input("Ingrese su correo electrónico: ")
# while not email:  # Verificar si el correo electrónico está vacío
#     email = input("Ingrese su correo electrónico (campo obligatorio): ")

# # Mostrar los datos ingresados
# print("\nDatos del estudiante:")
# print("DNI:", dni)
# print("Nombre:", nombre)
# print("Apellido:", apellido)
# print("Programa de estudio:", programa_estudio)
# print("Ciclo:", ciclo)
# print("Nacionalidad:", nacionalidad)
# print("Fecha de nacimiento:", fecha_nacimiento)
# print("Número de celular:", numero_celular)
# print("Correo electrónico:", email)



lista_alumnos=[]
def mensaje_menu():
     menu_opciones ="""
                bienvenido al sistema
                registra tu alumno
     1. escribe (s) si desas agregar un nuevo alumno
     2. escribe (n) si deseas salir del sistema
     escribe la accion que deseas realizar:""" 
     return menu_opciones

def ingresar_datos_alumnos():
     id=len(lista_alumnos)+1
     cui=int(input("ingresa el numero de su dni: "))
     nombre=input("ingrese nombre del alumno: ")
     apellido=input("ingrese el apellido del alumno: ")
     numero_celular=input("ingrese el numero de celular del alumno: ")
     programa_estudio=input("8ingrese el programa de estudio: ")
     ciclo_academico=input("ingrese su ciclo academico: ")
     email=input("ingrese su correo electronico: ")
     guardar_datos_alumno(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email)

def guardar_datos_alumno(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email):
     alumno= {

          "id":id,
          "cui":cui,
          "nombre":nombre,
          "apellido":apellido,
          "numero_celular":numero_celular,
          "programa_estudio":programa_estudio,
          "ciclo_academico":ciclo_academico,
          "email":email
     }     
while True:
     mensaje_menu=input(mensaje_menu())

     if menu_opciones.lower()== "n":
          print("saliendo del sistema")
          break
     elif menu_opciones.lower() == "s":
          ingresar_datos_alumno()
     else:
          print("opcion erronea")