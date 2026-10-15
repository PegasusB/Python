nums = input("Añada dos numeros a dividir, separlo con comas: ")
partes = nums.split(",")

num1 = float(partes[0])
num2 = float(partes[1])

if num2 == 0:
    print("Error: no se puede dividir entre cero.")
else:
    print(f"Este es el resultado de la division: {num1 / num2}")