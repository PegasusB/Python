precioPan = 3.49
descuento = 0.60

numBarras = int(input("Ingrese el número de barras de pan que no son del dia:  "))

descuentoBarras = precioPan * descuento
precioFinalBarra = precioPan - descuentoBarras
costeTotal = numBarras * precioFinalBarra

print(f"Precio habitual de una barra: {precioPan:.2f} €")
print(f"Descuento por no ser del día: {descuentoBarras:.2f} €")
print(f"Coste final total: {costeTotal:.2f} €")