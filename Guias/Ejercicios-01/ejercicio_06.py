#06-EJERCICIO

grupo1 = {"Marcos", "Gabriela", "Benjamin", "Matias"}
grupo2 = {"Marcos", "Nicolas", "Diego", "Matias"}

estudiantes_en_comun = grupo1.intersection(grupo2)

if len(estudiantes_en_comun)>0:
    print("Los siguientes estudiantes estan en ambos grupos: ")
    for estudiantes in estudiantes_en_comun:
     print(estudiantes)
else: print("No hay estudiantes en comun en ambos grupos")