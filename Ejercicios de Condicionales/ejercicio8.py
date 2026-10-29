puntos = float(input("¿Cuantos puntos has tenido? "))
dinero = 2400

if(puntos == 0.0): 
    print("Su nivel es inaceptable")
    print("Usted recibe: ", dinero*puntos)
elif(puntos == 0.4):
    print("Su nivel es aceptable")
    print("Usted recibe: ", dinero*puntos)
elif(puntos >= 0.6):
    print("Su nivel es meritorio")
    print("Usted recibe: ", dinero*puntos)
else: 
    print("Esa no es una opción")