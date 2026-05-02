while True:
    print("--- Calculadora ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    opcion = int(input("Elige una opción: "))

    if opcion in [1, 2, 3, 4]:
        a = float(input("Ingrese número A: "))
        b = float(input("Ingrese número B: "))
        if   opcion == 1: print("Resultado:", a + b)
        elif opcion == 2: print("Resultado:", a - b)
        elif opcion == 3: print("Resultado:", a * b)
        elif opcion == 4:
            if b != 0: print("Resultado:", a / b)
            else: print("Error: división por cero")
    elif opcion == 5:
        print("Adiós.")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")