#01-EJERCICIO

num1 = int(input("Ingrese primer numero entero: "))
num2 = int(input("Ingrese segundo numero entero: "))
num3 = int(input("Ingrese tercer numero entero: "))

numero_mayor = num1
numero_menor = num1

if num2>num1:
    numero_mayor = num2
    
if num3>num1:
    numero_mayor = num3

if num2<num1:
    numero_menor = num2
    
if num3<num1:
    numero_menor = num3

print("El numero mayor es:",numero_mayor)
print("El numero menor es:",numero_menor)
