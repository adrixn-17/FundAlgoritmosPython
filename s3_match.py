print("##### Menu Calculadora #####")
print("Menu Operaciones")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("")
resultado = 0.0
a = float(input("Ingresa primer número: "))
b = float(input("Ingresa segundo número: "))
opc = float(input("Ingresa opción: "))
match opc:
    case 1:
        resultado = a + b
    case 2:
        resultado = a - b
    case 3:
        resultado = a * b
    case 4:
        resultado = a / b
print("Resultado: ", resultado)