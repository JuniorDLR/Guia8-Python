kw_biblioteca = kw_administracion = kw_cafeteria = kw_laboratorio = kw_auditorio = 0

edificios = ["Biblioteca","Administracion","Cafeteria","Laboratorio","Auditorio central"]

turnos = ["matutino","vespertino","nocturno"]

def es_numero_flotante(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False
    
def registro(edificio):
    global kw_biblioteca, kw_administracion, kw_cafeteria, kw_laboratorio, kw_auditorio
    while True:
        if edificio == "Biblioteca":
            energia = input("Ingrese el consumo de electricidad: ").strip()
            print("")
            if energia == "":
                print("El campo no puede quedar vacío")
                continue
            elif es_numero_flotante(energia):
                energia = float(energia)
                kw_biblioteca += energia
                break
            else:
                print("Ingrese un valor válido")
                continue

        elif edificio == "Administracion":
            energia = input("Ingrese su consumo de electricidad: ").strip()
            print("")
            if energia == "":
                print("El campo no puede quedar vacío")
                continue
            elif es_numero_flotante(energia):
                energia = float(energia)
                kw_administracion += energia
                break
            else:
                print("Ingrese un valor válido")
                continue

        elif edificio == "Cafeteria":
            energia = input("Ingrese su consumo de electricidad: ").strip()
            print("")
            if energia == "":
                print("El campo no puede quedar vacío")
                continue
            elif es_numero_flotante(energia):
                energia = float(energia)
                kw_cafeteria += energia
                break
            else:
                print("Ingrese un valor válido")
                continue

        elif edificio == "Laboratorio":
            energia = input("Ingrese su consumo de electricidad: ").strip()
            print("")
            if energia == "":
                print("El campo no puede quedar vacío")
                continue
            elif es_numero_flotante(energia):
                energia = float(energia)
                kw_laboratorio += energia
                break
            else:
                print("Ingrese un valor válido")
                continue

        elif edificio == "Auditorio central":
            energia = input("Ingrese su consumo de electricidad: ").strip()
            print("")
            if energia == "":
                print("El campo no puede quedar vacío")
                continue
            elif es_numero_flotante(energia):
                energia = float(energia)
                kw_auditorio += energia
                break
            else:
                print("Ingrese un valor válido")
                continue
def main():
    for i in range(1, 2):
        print("======================================")
        print(F"===============DIA {i}================")
        print("=====REGISTRO DE ELECTRICIDAD UAM=====")
        print("======================================")
        for edificio in edificios:
            print("---------------------------")
            print(f"Edificio de {edificio}")
            print("---------------------------")
            print("")
            for turno in turnos:
                print(f"[!]Registro de electricidad, turno {turno}")
                print("")
                registro(edificio)
    print("==========================================")
    print("=====CONSUMO SEMANAL DE CADA EDIFICIO=====")
    print("==========================================")
    print(f"[✔]El edificio de la Biblioteca consumió: {kw_biblioteca:.2f} kilowatts")
    print(f"[✔]El edificio de Administración consumió: {kw_administracion:.2f} kilowatts")
    print(f"[✔]El edificio de Cafeteria consumió: {kw_cafeteria:.2f} kilowatts")
    print(f"[✔]El edificio del Laboratorio consumió: {kw_laboratorio:.2f} kilowatts")
    print(f"[✔]El edificio del Auditorio Central consumió: {kw_auditorio:.2f} kilowatts\n")

    print("=======================================")
    print("CONSUMO TOTAL DE ELECTRICIDAD DE LA UAM")
    print("=======================================")
    kw_Total = kw_biblioteca + kw_administracion + kw_cafeteria + kw_laboratorio + kw_auditorio
    print(f"[✔]La universidad UAM consumió {kw_Total:.2f} kilowatts en toda la semana")

if __name__ == "__main__":
    main()