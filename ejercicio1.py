# Caso 1: Control de venta de vigorón en feria universitaria UAM
# Desarrolle un programa que permita simular la venta de vigorón durante una feria gastronómica
# organizada en la Universidad Americana, UAM Managua. El sistema debe solicitar la cantidad
# de clientes atendidos y, por cada cliente, cuántas porciones de vigorón compró, junto con el
# precio unitario por porción. El programa debe calcular el total pagado por cada cliente y mostrar
# el total de ventas de toda la feria. Utilice estructuras cíclicas anidadas.


# mapa = {
#     "ventas": {
#         "cantidad": 0,
#         "Clientes": [{"nombre":"junior","cantidad": 0, "precio": 100, "total": 100}],
#     }
# }

def validar_dato(dato, es_entero):
    try:
        if es_entero:
            int(dato)
            return True
        else:
            float(dato)
            return True
    except ValueError:
        return False

def esta_vacio(dato):
    try:
        if dato.strip() == "":
            return True
        return False
    except ValueError:
        return False

def imprimir_registro(registro):
    print("\nRegistro de Clientes")
    total_ventas = 0
    for _, datos_venta in registro.items():
        for cliente in datos_venta["clientes"]:
            subtotal = cliente["cantidad"] * cliente["precio"]
            total_ventas += subtotal
            print(f"Nombre: {cliente['nombre']}")
            print(f"Cantidad: {cliente['cantidad']}")
            print(f"Precio: {cliente['precio']}")
            print(f"Subtotal: {subtotal}")
            print("-" * 20)
    print(f"Total de ventas: {total_ventas}")

def registrar_clientes(cantidad_clientes, clave, campos_cliente, registro):
    print("Registro del cliente\n")
    clave_clientes = "clientes"
    if clave_clientes not in registro[clave]:
        registro[clave][clave_clientes] = []
    for i in range(1, cantidad_clientes + 1):
        print(f"Registro número {i}")
        cliente = {}
        for campo in campos_cliente:
            while True:
                dato = input(f"{campo}: ")
                if esta_vacio(dato):
                    print("No se permiten campos vacíos. ¡Reintente de nuevo!")
                    continue
                if campo == "cantidad":
                    if validar_dato(dato, es_entero=True):
                        cliente[campo] = int(dato)
                    else:
                        print(f"Debe ingresar una {campo} válida.")
                        continue
                elif campo == "precio":
                    if validar_dato(dato, es_entero=False):
                        cliente[campo] = float(dato)
                    else:
                        print(f"Debe ingresar un {campo} válido.")
                        continue
                else:
                    cliente[campo] = dato
                break
        registro[clave][clave_clientes].append(cliente)

def registrar_venta(campos_generales, campos_cliente, registro):
    campo_cantidad = campos_generales[0]
    clave_ventas = "ventas"
    while True:
        cantidad = input(f"Ingrese la {campo_cantidad}: ")
        if esta_vacio(cantidad):
            print("No se permiten campos vacíos. ¡Reintente de nuevo!")
            continue
        if clave_ventas not in registro:
            registro[clave_ventas] = {}
        try:
            cantidad_clientes = int(cantidad)
            registro[clave_ventas]["cantidad_clientes"] = cantidad_clientes
            registrar_clientes(cantidad_clientes, clave_ventas, campos_cliente, registro)
            break
        except ValueError:
            print("Debe ingresar un número válido.")
            continue

def main():
    print("Control de venta de vigorón en feria universitaria UAM\n")
    campos_generales = ["cantidad de clientes"]
    campos_cliente = ["nombre", "cantidad", "precio"]
    registro = {}
    registrar_venta(campos_generales, campos_cliente, registro)
    imprimir_registro(registro)

if __name__ == "__main__":
    main()