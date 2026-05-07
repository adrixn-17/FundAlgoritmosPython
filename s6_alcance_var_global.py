cont = 0 # Global

def Contar():
    global cont # Llamar a la variable declarada como
    cont = cont + 1
    print("Valor de cont desde la Funcion: " ,cont)

if __name__ == "__main__":
    print("Valor de cont: ", cont)
    Contar()
    Contar()
    Contar()
    print("Valor de cont: ", cont)