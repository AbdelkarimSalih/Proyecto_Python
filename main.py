profesores = {
    "david" : "Mates",
    "karim" :"informatica"
}
alumnos = {
    "jero" : "primeraEso",
    "karim" :"terceraEso"
}
notas_alumnos={
    "jero":[5,6],
    "karim":[9,8]
}
def imprimir_profesores():
    print("****La list de profesores****")
    print("Profesores : Asignatura")
    for clave, valor in profesores.items():
        print(f"{clave} : {valor} ")

def imprimir_alumnos():
    print("****La list de profesores****")
    print("  Profesores : Asignatura")
    print("     Alumno  : Nivel")
    for clave, valor in alumnos.items():
        print(f"{clave} : {valor} ")
print("----------------------------------------------")
print("         ****Introduce quién eres****")
print("   - Si eres administrador elige el numero 1")
print("   - Si eres profesor elige el numero 2")
print("   - Si eres alumno elige el numero 3")
opcion_elegido = int(input("Escribe el numero de tu opcion: "))
if(opcion_elegido == 1):
    while(True):
        print("****Espacion administrador****")
        print("     1- Ver la list des profesores")
        print("     2- Ver la list des alumnos")
        print("     3- Añadir o borrar un profesor")
        print("     4- Añadir o borrar un alumno")
        print("     5- Salir")
        opcion_administrador=int(input("Escribe el numero de tu opcion:"))
        if(opcion_administrador == 1):
            imprimir_profesores()
        elif(opcion_administrador == 2): 
            imprimir_alumnos()
        elif(opcion_administrador == 3):
            opcion_anadir_borrar = input("¿Quieres añadir un profesor? (si/no)")
            if(opcion_anadir_borrar == "si"):
                nombre_prof = input("Introduce el nombre del profesor")
                asignatura = input("Introduce la asignatura del profesor")
                profesores[nombre_prof]=asignatura
            else:
                nombre_prof = input("Introduce el nombre del profesor que quieres borrar")
                del profesores[nombre_prof]
        elif(opcion_administrador == 4):
            opcion_anadir_borrar = input("¿Quieres añadir un alumno? (si/no)")
            if(opcion_anadir_borrar == "si"):
                nombre_alumno = input("Introduce el nombre del alumno")
                nivel = input("Introduce el nivel del alumno")
                alumnos[nombre_alumno]=nivel
            else:
                nombre_alumno = input("Introduce el nombre del alumno que quieres borrar")
                del alumnos[nombre_alumno]
        else:
            break

elif(opcion_elegido == 2):
    while(True):
        print("****Espacion profesor****")
        print("     1- Ver la list des alumnos")
        print("     2- Añadir o borrar notas de alumnos")
        print("     3- Ver la notas de todos los alumnos")
        print("     4- Salir")
        opcion_profesor = int(input("Escribe el numero de tu opcion: "))
        if(opcion_profesor == 1):
            imprimir_alumnos()
        elif(opcion_profesor == 2):
            opcion_uno_varios = input("¿Quieres anadir la nota a todos los alumnos? (si/no)")
            if(opcion_uno_varios == "si"):
                print("**** Anadir nota a todos los alumnos ****")
                for clave, valor in notas_alumnos.items():
                    print(f"Alumno : {clave}")
                    notas_alumnos[clave].append(input("Introduce la nota"))
            else:
                nombre = input("Introduce el nombre del alumno")
                if nombre in notas_alumnos:
                    nota = float("Introduce la nota de este alumno")
                    notas_alumnos[nombre].append(nota)
                else:
                    print("Este alumno no existe")
        elif(opcion_profesor == 3):
            print("**** Notas de los alumnos ****")
            for clave,valor in notas_alumnos.items():
                print(f"+++ Notas de {clave} +++")
                for nota in valor:
                    print(f"{nota}")
        else:
            break

else:
    print("alumno")
