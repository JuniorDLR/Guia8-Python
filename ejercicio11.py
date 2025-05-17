secciones = ["A", "B", "C"]
asistencia_1 = asistencia_2 = asistencia_3 = 0
inasistencia_1 = inasistencia_2 = inasistencia_3 = 0
dias = 2
estudiantes = 6

def asistencia_a(estudiante):
    global asistencia_1, inasistencia_1
    while True:
        opcion = input(f"El estudiante #{estudiante} asistió? [s/n]: ").lower()
        print("")

        if opcion == "s":
            asistencia_1 += 1
            break
        elif opcion == "n":
            inasistencia_1 += 1
            break
        else:
            print("Escriba [s] o [n]")
            continue
    
def asistencia_b(estudiante):
    global asistencia_2, inasistencia_2
    while True:
        opcion = input(f"El estudiante #{estudiante} asistió? [s/n]: ").lower()
        print("")

        if opcion == "s":
            asistencia_2 += 1
            break
        elif opcion == "n":
            inasistencia_2 += 1
            break
        else:
            print("Escriba [s] o [n]")
            continue
    
def asistencia_c(estudiante):
    global asistencia_3, inasistencia_3
    while True:
        opcion = input(f"El estudiante #{estudiante} asistió? [s/n]: ").lower()
        print("")

        if opcion == "s":
            asistencia_3 += 1
            break
        elif opcion == "n":
            inasistencia_3 += 1
            break
        else:
            print("Escriba [s] o [n]")
            continue


def main():
    print("=============================")
    print("===REGISTRO DE ASISTENCIAS===")
    print("=============================\n")

    for seccion in secciones:
        print("----------------------------------")
        print(f"Asistencia de la seccion {seccion}")
        print("----------------------------------\n")
        for dia in range(1, dias):
            print("=========================")
            print(f"Asistencia del dia {dia}")
            print("=========================")

            for estudiante in range(1, estudiantes+1):
            
                if seccion == "A":
                    asistencia_a(estudiante)

                elif seccion == "B":
                    asistencia_b(estudiante)

                elif seccion == "C":
                    asistencia_c(estudiante)

    print("====ASISTENCIA DE TODAS  LAS SECCIONES====\n")
    print(f"La seccion A tuvo: {asistencia_1} asistencias y {inasistencia_1} inasistencias")
    print(f"La seccion b tuvo: {asistencia_2} asistencias y {inasistencia_2} inasistencias")
    print(f"La seccion c tuvo: {asistencia_3} asistencias y {inasistencia_3} inasistencias\n")

    total_a = asistencia_1 + asistencia_2 + asistencia_3
    total_ina = inasistencia_1 + inasistencia_2 + inasistencia_3
    print("----TOTAL DE ASISTENCIAS EN LA UAM----")
    print(f"Hubieron {total_a} asistencias en toda la semana")
    print(f"Hubieron {total_ina} inasistencias en toda la semana")

if __name__ == "__main__":
    main()