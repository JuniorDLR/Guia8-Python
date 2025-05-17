total_helado_1 = 0
total_pizzas_1 = 0
total_cafe_1 = 0



Kioskos = {
    "Kiosko de cafe": {
        "capuchino": 130,
        "mocachino": 90,
        "café especial": 110,
        "café con leche": 100,
        "café negro": 120
    },
    "Kiosko de helados":{
        "Napolitano": 30,
        "Vainilla": 40,
        "Chocolate": 35,
        "Chicle": 25,
        "Fresa": 45
    },
    "Kiosko de pizzas":{
        "Jamon":180,
        "Pepperoni": 190,
        "Hawaiana": 200,
        "Suprema": 220,
        "carnuda": 250
    },
}
def kiosko_pizzas():
    global total_pizzas_1
    print("-----------------------------")
    print("----Menú kiosko de pizzas----")
    print("-----------------------------")
    count = 1
    for pizza, precio in Kioskos["Kiosko de pizzas"].items():
        print(f"{count}. {pizza} cuesta : {precio}")
        count += 1

    while True:
        opc = input("Que pizza desea comprar?: ")
        if es_numero_entero(opc):
            opc = int(opc)
            if opc == 1:
                print("Usted seleccionó pizza de jamón, cuesta 180")
                print("")
                total_pizzas_1 += 180
                    
                condicion = input("Desea comprar otra pizza? [S] si, [N] no: ")

                if condicion.lower() == "s":
                    continue

                elif condicion.lower() == "n":
                    condicion2 = input("Desea comprar en otro kiosko? [S] si, [N] no: ")

                    if condicion2.lower() == "s":
                        orden()
                        break

                    elif condicion2.lower() == "n":
                        break
                    else:
                        print("Respuesta no válida")
                        continue
                else:
                    print("Respuesta no válida")
                    continue
            elif opc == 2:
                print("Usted seleccionó pizza de pepperoni, cuesta 190")
                print("")
                total_pizzas_1 += 190
                    
                condicion = input("Desea comprar otra pizza? [S] si, [N] no: ")

                if condicion.lower() == "s":
                    continue

                elif condicion.lower() == "n":
                    condicion2 = input("Desea comprar en otro kiosko? [S] si, [N] no: ")

                    if condicion2.lower() == "s":
                        orden()
                        break

                    elif condicion2.lower() == "n":
                        break
                    else:
                        print("Respuesta no válida")
                        continue
                else:
                    print("Respuesta no válida")
                    continue
            elif opc == 3:
                print("Usted seleccionó pizza hawaiana, cuesta 200")
                print("")
                total_pizzas_1 += 200
                    
                condicion = input("Desea comprar otra pizza? [S] si, [N] no: ")

                if condicion.lower() == "s":
                    continue

                elif condicion.lower() == "n":
                    condicion2 = input("Desea comprar en otro kiosko? [S] si, [N] no: ")

                    if condicion2.lower() == "s":
                        orden()
                        break

                    elif condicion2.lower() == "n":
                        break
                    else:
                        print("Respuesta no válida")
                        continue
                else:
                    print("Respuesta no válida")
                    continue
            elif opc == 4:
                print("Usted seleccionó pizza suprema, cuesta 220")
                print("")
                total_pizzas_1 += 220
                    
                condicion = input("Desea comprar otra pizza? [S] si, [N] no: ")

                if condicion.lower() == "s":
                    continue

                elif condicion.lower() == "n":
                    condicion2 = input("Desea comprar en otro kiosko? [S] si, [N] no: ")

                    if condicion2.lower() == "s":
                        orden()
                        break

                    elif condicion2.lower() == "n":
                        break
                    else:
                        print("Respuesta no válida")
                        continue
                else:
                    print("Respuesta no válida")
                    continue
            elif opc == 5:
                print("Usted seleccionó pizza carnuda, cuesta 250")
                print("")
                total_pizzas_1 += 250
                    
                condicion = input("Desea comprar otra pizza? [S] si, [N] no: ")

                if condicion.lower() == "s":
                    continue

                elif condicion.lower() == "n":
                    condicion2 = input("Desea comprar en otro kiosko? [S] si, [N] no: ")

                    if condicion2.lower() == "s":
                        orden()
                        break

                    elif condicion2.lower() == "n":
                        break
                    else:
                        print("Respuesta no válida")
                        continue
                else:
                    print("Respuesta no válida")
                    continue
            else:
                print("Ingrese un numero válido")
                continue

        print("Ingrese un valor válido")
        continue

