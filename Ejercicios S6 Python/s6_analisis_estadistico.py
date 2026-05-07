def LeerNota(mensaje):
    nota = -1
    while nota < 0 or nota > 20:
        nota = float(input(mensaje))
        if nota < 0 or nota > 20:
            print("Nota inválida. Ingrese entre 0 y 20.")
    return nota

def EsAprobado(nota):
    return nota >= 11

def ClasificarNota(nota):
    if nota >= 18:
        return "Excelente"
    elif nota >= 14:
        return "Bueno"
    elif nota >= 11:
        return "Aprobado"
    else:
        return "Desaprobado"

def CalcularPromedio(suma, n):
    return suma / n

def MostrarEstadisticas(prom, mayor, menor, aprobados, total):
    print("====== ESTADÍSTICAS ======")
    print("Promedio:    ", prom)
    print("Mayor nota:  ", mayor)
    print("Menor nota:  ", menor)
    print("Aprobados:   ", aprobados, "/", total)
    print("==========================")

# --- MAIN ---
n = int(input("¿Cuántas notas desea ingresar? "))

suma = 0
mayor = -1
menor = 21
aprobados = 0

for i in range(n):
    nota = LeerNota("Ingrese nota " + str(i + 1) + ": ")
    suma = suma + nota
    if nota > mayor:
        mayor = nota
    if nota < menor:
        menor = nota
    if EsAprobado(nota):
        aprobados = aprobados + 1
    print("Clasificación:", ClasificarNota(nota))

prom = CalcularPromedio(suma, n)
MostrarEstadisticas(prom, mayor, menor, aprobados, n)