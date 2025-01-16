print("PT01 - Diseño y desarrollo de software")

def main():
    while True:
        print("\nMenú:")
        print("1. Suma de \"n\" números (positivos y negativos)")
        print("2. Producto entre \"n\" números")
        print("3. División entre 2 números")
        print("4. Calcular el factorial (n!) del número indicado")
        print("5. Imprimir las tablas de multiplicar (1 al 10)")
        print("6. Calcular el cuadrado y cubo de un número")
        print("7. Determinar el promedio de una serie de números (-1 para detener)")
        print("8. Encontrar el máximo, mínimo y total de \"n\" números enteros")
        print("9. Salir")

        try:
            opcion = int(input("\nSeleccione una opción: "))

            if opcion == 1:
                print("\nOpción 1 seleccionada: Suma de 'n' números.")
                # Agregar funcion aqui...
            elif opcion == 2:
                print("\nOpción 2 seleccionada: Producto entre 'n' números.")
                # Agregar funcion aqui...
            elif opcion == 3:
                print("\nOpción 3 seleccionada: División entre 2 números.")
                # Agregar funcion aqui...
            elif opcion == 4:
                print("\nOpción 4 seleccionada: Calcular el factorial.")
                # Agregar funcion aqui...
            elif opcion == 5:
                print("\nOpción 5 seleccionada: Imprimir tablas de multiplicar.")
                while True:
                    try:
                        n = int(input("Introduce un número para mostrar sus tablas de multiplicar: "))
                        print(f"\nTablas de multiplicar del número {n}:")
                        for i in range (1, 11):
                            print(f"{n} x {i} = {n * i}")
                        repeat = input("\n¿Quieres intentar con otro número? (si/no): ").strip().lower()
                        if repeat == 'no':
                            break
                    except ValueError:
                        print("\nPor favor, introduce un número valido.")
            elif opcion == 6:
                print("\nOpción 6 seleccionada: Calcular cuadrado y cubo de un número.")
                while True:
                    try:
                        n = int(input("Introduce un número para calcular su cuadrado y cubo: "))
                        print(f"\nNúmero: {n}")
                        print(f"Cuadrado: {n ** 2}")
                        print(f"Cubo: {n ** 3}")
                        repeat = input("\n¿Quieres intentar con otro número? (si/no): ").strip().lower()
                        if repeat == 'no':
                            break
                    except ValueError:
                        print("\nPor favor, introduce un número valido.")
            elif opcion == 7:
                print("\nOpción 7 seleccionada: Determinar promedio de números.")
                # Agregar funcion aqui...
            elif opcion == 8:
                print("\nOpción 8 seleccionada: Encontrar máximo, mínimo y total de números.")
                # Agregar funcion aqui...
            elif opcion == 9:
                print("\nSaliendo del programa. ¡Hasta luego!")
                break
            else:
                print("\nOpción no válida. Intente nuevamente.")

        except ValueError:
            print("\nEntrada inválida. Por favor, ingrese un número.")

if __name__ == "__main__":
    main()
