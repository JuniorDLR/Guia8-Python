# Caso 6: Registro de ventas de nacatamales en eventos de domingo en la UAM
# Cree un programa que simule la venta de nacatamales durante cuatro domingos consecutivos
# en actividades realizadas en la UAM (como torneos, convivencias o ferias). Por cada domingo,
# se deberá registrar la cantidad de clientes y cuántos nacatamales compró cada uno. El
# programa debe calcular el total vendido por domingo y el acumulado mensual. Utilice bucles
# anidados para domingos y clientes.

def main():
    print("=" * 20)
    print("Registro de ventas de nacatamales en eventos de domingo en la UAM")
    print("=" * 20)

eventos = ["torneos", "convivencia", "ferias"]
cantidaDomingo = 4
totalMensual = 0

for evento in eventos:
    print(f"Nombre evento:  {evento.capitalize()}")
    totalEvento = 0

    for domingo in range(1, cantidaDomingo + 1, 1):
        totalPorDomingo = 0

        print(f"Domingo #{domingo}")
        print("")

        cantidadCliente = int(input("Ingrese la cantidad de cliente: "))
        for cantidad in range(1, cantidadCliente + 1):
            cantidadNacatamales = int(
                input(f"Ingrese la cantidad de nacatamales que compro el cliente {cantidad}: "))
            
            totalPorDomingo += cantidadNacatamales
        print(f"Nacatamales vendidos en el domingo #{domingo}: {totalPorDomingo}")
        totalEvento += totalPorDomingo

    print(f"Nacatamles vendidos en {evento}: {totalEvento}") 
    totalMensual += totalEvento

    

totalMensual = sum(totalPorDomingo)
print(f"Nacatamales vendidos por los 3 eventos: {totalMensual}")

if __name__ == "__main__":
    main()