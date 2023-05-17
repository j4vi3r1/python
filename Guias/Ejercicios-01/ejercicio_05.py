#05-EJERCICIO

lab1 = float(input("Ingrese nota del laboratorio 1: "))
lab2 = float(input("Ingrese nota del laboratorio 2: "))
lab3 = float(input("Ingrese nota del laboratorio 3: "))

promedio = (lab1*0.3)+(lab2*0.4)+(lab3*0.3)

if promedio<4.0:
    mensaje = "El estudiante reprobo la asignatura"
    
if promedio>4.0:
    mensaje = "El estudiante aprobo la asignatura"
    
if promedio>6.0:
    mensaje = "El estudiante aprobo con distincion"
    
print(mensaje)