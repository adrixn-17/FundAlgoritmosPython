# Programa que calcula el IMC
# Declaracion y obtencion de datos
peso = float(input("Ingrese su peso (Kg): "))
altura = float(input("Ingrese su altura (m): "))

#Proceso
imc = peso / altura ** 2

#Mostrar informacion
print("Su imc es: ", imc)