rentUsu = int(input("Ingrese su renta anual: "))

if rentUsu < 10000:
    print("Le corresponde el 5%")
elif 10000 <= rentUsu <= 20000:
    print("Le corresponde el 15%")
elif 20000 <= rentUsu <= 35000:
    print("Le corresponde el 20%")
elif 35000 <= rentUsu <= 60000:
    print("Le corresponde el 30%")
elif rentUsu > 60000:
    print("Le corresponde el 45%")
else:
    print("Error")
