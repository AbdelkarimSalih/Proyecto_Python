import json
import logging
import sys
# --- 1. CONFIGURACIÓN DEL SISTEMA DE REGISTRO ---

# El 'logger' raíz (root) se usa aquí para la configuración global.
logging.basicConfig(
    # 1. Nivel mínimo global: Se procesarán mensajes desde INFO
    level=logging.INFO, 
    
    # 2. Formato de los mensajes
    format='%(asctime)s - %(levelname)s - Módulo: %(module)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    
    # 3. Handler 1: Guardar todos los mensajes (INFO+) en un fichero
    filename='fichero.log',
    filemode='a' 
)
# 4. Handler 2: Crear un handler para la consola (stdout)
# Este handler será más estricto y solo mostrará WARNING y superiores
consola_handler = logging.StreamHandler(sys.stdout)
consola_handler.setLevel(logging.INFO) # Establece su propio umbral
consola_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))

# 5. Aplicar el handler de consola al logger raíz
logging.getLogger().addHandler(consola_handler)




datos = {}
def guardar_datos():
    with open("Proyecto_Python/datos.json", "w") as f:
        json.dump(datos, f, indent=4) # Guardado formateado
def cargar_datos():
    global datos
    try:
        with open("Proyecto_Python/datos.json", "r") as f:
            datos = json.load(f)
            logging.info(f"Los datos han sido cargados")
    except FileNotFoundError:
        logging.warning("datos.json no encontrado, se crea uno nuevo")
def insertar_profesor(nombreProfesor, asignatura):
    try:
        if nombreProfesor.strip() == "" or asignatura.strip() == "":
            raise ValueError
        if nombreProfesor in datos["profesores"]:
            logging.warning(f"Profesor {nombreProfesor} ya existe su asignatura es:{datos["profesores"][nombreProfesor]["asignatura"]}")
            return
        datos["profesores"][nombreProfesor] = {"asignatura": asignatura}
        guardar_datos()
        logging.info(f"Profesor {nombreProfesor} añadido correctamente")
    except ValueError:
        logging.error(f"Error: Los datos no son correctos")
        print("Error: Los datos no son correctos")

def insertar_alumno(nombreAlumno, nivel):
    try:
        if nombreAlumno.strip() == "" or nivel.strip() == "":
            raise ValueError
        if nombreAlumno in datos["alumnos"]:
            logging.warning(f"Alumno {nombre} ya existe y su nivel es:{datos["alumnos"][nombreAlumno]["nivel"]}")
            return
        datos["alumnos"][nombreAlumno] = {"nivel": nivel, "notas": []}
        guardar_datos()
        logging.info(f"Alumno {nombre} añadido correctamente")
    except ValueError:
        logging.error(f"Error: Los datos no son correctos")

def imprimir_profesores():
    print("**** La lista de profesores ****")
    print("Profesor : Asignatura")
    for clave, valor in datos["profesores"].items():
        print(f"{clave} : {valor['asignatura']}")

def imprimir_alumnos():
    print("**** La lista de alumnos ****")
    print("Alumno : Nivel")
    for clave, valor in datos["alumnos"].items():
        print(f"{clave} : {valor['nivel']}")

def buscarProfesor(nombre):
    if nombre in datos["profesores"]:
        return datos["profesores"][nombre]["asignatura"]
    else:
        print("Este profesor no existe")
        return

def buscarAlumno(nombre):
    if nombre in datos["alumnos"]:
        return datos["alumnos"][nombre]["notas"]
    else:
        print("Este alumno no existe")
        return []

def modificar_Notas(nombre, nota, index):
    try:
        notaFloat = float(nota)
        if 0 > nota > 10:
            logging.warning(f"La nota tiene que estar entre 0 y 10")
            print("La nota tiene que estar entre 0 y 10")
        index = int(index)
        if nombre not in datos["alumnos"]:
            logging.error("Alumno no existe")
            return
        if index < 0 or index >= len(datos["alumnos"][nombre]["notas"]):
            logging.error("Índice de nota incorrecto")
            return
        datos["alumnos"][nombre]["notas"][index] = notaFloat
        guardar_datos()
    except ValueError:
        logging.error(f"Nota o índice no numérico")

def eliminar_profesor(nombre):
    if nombre in datos["profesores"]:
        del datos["profesores"][nombre]
        logging.info(f"Profesor {nombre} eliminado")
    elif nombre in datos["alumnos"]:
        del datos["alumnos"][nombre]
        logging.info(f"Alumno {nombre} eliminado")
        guardar_datos()
    else:
        logging.warning("Persona no encontrada")
def eliminar_alumno(nombre):
    if nombre in datos["alumnos"]:
        del datos["alumnos"][nombre]
        logging.info(f"Alumno {nombre} eliminado")
        guardar_datos()
    else:
        logging.warning("Persona no encontrada")
print("----------------------------------------------")
print("         ****Introduce quién eres****")
print("   - Si eres administrador elige el numero 1")
print("   - Si eres profesor elige el numero 2")
print("   - Si eres alumno elige el numero 3")
# guardar_datos()
cargar_datos()
try:
    opcion_elegido = int(input("Escribe el numero de tu opcion: "))
