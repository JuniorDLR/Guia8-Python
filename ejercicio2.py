# Caso 2: Registro semanal de gastos de estudiantes UAM
# Cree un programa que simule el control de gastos semanales de un grupo de estudiantes de
# primer año de la UAM. El sistema debe procesar datos de 4 semanas, y por cada semana,
# ingresar el gasto realizado cada día (7 días por semana). El programa debe calcular el total
# gastado por semana y el total acumulado del mes. Utilice bucles anidados para recorrer
# semanas y días.


estudiantes = {
    "estudiantes": [
        {
            "nombre": "Junior",
            "gastos": {
                "semana 1": {
                    "dia 1": 100,
                    "dia 2": 100,
                    "dia 3": 200,
                    "dia 4": 200,
                    "dia 5": 500,
                    "dia 6": 200,
                    "dia 7": 100,
                },
                "semana 2": {
                    "dia 1": 150,
                    "dia 2": 200,
                    "dia 3": 250,
                    "dia 4": 300,
                    "dia 5": 350,
                    "dia 6": 400,
                    "dia 7": 450,
                },
                
            },
            "gastoSemanal": {
                "semana 1":200,
                "semana 2":200,
                "semana 3":200,
                "semana 4":200,
            },  
            "gastoMensual": 50000,   
        },
    ]
}

def cantidad_estudiantes():
    while True:
        cantidad = input("Ingrese la cantidad de estudiantes de un grupo: ")

        if cantidad.strip() == "":
            print("No se permite campos vacios!")
            continue
        else:
            try:
                cantidadEntera = int(cantidad)
                return cantidadEntera
            except ValueError:
                print("Debes de ingresar un numero valido!")
                continue


def isEmpty(nombre):
    if nombre.strip() == "":
        return True
    else:
        return False


def registro_estudiante(encabezadoSemana, encabezadoDia, diccionario, cantidad):

    nombre_dict = {
    "nombre": "",
    "gastos": {},  
    "gastoSemanal": {},  
    "gastoMensual": 0,   
}

    clavePrincipal = "estudiantes"
    if clavePrincipal not in diccionario:
        diccionario[clavePrincipal] = []

    for estudiante in range(1, cantidad + 1, 1):
        print(f"Registro del estudiante {estudiante} \n")
        nombre = {}
        while True:
            nombre = input("Ingrese el nombre del estudiante: ")
            if isEmpty(nombre=nombre):
                print("Debes de ingresar un nombre valido!")
                continue
            else:
                nombre_dict["nombre"] = nombre
                break

        for semana in encabezadoSemana:
            diccionario_gasto = {}
            for dia in encabezadoDia:
                while True:
                    gasto = input(f"Ingrese el gasto de la {semana} del {dia}: ")

                    if isEmpty(gasto):
                        print("No se permiten campos vacios!")
                        continue
                    else:
                        try:
                            convertirFloat = float(gasto)
                            diccionario_gasto[dia] = convertirFloat
                            break
                        except ValueError:
                            print("Debes de ingresar un numero valido!")
                            continue
            nombre_dict["gastos"][semana] = diccionario_gasto
            nombre_dict["gastoSemanal"][semana] = sum(diccionario_gasto.values())

        nombre_dict["gastoMensual"] = sum(nombre_dict["gastoSemanal"].values())
        diccionario[clavePrincipal].append(nombre_dict)




def mostrar_gastos_por_semana(diccionario):
    if "estudiantes" in diccionario:
        for estudiante in diccionario["estudiantes"]:
            print(f"Estudiante: {estudiante['nombre']}")
            print("Gastos por semana:")
            print("-" * 30)
            
            # Mostrar los gastos por semana
            for semana, dias in estudiante["gastos"].items():
                print(f"{semana}:")
                for dia, gasto in dias.items():
                    print(f"  {dia}: {gasto}")
                print(f"  Total {semana}: {estudiante['gastoSemanal'][semana]}")
                print("-" * 30)
            
            # Mostrar el gasto mensual total
            print(f"Gasto total del mes: {estudiante['gastoMensual']}")
            print("=" * 50)
    else:
        print("No hay estudiantes registrados.")

def main():

    encabezadoSemana = ["semana 1", "semana 2", "semana 3", "semana 4"]
    encabezadoDia = ["dia 1", "dia 2", "dia 3", "dia 4", "dia 5", "dia 6", "dia 7"]
    diccionario = {}

    print("Registro semanal de gastos de estudiantes UAM\n")

    cantidad = cantidad_estudiantes()
    registro_estudiante(encabezadoSemana, encabezadoDia, diccionario, cantidad)
    mostrar_gastos_por_semana(diccionario)


if __name__ == "__main__":
    main()
