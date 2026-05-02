tipo = int(input("Tipo de cliente (1=VIP, 2=Regular): "))
monto = float(input("Monto de compra (S/): "))

if tipo == 1:
    if monto > 100:
        descuento = monto * 0.20
    else:
        descuento = monto * 0.10
else:
    if monto > 200:
        descuento = monto * 0.10
    else:
        descuento = monto * 0.05

total = monto - descuento
print("Descuento aplicado: S/", descuento)
print("Monto final a pagar: S/", total)