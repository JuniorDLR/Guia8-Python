# Caso 10: Control de préstamos en la biblioteca de la UAM
# Desarrolle un programa que permita registrar los préstamos de libros en la biblioteca de la UAM.
# Se trabajará con cuatro categorías de libros (ingeniería, salud, derecho y literatura), cada una
# con tres subcategorías. Por cada subcategoría se registrarán los préstamos de cinco días. El
# sistema debe mostrar el total de préstamos por subcategoría, categoría y el total general
# semanal.

diccionario = {
    "biblioteca": {
        "categoria": {
            "ingenieria": {
                "libro 1": {
                    "titulo": "python",
                    "prestamos": {"dia 1": 0, "dia 2": 0, "dia 3": 0, "dia 4": 0, "dia 5": 0}
                },
                "libro 2": {
                    "titulo": "kotlin",
                    "prestamos": {"dia 1": 0, "dia 2": 0, "dia 3": 0, "dia 4": 0, "dia 5": 0}
                },
                "libro 3": {
                    "titulo": "dart",
                    "prestamos": {"dia 1": 0, "dia 2": 0, "dia 3": 0, "dia 4": 0, "dia 5": 0}
                }
            },
            "salud": {
                "libro 1": {
                    "titulo": "La Ciudadela",
                    "prestamos": {"dia 1": 0, "dia 2": 0, "dia 3": 0, "dia 4": 0, "dia 5": 0}
                },
                "libro 2": {
                    "titulo": "Morfina",
                    "prestamos": {"dia 1": 0, "dia 2": 0, "dia 3": 0, "dia 4": 0, "dia 5": 0}
                },
                "libro 3": {
                    "titulo": "Los renglones torcidos de Dios",
                    "prestamos": {"dia 1": 0, "dia 2": 0, "dia 3": 0, "dia 4": 0, "dia 5": 0}
                }
            },
            "derecho": {
                "libro 1": {
                    "titulo": "El Contrato Social",
                    "prestamos": {"dia 1": 0, "dia 2": 0, "dia 3": 0, "dia 4": 0, "dia 5": 0}
                },
                "libro 2": {
                    "titulo": "El proceso de Franz Kafka",
                    "prestamos": {"dia 1": 0, "dia 2": 0, "dia 3": 0, "dia 4": 0, "dia 5": 0}
                },
                "libro 3": {
                    "titulo": "Historia del Derecho Romano de Ricardo Levene",
                    "prestamos": {"dia 1": 0, "dia 2": 0, "dia 3": 0, "dia 4": 0, "dia 5": 0}
                }
            },
            "literatura": {
                "libro 1": {
                    "titulo": "Cien años de soledad",
                    "prestamos": {"dia 1": 0, "dia 2": 0, "dia 3": 0, "dia 4": 0, "dia 5": 0}
                },
                "libro 2": {
                    "titulo": "Don Quijote de la Mancha",
                    "prestamos": {"dia 1": 0, "dia 2": 0, "dia 3": 0, "dia 4": 0, "dia 5": 0}
                },
                "libro 3": {
                    "titulo": "Orgullo y prejuicio",
                    "prestamos": {"dia 1": 0, "dia 2": 0, "dia 3": 0, "dia 4": 0, "dia 5": 0}
                }
            }
        }
    }
}

def mostrar_libros(diccionario):
    if "biblioteca" in diccionario:
        print("Libros disponibles:")
        categorias = diccionario["biblioteca"]["categoria"]
        for categoria, libros in categorias.items():
            print(f"\nCategoría: {categoria.capitalize()}")
            for libro, detalles in libros.items():
                print(f"  - {libro}: {detalles['titulo']}")

def registrar_prestamos(diccionario):
    categoria = input("\nSeleccione una categoría: ").lower()
    if categoria in diccionario["biblioteca"]["categoria"]:
        libros = diccionario["biblioteca"]["categoria"][categoria]
        libro = input("Seleccione un libro (ejemplo: libro 1): ").lower()
        if libro in libros:
            for dia in libros[libro]["prestamos"]:
                prestamos = int(input(f"Ingrese el número de préstamos para {dia}: "))
                libros[libro]["prestamos"][dia] += prestamos
        else:
            print("Libro no encontrado.")
    else:
        print("Categoría no encontrada.")

def mostrar_totales(diccionario):
    total_general = 0
    print("\nTotales de préstamos:")
    categorias = diccionario["biblioteca"]["categoria"]
    for categoria, libros in categorias.items():
        total_categoria = 0
        print(f"\nCategoría: {categoria.capitalize()}")
        for libro, detalles in libros.items():
            total_libro = sum(detalles["prestamos"].values())
            total_categoria += total_libro
            print(f"  - {detalles['titulo']}: {total_libro} préstamos")
        total_general += total_categoria
        print(f"Total categoría {categoria.capitalize()}: {total_categoria} préstamos")
    print(f"\nTotal general semanal: {total_general} préstamos")

def main():
    while True:
        print("\nMenú:")
        print("1. Mostrar libros")
        print("2. Registrar préstamos")
        print("3. Mostrar totales")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_libros(diccionario)
        elif opcion == "2":
            registrar_prestamos(diccionario)
        elif opcion == "3":
            mostrar_totales(diccionario)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()