def kiosko_helados():
    global total_helado_1
    print("------------------------------")
    print("----Menú kiosko de helados----")
    print("------------------------------")
    count = 1
    for helado, precio in Kioskos["Kiosko de helados"].items():
        print(f"{count}. {helado} cuesta : {precio}")
        count += 1

    while True:
        opc = input("Que helado desea comprar?: ")

        if es_numero_entero(opc):
            opc = int(opc)
            if opc == 1:
                print("Usted seleccionó napolitano, cuesta 30")
                print("")
                total_helado_1 += 30
                    
                condicion = input("Desea comprar otro helado? [S] si, [N] no: ")

                if condicion.lower() == "s":
                    continue

                elif condicion.lower() == "n":
                    condicion2 = input("Desea comprar en otro kiosko? [S] si, [N] no: ")

                    if condicion2.lower() == "s":
                        orden()
                        break

                    elif condicion2.lower() == "n":
                        break
                    else:
                        print("Respuesta no válida")
                        continue
                else:
                    print("Respuesta no válida")
                    continue
            elif opc == 2:
                print("Usted seleccionó vainilla, cuesta 40")
                print("")
                total_helado_1 += 40
                    
                condicion = input("Desea comprar otro helado? [S] si, [N] no: ")

                if condicion.lower() == "s":
                    continue

                elif condicion.lower() == "n":
                    condicion2 = input("Desea comprar en otro kiosko? [S] si, [N] no: ")

                    if condicion2.lower() == "s":
                        orden()
                        break

                    elif condicion2.lower() == "n":
                        break
                    else:
                        print("Respuesta no válida")
                        continue
                else:
                    print("Respuesta no válida")
                    continue
            elif opc == 3:
                print("Usted seleccionó chocolate, cuesta 35")
                print("")
                total_helado_1 += 35
                    
                condicion = input("Desea comprar otro helado? [S] si, [N] no: ")

                if condicion.lower() == "s":
                    continue

                elif condicion.lower() == "n":
                    condicion2 = input("Desea comprar en otro kiosko? [S] si, [N] no: ")

                    if condicion2.lower() == "s":
                        orden()
                        break

                    elif condicion2.lower() == "n":
                        break
                    else:
                        print("Respuesta no válida")
                        continue
                else:
                    print("Respuesta no válida")
                    continue
            elif opc == 4:
                print("Usted seleccionó chicle, cuesta 25")
                print("")
                total_helado_1 += 25
                    
                condicion = input("Desea comprar otro helado? [S] si, [N] no: ")

                if condicion.lower() == "s":
                    continue

                elif condicion.lower() == "n":
                    condicion2 = input("Desea comprar en otro kiosko? [S] si, [N] no: ")

                    if condicion2.lower() == "s":
                        orden()
                        break

                    elif condicion2.lower() == "n":
                        break
                    else:
                        print("Respuesta no válida")
                        continue
                else:
                    print("Respuesta no válida")
                    continue
            elif opc == 5:
                print("Usted seleccionó fresa, cuesta 45")
                print("")
                total_helado_1 += 45

                condicion = input("Desea comprar otro helado? [S] si, [N] no: ")

                if condicion.lower() == "s":
                    continue

                elif condicion.lower() == "n":
                    condicion2 = input("Desea comprar en otro kiosko? [S] si, [N] no: ")

                    if condicion2.lower() == "s":
                        orden()
                        break

                    elif condicion2.lower() == "n":
                        break
                    else:
                        print("Respuesta no válida")
                        continue
                else:
                    print("Respuesta no válida")
                    continue
            print("Ingrese un numero válido")
            continue
        print("Ingrese un valor válido")
        continue

