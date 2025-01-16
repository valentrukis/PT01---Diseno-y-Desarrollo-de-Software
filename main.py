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
                suma_numeros()
            elif opcion == 2:
                print("\nOpción 2 seleccionada: Producto entre 'n' números.")
                producto_numeros()
            elif opcion == 3:
                print("\nOpción 3 seleccionada: División entre 2 números.")
                division_numeros()
            elif opcion == 4:
                print("\nOpción 4 seleccionada: Calcular el factorial.")
                calcular_factorial()
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
                determinar_promedio()
            elif opcion == 8:
                print("\nOpción 8 seleccionada: Encontrar máximo, mínimo y total de números.")
                Calcular_max_min()
            elif opcion == 9:
                print("\nSaliendo del programa. ¡Hasta luego!")
                break
            else:
                print("\nOpción no válida. Intente nuevamente.")

        except ValueError:
            print("\nEntrada inválida. Por favor, ingrese un número.")
        
def suma_numeros():
    print("Introduce números para sumar. Ingresa una línea vacía para finalizar.")
    suma = 0
    while True:
        entrada = input("Número: ")
        if entrada.strip() == "":
            break
        try:
            suma += float(entrada)
        except ValueError:
            print("Por favor, introduce un número válido.")
    print(f"La suma es: {suma}")

    input ("Presione cualquier tecla para continuar.")
    
def producto_numeros():
    print("Introduce números para multiplicar. Ingresa una línea vacía para finalizar.")
    producto = 1
    numeros_ingresados = False
    while True:
        entrada = input("Número: ")
        if entrada.strip() == "":
            break
        try:
            producto *= float(entrada)
            numeros_ingresados = True
        except ValueError:
            print("Por favor, introduce un número válido.")
    if numeros_ingresados:
        print(f"El producto es: {producto}")
    else:
        print("No se ingresaron números válidos.")
    input ("Presione cualquier tecla para continuar.")

4
def calcular_factorial():
    print("Calculadora de Factoriales")
    i = 1
    num = int(input("Ingrese un número: "))

    factorial = 1
    while (i <= num):
        factorial = factorial * i
        i = i+1

    print ("Factorial de " + str(num) + " = " + str(factorial))
    input ("Presione cualquier tecla para continuar.")

def Calcular_max_min():
    print("Valor mínimo y máximo de varios valores")
    valores = []
    while True:
        entrada = input("Número: ")
        if entrada.strip() == "":
            break
        try:
            valores.append(float(entrada))
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    if valores:
        minimo = min(valores)
        maximo = max(valores)
        print(f"Valor mínimo: {minimo}")
        print(f"Valor máximo: {maximo}")
    else:
        print("No se ingresaron números válidos.")
    
    input("Presione cualquier tecla para continuar.")

def determinar_promedio():
    numeros = []
    print("Ingrese números para calcular el promedio. Ingrese -1 para finalizar.")
    while True:
        try:
            num = float(input("Número: "))
            if num == -1:
                break
            numeros.append(num)
        except ValueError:
            print("Por favor, ingrese un número válido.")

    if numeros:
        promedio = sum(numeros) / len(numeros)
        print(f"El promedio de los números ingresados es: {promedio}")
    else:
        print("No se ingresaron números.")

def division_numeros():
    print("Introduzca los valores a dividir.")
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if num2 == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}")
    except ValueError:
        print("Por favor, ingrese números válidos.")
    input("Presione cualquier tecla para continuar.")



if __name__ == "__main__":
    main()