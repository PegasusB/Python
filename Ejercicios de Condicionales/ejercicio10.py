pizza = input("Quiere su pizza vegetariana o normal: ")

if(pizza.lower == "vegetariana"):
    ingredientesV = input("Nuestros ingredientes para la pizza vegetariana son pimiento y tofu, elija solo 1")
    print(f"Su pizza {pizza} esta compuesta por tomate, mozzarella y {ingredientesV}")
elif(pizza.lower == "normal"):
    ingredientesN = input("Nuestros ingredientes para la pizza normal son peperoni, jamon y salmon, elija solo 1")
    print(f"Su pizza {pizza} esta compuesta por tomate, mozzarella y {ingredientesN}")
else :
    print("ERROR")
