#Resultado de encuentas de facultad de FIA
Fia = Fia_moto = Fia_bus = Fia_taxi = Fia_caminando = Fia_bici = 0
#Resultado de encuestas de facultad de FCM
Fcm = Fcm_moto = Fcm_bus = Fcm_taxi = Fcm_caminando = Fcm_bici = 0
#Resultado de encuestas de facultad de Fae
Fcae = Fcae_moto = Fcae_bus = Fcae_taxi = Fcae_caminando = Fcae_bici = 0
Facultades = {
    "Facultad_Fia": ["Arquitectura", "Ingenieria en sistemas"],
    "Facultad_Ciencias_Medicas":["Medicina","Nutricion"],
    "Facultad_Administrativas_Economicas":["Economia", "Contabilidad"]
}
Estudiantes = 5

def es_numero_entero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def resumen_total():
    Total_bus = Fia_bus + Fcm_bus + Fcae_bus
    Total_moto = Fia_moto + Fcm_moto + Fcae_moto
    total_bici = Fia_bici + Fcm_bici + Fcae_bici
    Total_taxi = Fia_taxi + Fcm_taxi + Fcae_taxi
    Total_caminando = Fia_caminando + Fcm_caminando + Fcae_caminando
    print("=============================")
    print("=======Resumen General=======")
    print("=============================")
    print(f"En total {Total_bus} estudiantes viajan en bus")
    print(f"En total {total_bici} estudinte viajan en bicicleta")
    print(f"En total {Total_caminando} estudiantes viajan caminando")
    print(f"En total {Total_moto} estudiantes viajan en motocicleta")
    print(f"En total {Total_taxi} estudiantes viajan en taxi")
    print("\n")

def resumen_fia():
    print("=========================================================")
    print("===Resumen de la facultad de Ingenieria y arquitectura===")
    print("=========================================================")
    print(f"{Fia_moto} estudiantes viajan en moto")
    print(f"{Fia_bus} estudiantes viajan en autobus")
    print(f"{Fia_taxi} estudiantes viajan en taxi")
    print(f"{Fia_caminando} estudiantes viajan caminando")
    print(f"{Fia_bici} estudiantes viajan en bici")
    print("\n")

def resumen_fcm():
    print("=========================================================")
    print("===Resumen de la facultad de Ciencias Medicas===")
    print("=========================================================")
    print(f"{Fcm_moto} estudiantes viajan en moto")
    print(f"{Fcm_bus} estudiantes viajan en autobus")
    print(f"{Fcm_taxi} estudiantes viajan en taxi")
    print(f"{Fcm_caminando} estudiantes viajan caminando")
    print(f"{Fcm_bici} estudiantes viajan en bici")
    print("\n")

def resumen_fcae():
    print("==================================================================")
    print("===Resumen de la facultad Ciencias Administrativas y Económicas===")
    print("==================================================================")
    print(f"{Fcae_moto} estudiantes viajan en moto")
    print(f"{Fcae_bus} estudiantes viajan en autobus")
    print(f"{Fcae_taxi} estudiantes viajan en taxi")
    print(f"{Fcae_caminando} estudiantes viajan caminando")
    print(f"{Fcae_bici} estudiantes viajan en bici")
    print("\n")


def encuesta_fcae():
    global Fcae_moto, Fcae_bici, Fcae_caminando, Fcae_taxi, Fcae_bus
    print("")
    print("Indique el medio de transporte que utiliza\n")
    print("1. Bicicleta")
    print("2. Motocicleta")
    print("3. Taxi")
    print("4. Bus")
    print("5. Caminando")
    opc = int(input("Escriba su opcion: "))
    print("")
    while True:
        if es_numero_entero(opc):
            if opc == 1:
                Fcae_bici += 1
                break
            elif opc == 2:
                Fcae_moto += 1
                break
            elif opc == 3:
                Fcae_taxi += 1
                break
            elif opc == 4:
                Fcae_bus += 1
                break
            elif opc == 5:
                Fcae_caminando += 1
                break
        print("Ingrese un valor válido")
        continue

def encuesta_fcm():
    global Fcm_moto, Fcm_bici, Fcm_caminando, Fcm_taxi, Fcm_bus
    print("")
    print("Indique el medio de transporte que utiliza\n")
    print("1. Bicicleta")
    print("2. Motocicleta")
    print("3. Taxi")
    print("4. Bus")
    print("5. Caminando")
    opc = int(input("Escriba su opcion: "))
    print("")
    while True:
        if es_numero_entero(opc):
            if opc == 1:
                Fcm_bici += 1
                break
            elif opc == 2:
                Fcm_moto += 1
                break
            elif opc == 3:
                Fcm_taxi += 1
                break
            elif opc == 4:
                Fcm_bus += 1
                break
            elif opc == 5:
                Fcm_caminando += 1
                break
        print("Ingrese un valor válido")
        continue

def encuesta_fia():
    global Fia_moto, Fia_bici, Fia_caminando, Fia_taxi, Fia_bus
    print("")
    print("Indique el medio de transporte que utiliza\n")
    print("1. Bicicleta")
    print("2. Motocicleta")
    print("3. Taxi")
    print("4. Bus")
    print("5. Caminando")
    opc = int(input("Escriba su opcion: "))
    print("")
    while True:
        if es_numero_entero(opc):
            if opc == 1:
                Fia_bici += 1
                break
            elif opc == 2:
                Fia_moto += 1
                break
            elif opc == 3:
                Fia_taxi += 1
                break
            elif opc == 4:
                Fia_bus += 1
                break
            elif opc == 5:
                Fia_caminando += 1
                break
        print("Ingrese un valor válido")
        continue
def main():
    print("===============================================")
    print("ENCUESTA SOBRE EL MEDIO DE TRANSPORTE EN LA UAM")
    print("===============================================")

    for facultad, carreras in Facultades.items():
        print(f"\nEstudiantes de la {facultad} ")
        for carrera in carreras:
            print(f"[!]Estudiantes de la carrera de {carrera}")
            for estudiante in range (1, Estudiantes + 1):
                if carrera == "Arquitectura" or carrera == "Ingenieria en sistemas":
                    print(f"[✔]Estudiante numero {estudiante}")
                    encuesta_fia()
                elif carrera == "Medicina"or carrera == "Nutricion":
                    print(f"[✔]Estudiante numero {estudiante}")
                    encuesta_fcm()
                elif carrera == "Economia" or carrera == "Contabilidad":
                    print(f"[✔]Estudiante numero {estudiante}")
                    encuesta_fcae()
    resumen_fia()
    resumen_fcm()
    resumen_fcae()
    resumen_total()

    print("==================================")
    print("GRACIAS POR UTILIZAR ESTE PROGRAMA")
    print("==================================")
if __name__ == "__main__":
    main()