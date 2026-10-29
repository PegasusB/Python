edadCliente = int(input("Ingrese la edad del cliente: "))

if(edadCliente < 4):
    print("Puede entrar gratis")
elif(edadCliente <= 18):
    print("Tiene que pagar 5€")
elif(edadCliente > 18):
    print("Tiene que pagar 10€")
    