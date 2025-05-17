# Caso 6: Registro de ventas de nacatamales en eventos de domingo en la UAM
# Cree un programa que simule la venta de nacatamales durante cuatro domingos consecutivos
# en actividades realizadas en la UAM (como torneos, convivencias o ferias). Por cada domingo,
# se deberá registrar la cantidad de clientes y cuántos nacatamales compró cada uno. El
# programa debe calcular el total vendido por domingo y el acumulado mensual. Utilice bucles
# anidados para domingos y clientes.

print("")
print("----- Registro de ventas de nacatamales en eventos dominicales - UAM -----")
print("")

total_mensual = 0
total_domingo = 0

eventos =["Torneos", "Convivencias", "Ferias"]
eventos1 = [0, 0, 0]

for i in range (3):
        print("El evento del día de hoy es de: ", eventos[i])
        print("")

        for domingo in range(1,5):
            print(f"\n--- Domingo #{domingo} ---")
            print("")
            print("")
            clientes = int(input("Ingrese la cantidad de clientes que compraron nacatamales: "))
            print("")

            for cliente in range(1, clientes + 1):
                
                cantidad = int(input(f"Ingrese cuántos nacatamales compró el cliente #{cliente}: "))
                eventos1[i] += cantidad

total_mensual = sum(eventos1)

print("---Resumen de ventas---")
print("")
print(f"Nacatamales vendidos en Torneos: {eventos1[0]}")
print(f"Nacatamales vendidos en Convivencias: {eventos1[1]}")
print(f"Nacatamales vendidos en Ferias: {eventos1[2]}")
print(f"Total general de nacatamales vendidos en los 3 eventos: {total_mensual}")