except ValueError:
    opcion_elegido = 0
    logging.error(f"La opcion elegido tiene que estar entre 1 y 5")

if opcion_elegido == 1:
    while True:
        print("**** Espacio administrador ****")
        print("     1- Ver la lista de profesores")
        print("     2- Ver la lista de alumnos")
        print("     3- Añadir o borrar un profesor")
        print("     4- Añadir o borrar un alumno")
        print("     5- Salir")
        try:
            opcion_administrador = int(input("Escribe el numero de tu opcion: "))
        except ValueError:
            continue

        if opcion_administrador == 1:
            imprimir_profesores()
        elif opcion_administrador == 2:
            imprimir_alumnos()
        elif opcion_administrador == 3:
            opcion_anadir_borrar = input("¿Quieres añadir un profesor? (si/no) ")
            if opcion_anadir_borrar == "si":
                nombre_prof = input("Introduce el nombre del profesor ")
                asignatura = input("Introduce la asignatura del profesor ")
                if nombre_prof.strip() != "" and asignatura.strip() !="":
                    insertar_profesor(nombre_prof, asignatura)
                else:
                    logging.error(f"El nombre del profesor y asignatura tienen que ser una cadena de letras")
            else:
                nombre_prof = input("Introduce el nombre del profesor que quieres borrar ")
                eliminar_profesor(nombre_prof)
        elif opcion_administrador == 4:
            opcion_anadir_borrar = input("¿Quieres añadir un alumno? (si/no) ")
            if opcion_anadir_borrar == "si":
                nombre_alumno = input("Introduce el nombre del alumno ")
                nivel = input("Introduce el nivel del alumno ")
                if nombre_alumno.strip() != "" and nivel.strip() !="":
                    insertar_alumno(nombre_alumno, nivel)
                else:
                    logging.error(f"El nombre del alumno y su nivel tienen que ser una cadena de letras")
            else:
                nombre_alumno = input("Introduce el nombre del alumno que quieres borrar ")
                eliminar_alumno(nombre_alumno)
        else:
            break

elif opcion_elegido == 2:
    while True:
        print("**** Espacio profesor ****")
        print("     1- Ver la lista de alumnos")
        print("     2- Añadir o borrar notas de alumnos")
        print("     3- Ver las notas de todos los alumnos")
        print("     4- Modificar la nota de un alumno")
        print("     5- Salir")
        try:
            opcion_profesor = int(input("Escribe el numero de tu opcion: "))
        except ValueError:
            continue

        if opcion_profesor == 1:
            imprimir_alumnos()
        elif opcion_profesor == 2:
            opcion_añadir_borrar = input("¿Quieres añadir o borrar algun nota? (A/B) ")
            if opcion_añadir_borrar == "A":
                opcion_uno_varios = input("¿Quieres añadir la nota a todos los alumnos? (si/no) ")
                if opcion_uno_varios == "si":
                    print("**** Añadir nota a todos los alumnos ****")
                    for clave, valor in datos["alumnos"].items():
                        print(f"Alumno : {clave}")
                        valor["notas"].append(float(input("Introduce la nota ")))
                    guardar_datos()
                    logging.info(f"Has añadido una nota a todos los alumnos con exito")
                else:
                    nombre = input("Introduce el nombre del alumno ")
                    if nombre in datos["alumnos"]:
                        nota = float(input("Introduce la nota de este alumno "))
                        datos["alumnos"][nombre]["notas"].append(nota)
                        guardar_datos()
                        logging.info(f"Has añadido una nota a {nombre} con exito")
                    else:
                        print("Este alumno no existe")
            else:
                alumno =  input("¿Introduce el alumno que quieres borrar su nota? ")
                posicion_nota = int(input("Introduce la posicion de la nota que quieres borra.Ojo la posicion empeza de 0:"))
                del datos["alumnos"][alumno]["notas"][posicion_nota]
                logging.info(f"La nota de Alumno {alumno} se ha borrado con exito")
                guardar_datos()
            
        elif opcion_profesor == 3:
            print("**** Notas de los alumnos ****")
            for clave, valor in datos["alumnos"].items():
                print(f"+++ Notas de {clave} +++")
                for nota in valor["notas"]:
                    print(nota)
        elif opcion_profesor == 4:
            nombreAlumno = input("Introduce el nombre del alumno ")
            nota = input("Introduce la nota ")
            pos = input("Introduce la posición de la nota, la primera es 0 ")
            modificar_Notas(nombreAlumno, nota, pos)
        else:
            break
else:
    while True:
        print("**** Espacio alumno ****")
        print("     1- Ver mis notas")
        print("     2- Salir")
        try:
            opcion_alumno = int(input("Escribe el numero de tu opcion: "))
        except ValueError:
            continue

        if opcion_alumno == 1:
            nombre = input("Introduce tu nombre ")
            notas = buscarAlumno(nombre)
            for n in notas:
                print(n)
        else:
            break
