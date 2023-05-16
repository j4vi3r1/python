print("##### 01 OPERADORES ARITMETICOS #####")

a = 25
b = 2
c = 14
d = 36
e = 7

#operadores aritmeticos o comunes
print("Suma a + b es:", a + b)
print("Resta a - b es:", a - b)
print("Multiplicacion entre a * b es:", a * b)
print("Divicion entre a / b es:", a / b )
print(a%b)
print(a**b)
print(a//b)

t = 5.39
g = 9.81

#operadores aritmeticos entre flotantes
v = g * t
print(f"la velocidad del objetivo en caida libre es de: {v} b\s")
print("la velocidad del objeto en caida libre es de: {:.2f}")

#creando un numero complejo con complex
c2 = complex(3,-5)

print("el numero complejo es:", c2)

print(c2.real)#obteniendo la parte real del complex
print(c2.imag)

print("hola"*5)

#print("hola"*3.7*2)

print("hola"*(int((10*2)/5)))

a = 1
b = 2

print("##### 02-operadores de comparacion #####")
print(a == b)#es igual
print(a != b)#es distinto
print(a > b)#mayor a
print(a < b)#menor a
print(a >= b)#mayor igual
print(a <= b)#menor igual

animal_domestico = "gato"
animal_salvaje = "leopardo"
print("\nComparando cadenas de caracteres")
print(a>b)
print(animal_domestico == animal_salvaje)
print(animal_domestico != animal_salvaje)
print(animal_domestico > animal_salvaje)
print(animal_domestico < animal_salvaje)
print(animal_domestico >= animal_salvaje)
print(animal_domestico <= animal_salvaje)

print("##### 03-OPERADORES LOGICOS #####")

bencina = True
encendido = True
edad = 19

#utilizando el operador AND
if bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")
    
#utilizando el operador OR
if bencina or encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")
    
#utilizando el operador NOT junto al AND
if not bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")
    
#utilizando el operador NOT junto al OR
if not bencina or encendido:
    print("Utilizando Nor y OR: El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")
    
#utilizando el operador NOT junto AND y OR
if not bencina or (encendido and edad >=18):
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")
    
