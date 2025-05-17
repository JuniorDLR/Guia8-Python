edificio_c = edificio_a = edificio_b = edificio_d = 0

edificios_uam = ["Edificio A","Edificio B","Edificio C","Edificio D"]
turnos = ["matutino","vespertino","nocturno"]

def es_numero_flotante(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def monitoreo(edificio):
    global edificio_c, edificio_a, edificio_b, edificio_d
    while True:
        if edificio == "Edificio A":
            energia = input("Ingrese el consumo de electricidad: ").strip()
            print("")
            if energia == "":
                print("El campo no puede quedar vacío")
                continue
            elif es_numero_flotante(energia):
                energia = float(energia)
                edificio_a += energia
                break
            else:
                print("Ingrese un valor válido")
                continue

        elif edificio == "Edificio B":
            energia = input("Ingrese el consumo de electricidad: ").strip()
            print("")
            if energia == "":
                print("El campo no puede quedar vacío")
                continue
            elif es_numero_flotante(energia):
                energia = float(energia)
                edificio_b += energia
                break
            else:
                print("Ingrese un valor válido")
                continue

        elif edificio == "Edificio C":
            energia = input("Ingrese el consumo de electricidad: ").strip()
            print("")
            if energia == "":
                print("El campo no puede quedar vacío")
                continue
            elif es_numero_flotante(energia):
                energia = float(energia)
                edificio_c += energia
                break
            else:
                print("Ingrese un valor válido")
                continue

        elif edificio == "Edificio D":
            energia = input("Ingrese el consumo de electricidad: ").strip()
            print("")
            if energia == "":
                print("El campo no puede quedar vacío")
                continue
            elif es_numero_flotante(energia):
                energia = float(energia)
                edificio_d += energia
                break
            else:
                print("Ingrese un valor válido")
                continue

def main():
    for i in range(1, 2):
        print("======================================")
        print(F"===============DIA {i}===============")
        print("===MONITOREO DEL CONSUMO ENERGETICO===")
        print("======================================")
        
        for edificio in edificios_uam:
            print("==============")
            print(f"=={edificio}==")
            print("==============\n")

            for turno in turnos:
                print(f"[!]Monitoreo del turno {turno}")
                monitoreo(edificio)
    
    print("==========================================")
    print("=====CONSUMO SEMANAL DE CADA EDIFICIO=====")
    print("==========================================")
    print(f"[✔]El edificio A consumió: {edificio_a:.2f} kilovatios")
    print(f"[✔]El edificio B consumió: {edificio_b:.2f} kilovatios")
    print(f"[✔]El edificio C consumió: {edificio_c:.2f} kilovatios")
    print(f"[✔]El edificio D consumió: {edificio_d:.2f} kilovatios\n")

    print("===================================")
    print("CONSUMO TOTAL DE ENERGIA EN LA UAM")
    print("===================================\n")
    energia_promedio = (edificio_c + edificio_a + edificio_b + edificio_d) / 7
    energia_total = edificio_c + edificio_a + edificio_b + edificio_d
    print(f"[✔]La universidad UAM consumió {energia_total:.3f} kilovatios en toda la semana\n")
    print(f"[!]La universidad UAM consume un promedio de {energia_promedio:.3f} kilovatios por dia")

if __name__ == "__main__":
    main()