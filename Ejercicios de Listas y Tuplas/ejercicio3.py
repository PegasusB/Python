asignaturas = ["Matematicas","Fisica","Quimica","Historia","Lengua"]
notas = []

for i in asignaturas:
    nota = input(f"Cual fue tu nota en {i}?: ")
    notas.append(nota)
for j in range(len(asignaturas)):
    print("En ", asignaturas[j], "sacaste un ", notas[j])
    