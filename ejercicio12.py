import random

# Definimos constantes
FILAS = 5
COLUMNAS = 4
LABORATORIOS = 2

def crear_laboratorio():
    """Crea un laboratorio con computadoras aleatoriamente ocupadas o libres"""
    laboratorio = []
    for fila in range(FILAS):
        fila_computadoras = []
        for columna in range(COLUMNAS):
            # 0: libre, 1: ocupada
            estado = random.choice([0, 1])
            fila_computadoras.append(estado)
        laboratorio.append(fila_computadoras)
    return laboratorio

def mostrar_laboratorio(laboratorio, numero):
    """Muestra el estado del laboratorio"""
    print(f"\nLaboratorio {numero}:")
    for fila in laboratorio:
        for computadora in fila:
            simbolo = 'O' if computadora == 1 else 'L'
            print(simbolo, end=' ')
        print()

def resumen_laboratorio(laboratorio):
    """Calcula el resumen de ocupadas y libres"""
    ocupadas = 0
    libres = 0
    for fila in laboratorio:
        for computadora in fila:
            if computadora == 1:
                ocupadas += 1
            else:
                libres += 1
    return ocupadas, libres

# Programa principal
laboratorios = []
for i in range(LABORATORIOS):
    laboratorio = crear_laboratorio()
    laboratorios.append(laboratorio)
    mostrar_laboratorio(laboratorio, i + 1)
    ocupadas, libres = resumen_laboratorio(laboratorio)
    print(f"Computadoras ocupadas: {ocupadas}")
    print(f"Computadoras libres: {libres}")
