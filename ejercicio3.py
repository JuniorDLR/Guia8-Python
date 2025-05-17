# Caso 3: Cálculo de promedio académico en la UAM
# Elabore un programa que procese las calificaciones de varios estudiantes de la carrera de
# Ingeniería en Sistemas de la Información en la UAM. Por cada estudiante, se ingresarán las
# calificaciones de tres asignaturas, y cada asignatura incluirá tres tareas y un examen. El
# programa debe calcular el promedio por asignatura y el promedio general del estudiante. Utilice
# estructuras cíclicas anidadas para manejar estudiantes, asignaturas y evaluaciones.

print("Promedio académico - UAM")
print("")

print("Bienvenido al sistema de cálculo de promedio de UAM")
print("")

veces = int(input("Ingrese la cantidad de estudiantes que utilizarán el programa: "))
print("")

for i in range (veces):
    print(f"\n---Usuario #{i + 1}----")
    
    promedios = 0

    for u in range (3):
        if u == 0:
            print("\nCalificaciones de la primera asignatura:")
        elif u == 1:
            print("\nCalificaciones de la segunda asignatura:")
        elif u == 2:
            print("\nCalificaciones de la tercera asignatura:")
        tarea1 = int(input("Ingrese la calificación de su primera tarea: "))
        tarea2 = int(input("Ingrese la calificación de su segunda tarea: "))
        tarea3 = int(input("Ingrese la calificación de su tercer tarea: "))
        examen = int(input("Ingrese la calificación de su examen: "))
        
        print("")

        promedio = (tarea1 + tarea2 + tarea3 + examen) / 4
        print(f"Promedio de esta asignatura: {promedio:.2f}\n")

        promedios += promedio

    promedio_general = promedios / 3
    print(f"Promedio general del estudiante: {promedio_general:.2f}")
    print("")