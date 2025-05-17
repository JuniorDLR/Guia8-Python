import random

# Definimos constantes de la feria
DIAS = 3
STANDS_POR_DIA = 4
PRODUCTOS_POR_STAND = 3

def registrar_ventas_stand(dia, stand):
    """Permite registrar ventas de un stand"""
    total_stand = 0
    print(f"\nDía {dia} - Stand {stand}")
    for producto in range(1, PRODUCTOS_POR_STAND + 1):
        # Aquí puedes cambiar por entrada manual si deseas
        monto = float(input(f"Ingrese monto de venta para el producto {producto}: $"))
        total_stand += monto
    return total_stand

def resumen_ventas_dia(dia):
    """Calcula el resumen de ventas de un día completo"""
    total_dia = 0
    for stand in range(1, STANDS_POR_DIA + 1):
        ventas_stand = registrar_ventas_stand(dia, stand)
        print(f"Total ventas Stand {stand}: ${ventas_stand:.2f}")
        total_dia += ventas_stand
    print(f"\nTOTAL DE VENTAS DEL DÍA {dia}: ${total_dia:.2f}")
    return total_dia

def resumen_general_feria():
    """Controla el flujo de toda la feria y muestra el resumen general"""
    total_general = 0
    for dia in range(1, DIAS + 1):
        total_dia = resumen_ventas_dia(dia)
        total_general += total_dia
    print(f"\n********* TOTAL GENERAL DE LA FERIA *********")
    print(f"Total general: ${total_general:.2f}")

# Programa principal
resumen_general_feria()
