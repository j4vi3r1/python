estudiantes = {}
nombre_estudiante = input("Ingrese el nombre del estudiante:\n")
nombre_asignatura = input("Ingrese el nombre de la asignatura:\n")
nota_lab1 = float(input("Ingrese la nota del Laboratorio N°1:\n"))
nota_lab2 = float(input("Ingrese la nota del Laboratorio N°2:\n"))

promedio_ponderado = (nota_lab1 * 0.3) + (nota_lab2 * 0.7)

estudiantes[nombre_estudiante] = {"Asignatura": nombre_asignatura , 
                                   "Laboratorio N°1": nota_lab1, 
                                   "Laboratorio N°2": nota_lab2, 
                                   "Promedio Ponderado": round(promedio_ponderado, 1)}
print(estudiantes)
