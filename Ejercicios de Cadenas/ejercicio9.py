fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")

partes = fecha.split("/")

print(f"Día: {partes[0]}")
print(f"Mes: {partes[1]}")
print(f"Año: {partes[2]}")