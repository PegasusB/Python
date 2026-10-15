precio = input("Introduce el precio del producto: ")

partes = precio.split(".")

print(f"Euros: {partes[0]}")
print(f"Céntimos: {partes[1]}")