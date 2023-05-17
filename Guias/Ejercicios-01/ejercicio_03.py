#03-EJERCICIO

import math

a = float(input("Ingrese longitud del lado a: "))
b = float(input("Ingrese longitud del lado b: "))
c = float(input("Ingrese longitud del lado c: "))

if a+b<=c or a+c<=b or b+c<=a:
    print("Los lados ingresados no corresponden a un triangulo verdadero")
    exit()
    
if a == b and b == c:
    print("El triangulo es equilatero")
elif a == b or a == c or b == c:
    print("El triangulo es isoceles")
else: print("El triangulo es escaleno")

p = (a+b+c)/2

area = math.sqrt(p*(p-a)*(p-b)*(p-c))

print("El area del triangulo es:", round(area, 2))