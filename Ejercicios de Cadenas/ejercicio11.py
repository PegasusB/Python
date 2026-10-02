producto = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio: "))
unidades = int(input("Introduce el número de unidades: "))

costeTotal = precio * unidades

print(f"{producto} {precio:09.2f} {unidades:03d} {costeTotal:011.2f}")