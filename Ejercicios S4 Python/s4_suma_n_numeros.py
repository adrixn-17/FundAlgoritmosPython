n = int(input("¿Cuántos números quieres sumar? "))

suma = 0
mayor = None
menor = None
i = 1

while i <= n:
    num = int(input(f"Ingrese número {i}: "))
    suma += num
    if mayor is None:
        mayor = menor = num
    else:
        if num > mayor: mayor = num
        if num < menor: menor = num
    i += 1

promedio = suma / n
print(f"Cantidad: {n}")
print(f"Suma total: {suma}")
print(f"Promedio: {promedio:.2f}")
print(f"Mayor: {mayor}")
print(f"Menor: {menor}")