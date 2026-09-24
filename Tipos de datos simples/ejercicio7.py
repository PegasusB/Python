peso = float(input("Introduzca su peso(Kg): "))
estatura = float(input("Introduzca su estatura(m): "))

imc = peso / estatura **2

print(f"Tu IMC es de: {round(imc, 2)}")