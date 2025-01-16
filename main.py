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
                print("Opción 1 seleccionada: Suma de 'n' números.")
                # Agregar funcion aqui...
            elif opcion == 2:
                print("Opción 2 seleccionada: Producto entre 'n' números.")
                # Agregar funcion aqui...
            elif opcion == 3:
                print("Opción 3 seleccionada: División entre 2 números.")
                # Agregar funcion aqui...
            elif opcion == 4:
                print("Oción 4 seleccionada: Calcular el factorial.")
                # Agregar funcion aqui...
            elif opcion == 5:
                print("Opción 5 seleccionada: Imprimir tablas de multiplicar.")
                # Agregar funcion aqui...
            elif opcion == 6:
                print("Opción 6 seleccionada: Calcular cuadrado y cubo de un número.")
                # Agregar funcion aqui...
            elif opcion == 7:
                print("Opción 7 seleccionada: Determinar promedio de números.")
                # Agregar funcion aqui...
            elif opcion == 8:
                print("Opción 8 seleccionada: Encontrar máximo, mínimo y total de números.")
                # Agregar funcion aqui...
            elif opcion == 9:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

if __name__ == "__main__":
    main()
