import json
datos = {}
def guardar_datos():
    with open("datos.json", "w") as f:
        json.dump(datos, f, indent=4) # Guardado formateado
def cargar_datos():
    global datos
    with open("datos.json", "r") as f:
        datos = json.load(f)
def insertar_profesor(nombreProfesor, asignatura):
    try:
        if nombreProfesor.strip() == "" or asignatura.strip() == "":
            raise ValueError
        if nombreProfesor in datos["profesores"]:
            print("Este profesor ya existe y su asignatura es:",
                  datos["profesores"][nombreProfesor]["asignatura"])
            return
        datos["profesores"][nombreProfesor] = {"asignatura": asignatura}
        guardar_datos()
    except ValueError:
        print("Error: Los datos no son correctos")

def insertar_alumno(nombreAlumno, nivel):
    try:
        if nombreAlumno.strip() == "" or nivel.strip() == "":
            raise ValueError
        if nombreAlumno in datos["alumnos"]:
            print("Este alumno ya existe y su nivel es:",
                  datos["alumnos"][nombreAlumno]["nivel"])
            return
        datos["alumnos"][nombreAlumno] = {"nivel": nivel, "notas": []}
        guardar_datos()
    except ValueError:
        print("Error: Los datos no son correctos")

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
        index = int(index)
        if nombre not in datos["alumnos"]:
            print("El alumno no existe")
            return
        if index < 0 or index >= len(datos["alumnos"][nombre]["notas"]):
            print("Posición incorrecta")
            return
        datos["alumnos"][nombre]["notas"][index] = notaFloat
        guardar_datos()
    except ValueError:
        print("Nota y index tienen que ser número")

def eliminar_profesor(nombre):
    if nombre in datos["profesores"]:
        del datos["profesores"][nombre]
    elif nombre in datos["alumnos"]:
        del datos["alumnos"][nombre]
    else:
        print("Esta persona no existe")

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
                insertar_profesor(nombre_prof, asignatura)
            else:
                nombre_prof = input("Introduce el nombre del profesor que quieres borrar ")
                eliminar_profesor(nombre_prof)
        elif opcion_administrador == 4:
            opcion_anadir_borrar = input("¿Quieres añadir un alumno? (si/no) ")
            if opcion_anadir_borrar == "si":
                nombre_alumno = input("Introduce el nombre del alumno ")
                nivel = input("Introduce el nivel del alumno ")
                insertar_alumno(nombre_alumno, nivel)
            else:
                nombre_alumno = input("Introduce el nombre del alumno que quieres borrar ")
                eliminar_profesor(nombre_alumno)
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
            opcion_uno_varios = input("¿Quieres añadir la nota a todos los alumnos? (si/no) ")
            if opcion_uno_varios == "si":
                print("**** Añadir nota a todos los alumnos ****")
                for clave, valor in datos["alumnos"].items():
                    print(f"Alumno : {clave}")
                    valor["notas"].append(float(input("Introduce la nota ")))
            else:
                nombre = input("Introduce el nombre del alumno ")
                if nombre in datos["alumnos"]:
                    nota = float(input("Introduce la nota de este alumno "))
                    datos["alumnos"][nombre]["notas"].append(nota)
                else:
                    print("Este alumno no existe")
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
