total = 0
suma = 0
mayor = -1
menor = 21
excelente = bueno = aprobado = desaprobado = 0

while True:
    nota = int(input("Ingrese nota (0-20) o -1 para salir: "))
    if nota == -1:
        break
    if 0 <= nota <= 20:
        total += 1
        suma += nota
        if nota > mayor: mayor = nota
        if nota < menor: menor = nota
        if   nota >= 17: excelente += 1
        elif nota >= 14: bueno += 1
        elif nota >= 11: aprobado += 1
        else:            desaprobado += 1
    else:
        print("Nota inválida. Ingresa entre 0 y 20.")

if total > 0:
    print(f"Total de notas: {total}")
    print(f"Promedio: {suma/total:.2f}")
    print(f"Nota más alta: {mayor}")
    print(f"Nota más baja: {menor}")
    print(f"Excelente (17-20): {excelente}")
    print(f"Bueno (14-16): {bueno}")
    print(f"Aprobado (11-13): {aprobado}")
    print(f"Desaprobado (0-10): {desaprobado}")
else:
    print("No se ingresó ninguna nota.")