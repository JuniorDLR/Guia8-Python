# Caso 4: Registro de participación estudiantil por carrera en la UAM
# Desarrolle un programa que registre la participación de estudiantes de la UAM en actividades
# extracurriculares por carrera. Considere tres carreras (por ejemplo: Sistemas, Marketing y
# Derecho), cada una con tres años académicos, y cada año con dos secciones. Por cada
# sección, se debe registrar cuántos estudiantes participaron. El programa debe mostrar el total
# por carrera y el total general de participantes. Utilice bucles anidados.

carreras = ["Sistemas", "Marketing", "Derecho"]
anios = [1, 2, 3]
secciones = ["A", "B"]

total_general = 0

total_por_carrera = {carrera: 0 for carrera in carreras}

print("Registro de participación estudiantil en actividades extracurriculares - UAM\n")

for carrera in carreras:
    print(f"Carrera: {carrera}")
    
    for anio in anios:
        for seccion in secciones:
            participantes = int(input(f"Ingrese número de estudiantes que participaron en {anio}° año, sección {seccion}: "))
            
            total_por_carrera[carrera] += participantes
            total_general += participantes
    
    print(f"Total participantes en {carrera}: {total_por_carrera[carrera]}\n")

print(f"Total general de participantes en todas las carreras: {total_general}")