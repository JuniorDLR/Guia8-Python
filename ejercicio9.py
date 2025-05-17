ingenieria_estable = ingenieria_intermitente = ingenieria_no_acceso = 0
medicina_estable = medicina_intermitente = medicina_no_acceso = 0
marcketing_estable = marcketing_intermitente = marcketing_no_acceso = 0
carreras = ["Ingenieria en sistemas",
            "Medicina",
            "Marcketing"]

def es_numero_entero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

estudiantes = 5

def resumen_ingenieria():
    print("===============================")
    print("======INGENIERIA EN SISTEMAS===")
    print("===============================\n")
    print("Carrera de Ingenieria en Sistemas")
    print(f"[✔]{ingenieria_estable} estudiantes tienen acceso a internet")
    print(f"[-]{ingenieria_intermitente} estudiantes tienes acceso intermitente")
    print(f"[X]{ingenieria_no_acceso} estudiantes no tienen acceso")
    print("")

def resumen_medicina():
    print("====================")
    print("======MEDICINA======")
    print("====================\n")
    print(f"[✔]{medicina_estable} estudiantes tienen acceso a internet")
    print(f"[-]{medicina_intermitente} estudiantes tienes acceso intermitente")
    print(f"[X]{medicina_no_acceso} estudiantes no tienen acceso")
    print("")

def resumne_marcketing():
    print("======================")
    print("======MARCKETING======")
    print("======================\n")
    print(f"[✔]{marcketing_estable} estudiantes tienen acceso a internet")
    print(f"[-]{marcketing_intermitente} estudiantes tienes acceso intermitente")
    print(f"[X]{marcketing_no_acceso} estudiantes no tienen acceso")
    print("")


def encuesta(carrera):
    global marcketing_estable, marcketing_intermitente, marcketing_no_acceso
    global ingenieria_intermitente, ingenieria_estable, ingenieria_no_acceso
    global medicina_no_acceso, medicina_estable, medicina_intermitente
    print("[!] INDIQUE SU TIPO DE ACCESO A INTERNET\n")
    print("1. Acceso estable")
    print("2. Acceso intermitente")
    print("3. No tengo acceso")

    if carrera == "Ingenieria en sistemas":
        
        while True:
            opcion = input("Escriba su opcion(1-3): ").strip()
            print("")
            if opcion == "":
                print("[!]El campo no puede quedar vacío")
                continue
            
            elif es_numero_entero(opcion):
                opcion = int(opcion)
                if opcion == 1:
                    ingenieria_estable += 1
                    break

                elif opcion == 2:
                    ingenieria_intermitente += 1
                    break

                elif opcion == 3:
                    ingenieria_no_acceso += 1
                    break

                else:
                    print("[!]Valor válido")
                    continue

            else:
                print("[!]Indique un valor válido")
                continue

    elif carrera == "Medicina":
        while True:
            opcion = input("Escriba su opcion(1-3): ").strip()
            print("")
            if opcion == "":
                print("[!]El campo no puede quedar vacío")
                print("")
                continue
            
            elif es_numero_entero(opcion):
                opcion = int(opcion)
                if opcion == 1:
                    medicina_estable += 1
                    break

                elif opcion == 2:
                    medicina_intermitente += 1
                    break

                elif opcion == 3:
                    medicina_no_acceso += 1
                    break

                else:
                    print("[!]Valor válido")
                    print("")
                    continue

            else:
                print("[!]Indique un valor válido")
                print("")
                continue

    elif carrera == "Marcketing":
        
        while True:
            opcion = input("Escriba su opcion(1-3): ").strip()
            print("")
            if opcion == "":
                print("[!]El campo no puede quedar vacío")
                print("")
                continue
            
            elif es_numero_entero(opcion):
                opcion = int(opcion)
                if opcion == 1:
                    marcketing_estable += 1
                    break

                elif opcion == 2:
                    marcketing_intermitente += 1
                    break

                elif opcion == 3:
                    marcketing_no_acceso += 1
                    break

                else:
                    print("[!]Valor válido")
                    print("")
                    continue

            else:
                print("[!]Indique un valor válido")
                print("")
                continue

def main():
    print("======================================================")
    print("ENCUESTA SOBRE EL ACCESO A INTERNET DE LOS ESTUDIANTES")
    print("======================================================")
    for carrera in carreras:
        contador = 1
        print("---------------------------------")
        print(f"[!]Carrera de {carrera}")
        print("---------------------------------")
        for estudiante in range (estudiantes):
            print(f"[✔] Estudiante #{contador}")
            contador += 1
            encuesta(carrera)
    resumen_ingenieria()
    resumen_medicina()
    resumne_marcketing()
    print("=========================================")
    print("=======RESUMEN GENERAL DE ENCUESTA=======")
    print("=========================================")
    con_acceso = ingenieria_estable + medicina_estable + marcketing_estable
    acceso_intermitente = ingenieria_intermitente + medicina_intermitente + marcketing_intermitente
    sin_acceso = ingenieria_no_acceso + medicina_no_acceso + marcketing_no_acceso
    print(f"[✔]{con_acceso} estudiantes en total tienen acceso a internet")
    print(f"[-]{acceso_intermitente} estudiantes en total tienen acceso intermitente")
    print(f"[X]{sin_acceso} estudiantes en total no tienen acceso a internet")

if __name__ == "__main__":
    main()