productos = input("Introduce los productos de la cesta separados por comas: ")

productos = productos.split(",")

for producto in productos:
    print(producto)