nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (H/M): ").upper()

if sexo == "M" and nombre.upper() < "M":
    grupo = "A"
elif sexo == "H" and nombre.upper() > "N":
    grupo = "A"
else:
    grupo = "B"

print(f"Te corresponde el grupo {grupo}")