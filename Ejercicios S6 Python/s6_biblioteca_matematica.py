def EsPar(n):
    return n % 2 == 0

def Factorial(n):
    r = 1
    for i in range(1, n + 1):
        r = r * i
    return r

def MaxDe3(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c

def ConvTemp(c):
    return c * 9 / 5 + 32

def AreaRect(b, h):
    return b * h

# Pruebas
print("¿8 es par?", EsPar(8))
print("Factorial de 5:", Factorial(5))
print("Mayor de 3, 7, 5:", MaxDe3(3, 7, 5))
print("25°C en Fahrenheit:", ConvTemp(25))
print("Area rectangulo 4x6:", AreaRect(4, 6))