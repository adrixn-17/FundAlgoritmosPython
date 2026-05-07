def MostrarLinea(caracter, n):
    linea = ""
    for i in range(n):
        linea = linea + caracter
    print(linea)

if __name__ == "__main__":
    MostrarLinea("*", 10)
    MostrarLinea("-", 20)