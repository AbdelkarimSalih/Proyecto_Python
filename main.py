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
    filename='Proyecto_Python/fichero.log',
    filemode='a' 
)
# 4. Handler 2: Crear un handler para la consola (stdout)
# Este handler será más estricto y solo mostrará WARNING y superiores
consola_handler = logging.StreamHandler(sys.stdout)
consola_handler.setLevel(logging.INFO) # Establece su propio umbral
consola_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))

# 5. Aplicar el handler de consola al logger raíz
logging.getLogger().addHandler(consola_handler)

# clases
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Administrador(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def imprimir_profesores(self):
        """
        Muestra por pantalla la lista de profesores y sus asignaturas.
        """
        print("**** La lista de profesores ****")
        print("Profesor : Asignatura")
        for clave, valor in datos["profesores"].items():
            print(f"{clave} : {valor['asignatura']}")

    def asignaturaAsignada(self):
        return {"asignatura": self.asignatura}
    
    def imprimir_alumnos(self):
        """
        Muestra por pantalla la lista de alumnos y su nivel.
        """
        print("**** La lista de alumnos ****")
        print("Alumno : Nivel")
        for clave, valor in datos["alumnos"].items():
            print(f"{clave} : {valor['nivel']}")
    
    def insertar_profesor(self,profesor):
        """ Inserta un profesor con su asignatura en el sistema. """
        try:
            if profesor.nombre in datos["profesores"]:
                logging.warning(f"Profesor {profesor.nombre} ya existe su asignatura es:{datos["profesores"][profesor.nombre]["asignatura"]}")
                return
            datos["profesores"][profesor.nombre] = {"asignatura": profesor.asignatura}
            guardar_datos()
            logging.info(f"Profesor {profesor.nombre} añadido correctamente")
        except ValueError:
            logging.error(f"Error: Los datos no son correctos")
            print("Error: Los datos no son correctos")

    def insertar_alumno(self,alumno):
        """Inserta un nuevo alumno con su nivel."""
        try:
            if alumno.nombre in datos["alumnos"]:
                logging.warning(f"Alumno {alumno.nombre} ya existe y su nivel es:{datos["alumnos"][alumno.nombre]["nivel"]}")
                return
            datos["alumnos"][alumno.nombre] = {"nivel": alumno.nivel, "notas": []}
            guardar_datos()
            logging.info(f"Alumno {alumno.nombre} añadido correctamente")
        except ValueError:
            logging.error(f"Error: Los datos no son correctos")
    
    def eliminar_profesor(self,nombre):
        """ Elimina un profesor del sistema. """
        if nombre in datos["profesores"]:
            del datos["profesores"][nombre]
            guardar_datos()
            logging.info(f"Profesor {nombre} eliminado")
        elif nombre in datos["alumnos"]:
            del datos["alumnos"][nombre]
            logging.info(f"Alumno {nombre} eliminado")
        else:
            logging.warning("Persona no encontrada")
    
    def eliminar_alumno(self,nombre):
        """ Elimina un alumno del sistema """
        if nombre in datos["alumnos"]:
            del datos["alumnos"][nombre]
            logging.info(f"Alumno {nombre} eliminado")
            guardar_datos()
        else:
            logging.warning("Persona no encontrada")
    def calcular_media_alumno(self,nombre):
        """
        Calcula la media de las notas de un alumno.

        Parámetros:
        nombre (str): nombre del alumno

        Retorna:
        str: nombre del alumno y su media con dos decimales
        None: si el alumno no existe o no tiene notas
        """
        if nombre not in datos["alumnos"]:
            logging.error(f"El alumno {nombre} no existe")
            return 
        notas = datos["alumnos"][nombre]["notas"]

        if not notas:
            logging.warning(f"El alumno {nombre} no tiene notas")
            print("Este alumno no tiene notas")
            return None

        media =  round(sum(notas) / len(notas), 2)
        return nombre+"   :   "+str(media)
    
    def imprimir_Media_alumnos(self):
        print(f"Alumno   :   Media")
        for clave, valor in datos["alumnos"].items():
            print(self.calcular_media_alumno(clave))

class Profesor(Persona):
    def __init__(self, nombre, asignatura):
        super().__init__(nombre)
        self.asignatura = asignatura

    def asignaturaAsignada(self):
        return {"asignatura": self.asignatura}

    def imprimir_alumnos(self):
        """
        Muestra por pantalla la lista de alumnos y su nivel.
        """
        print("**** La lista de alumnos ****")
        print("Alumno : Nivel")
        for clave, valor in datos["alumnos"].items():
            print(f"{clave} : {valor['nivel']}")
    def anadir_notas(self,nombre=""):
        if(nombre.strip() != ""):
            if nombre in datos["alumnos"]:
                nota = float(input("Introduce la nota de este alumno "))
                datos["alumnos"][nombre]["notas"].append(nota)
                guardar_datos()
                logging.info(f"Has añadido una nota a {nombre} con exito")
            else:
                print("Este alumno no existe")
        else:
            print("**** Añadir nota a todos los alumnos ****")
            for clave, valor in datos["alumnos"].items():
                print(f"Alumno : {clave}")
                valor["notas"].append(float(input("Introduce la nota ")))
            guardar_datos()
            logging.info(f"Has añadido una nota a todos los alumnos con exito")
    def borrar_notas(self):
        alumno =  input("¿Introduce el alumno que quieres borrar su nota? ")
        posicion_nota = int(input("Introduce la posicion de la nota que quieres borra.Ojo la posicion empeza de 0:"))
        del datos["alumnos"][alumno]["notas"][posicion_nota]
        logging.info(f"La nota de Alumno {alumno} se ha borrado con exito")
    
    def imprimir_notas(self):
        print("**** Notas de los alumnos ****")
        for clave, valor in datos["alumnos"].items():
            print(f"+++ Notas de {clave} +++")
            for nota in valor["notas"]:
                print(nota)
    
    def modificar_Notas(self,nombre, nota, index):
        """ Modifica una nota concreta de un alumno. """
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
    def calcular_media_alumno(self,nombre):
        """
        Calcula la media de las notas de un alumno.

        Parámetros:
        nombre (str): nombre del alumno

        Retorna:
        str: nombre del alumno y su media con dos decimales
        None: si el alumno no existe o no tiene notas
        """
        if nombre not in datos["alumnos"]:
            logging.error(f"El alumno {nombre} no existe")
            return 
        notas = datos["alumnos"][nombre]["notas"]

        if not notas:
            logging.warning(f"El alumno {nombre} no tiene notas")
            print("Este alumno no tiene notas")
            return None

        media =  round(sum(notas) / len(notas), 2)
        return nombre+"   :   "+str(media)
    
    def imprimir_Media_alumnos(self):
        print(f"Alumno   :   Media")
        for clave, valor in datos["alumnos"].items():
            print(self.calcular_media_alumno(clave))

class Alumno(Persona):
    def __init__(self, nombre, nivel, notas=None):
        super().__init__(nombre)
        self.nivel = nivel
        self.notas = notas if notas else []
    def imprimir_misNotas(self):
        print("***Mis Notas ***")
        for n in self.notas:
            print(n)
    def calcular_media_alumno(self):

        if not self.notas:
            logging.warning(f"El alumno {self.nombre} no tiene notas")
            print("Este alumno no tiene notas")
            return None

        media =  round(sum(self.notas) / len(self.notas), 2)
        return self.nombre+"   :   "+str(media)

datos = {}
def guardar_datos():
    """Guarda el diccionario datos en el archivo JSON."""
    with open("Proyecto_Python/datos.json", "w") as f:
        json.dump(datos, f, indent=4) # Guardado formateado
def cargar_datos():
    """Carga los datos desde el archivo JSON."""
    global datos
    try:
        with open("Proyecto_Python/datos.json", "r") as f:
            datos = json.load(f)
            logging.info(f"Los datos han sido cargados")
    except FileNotFoundError:
        logging.warning("datos.json no encontrado, se crea uno nuevo")

def buscarProfesor(nombre):
    if nombre in datos["profesores"]:
        return datos["profesores"][nombre]["asignatura"]
    else:
        print("Este profesor no existe")
        return None

def buscarAlumno(nombre):
    if nombre in datos["alumnos"]:
        return datos["alumnos"][nombre]["nivel"],datos["alumnos"][nombre]["notas"]
    else:
        print("Este alumno no existe")
        return None






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
    administrador = Administrador("admin")
    while True:
        print("**** Espacio administrador ****")
        print("     1- Ver la lista de profesores")
        print("     2- Ver la lista de alumnos")
        print("     3- Añadir o borrar un profesor")
        print("     4- Añadir o borrar un alumno")
        print("     5- ver la media de los alumnos")
        print("     6- Salir")
        try:
            opcion_administrador = int(input("Escribe el numero de tu opcion: "))
        except ValueError:
            continue

        if opcion_administrador == 1:
            administrador.imprimir_profesores()
        elif opcion_administrador == 2:
            administrador.imprimir_alumnos()
        elif opcion_administrador == 3:
            opcion_anadir_borrar = input("¿Quieres añadir un profesor? (si/no) ")
            if opcion_anadir_borrar == "si":
                nombre_prof = input("Introduce el nombre del profesor ")
                asignatura = input("Introduce la asignatura del profesor ")
                if nombre_prof.strip() != "" and asignatura.strip() !="":
                    profesor = Profesor(nombre_prof,asignatura)
                    administrador.insertar_profesor(profesor)
                else:
                    logging.error(f"El nombre del profesor y asignatura tienen que ser una cadena de letras")
            else:
                nombre_prof = input("Introduce el nombre del profesor que quieres borrar ")
                administrador.eliminar_profesor(nombre_prof)
        elif opcion_administrador == 4:
            opcion_anadir_borrar = input("¿Quieres añadir un alumno? (si/no) ")
            if opcion_anadir_borrar == "si":
                nombre_alumno = input("Introduce el nombre del alumno ")
                nivel = input("Introduce el nivel del alumno ")
                if nombre_alumno.strip() != "" and nivel.strip() !="":
                    alumno = Alumno(nombre_alumno,nivel)
                    administrador.insertar_alumno(alumno)
                else:
                    logging.error(f"El nombre del alumno y su nivel tienen que ser una cadena de letras")
            else:
                nombre_alumno = input("Introduce el nombre del alumno que quieres borrar: ")
                administrador.eliminar_alumno(nombre_alumno)
        elif opcion_administrador == 5:
            opcion_solo_todos = input("¿Quieres ver la media de todos los alumnos o un especifico? (todos/uno): ")
            if opcion_solo_todos == "todos":
               administrador.imprimir_Media_alumnos()
            else:
                nombre = input("?Introduce el nombre del alumno que quieres ver su media: ")
                print(f"Alumno   :   Media")
                print(administrador.calcular_media_alumno(nombre))
        else:
            break

elif opcion_elegido == 2:
    while True:
        print("**** Espacio profesor ****")
        print("     1- Ver la lista de alumnos")
        print("     2- Añadir o borrar notas de alumnos")
        print("     3- Ver las notas de todos los alumnos")
        print("     4- Modificar la nota de un alumno")
        print("     5- Ver la nota media de los alumnos")
        print("     6- Salir")
        try:
            nombreProfesor = input("Escribe tu nombre: ")
            asignatura = buscarProfesor(nombreProfesor)
            if(asignatura):
                profesor = Profesor(nombreProfesor,asignatura)
                opcion_profesor = int(input("Escribe el numero de tu opcion: "))
            else:
                opcion_profesor=6
        except ValueError:
            continue

        if opcion_profesor == 1:
            profesor.imprimir_alumnos()
        elif opcion_profesor == 2:
            opcion_añadir_borrar = input("¿Quieres añadir o borrar algun nota? (A/B) ")
            if opcion_añadir_borrar == "A":
                opcion_uno_varios = input("¿Quieres añadir la nota a todos los alumnos? (si/no) ")
                if opcion_uno_varios == "si":
                    profesor.anadir_notas()
                else:
                    nombre = input("Introduce el nombre del alumno ")
                    profesor.anadir_notas(nombre)
            else:
                profesor.borrar_notas()
                guardar_datos()
            
        elif opcion_profesor == 3:
            profesor.imprimir_notas()
        elif opcion_profesor == 4:
            nombreAlumno = input("Introduce el nombre del alumno ")
            nota = input("Introduce la nota ")
            pos = input("Introduce la posición de la nota, la primera es 0 ")
            profesor.modificar_Notas(nombreAlumno, nota, pos)
        elif opcion_profesor == 5:
            opcion_solo_todos = input("¿Quieres ver la media de todos los alumnos o un especifico? (todos/uno): ")
            if opcion_solo_todos == "todos":
                profesor.imprimir_Media_alumnos()
            else:
                nombre = input("?Introduce el nombre del alumno que quieres ver su media: ")
                print(f"Alumno   :   Media")
                print(profesor.calcular_media_alumno(nombre))
        else:
            break
else:
    while True:
        print("**** Espacio alumno ****")
        print("     1- Ver mis notas")
        print("     2- Ver la media")
        print("     3- Salir")
        try:
            nombreAlumno = input("Escribe tu nombre: ")
            nivel = buscarAlumno(nombreAlumno)
            if(buscarAlumno(nombreAlumno)):
                nivel,notas =buscarAlumno(nombreAlumno)
                alumno = Alumno(nombreAlumno,nivel,notas)
                opcion_alumno = int(input("Escribe el numero de tu opcion: "))
            else:
                opcion_alumno = 3
        except ValueError:
            continue

        if opcion_alumno == 1:
            alumno.imprimir_misNotas()
        elif opcion_alumno == 2:
            print(f"Alumno   :   Media")
            print(alumno.calcular_media_alumno())
        else:
            break