def kiosko_cafe():
    global total_cafe_1
    print("----------------------------")
    print("----Menú kiosko de cafés----")
    print("----------------------------")
    count = 1
    for cafe, precio in Kioskos["Kiosko de cafe"].items():
        print(f"{count}. {cafe} cuesta : {precio}")
        count += 1

    while True:
        opc = input("Que café desea comprar?: ")

        if es_numero_entero(opc):
            opc = int(opc)
            if opc == 1:
                print("Usted seleccionó capuchino, cuesta 130")
                print("")
                total_cafe_1 = total_cafe_1 + 130
                
                condicion = input("Desea comprar otro café? [S] si, [N] no: ")

                if condicion.lower() == "s":
                    continue

                elif condicion.lower() == "n":
                    condicion2 = input("Desea comprar en otro kiosko? [S] si, [N] no: ")

                    if condicion2.lower() == "s":
                        orden()
                        break

                    elif condicion2.lower() == "n":
                        break
                    else:
                        print("Respuesta no válida")
                        continue
                else:
                    print("Respuesta no válida") 
                    continue               
            elif opc == 2:
                print("Usted seleccionó mocachino, cuesta 90")
                print("")
                total_cafe_1 = total_cafe_1 + 90
                
                condicion = input("Desea comprar otro café? [S] si, [N] no: ")

                if condicion.lower() == "s":
                    continue

                elif condicion.lower() == "n":
                    condicion2 = input("Desea comprar en otro kiosko? [S] si, [N] no: ")

                    if condicion2.lower() == "s":
                        orden()
                        break

                    elif condicion2.lower() == "n":
                        break
                    else:
                        print("Respuesta no válida")
                        continue
                else:
                    print("Respuesta no válida")
                    continue
            elif opc == 3:
                print("Usted seleccionó cafe especial, cuesta 110")
                print("")
                total_cafe_1 = total_cafe_1 + 110
                
                condicion = input("Desea comprar otro café? [S] si, [N] no: ")

                if condicion.lower() == "s":
                    continue

                elif condicion.lower() == "n":
                    condicion2 = input("Desea comprar en otro kiosko? [S] si, [N] no: ")

                    if condicion2.lower() == "s":
                        orden()
                        break

                    elif condicion2.lower() == "n":
                        break
                    else:
                        print("Respuesta no válida")
                        continue
                else:
                    print("Respuesta no válida")
                    continue
            elif opc == 4:
                print("Usted seleccionó cafe con leche, cuesta 100")
                print("")
                total_cafe_1 = total_cafe_1 + 100

                condicion = input("Desea comprar otro café? [S] si, [N] no: ")

                if condicion.lower() == "s":
                    continue

                elif condicion.lower() == "n":
                    condicion2 = input("Desea comprar en otro kiosko? [S] si, [N] no: ")

                    if condicion2.lower() == "s":
                        orden()
                        break

                    elif condicion2.lower() == "n":
                        break
                    else:
                        print("Respuesta no válida")
                        continue
                else:
                    print("Respuesta no válida")
                    continue
            elif opc == 5:
                print("Usted seleccionó cafe negro, cuesta 120")
                print("")
                total_cafe_1 = total_cafe_1 + 120
                
                condicion = input("Desea comprar otro café? [S] si, [N] no: ")

                if condicion.lower() == "s":
                    continue

                elif condicion.lower() == "n":
                    condicion2 = input("Desea comprar en otro kiosko? [S] si, [N] no: ")

                    if condicion2.lower() == "s":
                        orden()
                        break

                    elif condicion2.lower() == "n":
                        break
                    else:
                        print("Respuesta no válida")
                        continue
                else:
                    print("Respuesta no válida")
                    continue
            print("Ingrese un numero válido")
            continue
        print("Ingrese un valor válido")
        continue

def es_numero_entero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False
    
def orden():
    print("")
    print("[!]Porfavor indíque  en que kiosko desee comprar\n")
    print("1. Kiosko de café")
    print("2. Kiosko de helados")
    print("3. Kiosko de pizzas")
    print("4. Terminar dia")
    while True:
        opc = input("Escriba su opcion(1-4): ")
        if es_numero_entero(opc):
            opc = int(opc)
            if opc == 1:
                kiosko_cafe()
                break
            elif opc == 2:
                kiosko_helados()
                break
            elif opc == 3:
                kiosko_pizzas()
                break
            elif opc == 4:
                break
            else:
                print("Numero no válido")
                continue
        else:
            print("[!]Ingrese un numero válido")
            continue

def main():
    global total_pizzas_1, total_cafe_1, total_helado_1
    for i in range(1, 5, 1):
        total_helado_1 = total_cafe_1 = total_pizzas_1 = 0
        print("================================")
        print(f"=============DIA {i}=============")
        print("====Bienvenido a metrocentro====")
        print("================================")
        orden()
        
        print(f"=====Ventas del dia {i}=====")
        print("Ganancias total del kiosko de café: ", total_cafe_1)
        print("Ganancias total del kiosko de helado: ", total_helado_1)
        print("Ganancias total del kiosko de pizzas: ", total_pizzas_1)
    print("====GRACIAS POR UTILIZAR ESTE PROGRAMA====")
if __name__ == "__main__":
    main()

