import random

#Definir la lista
numeros = []
#Definir cantidad de numeros a buscar
for i in range(20):
    #Buscar numeros aleatorios entre cierto rango de numeros
    numeros.append(random.randint(40,350))

#Imprimir los numeros encontrados
print(numeros)

#Pedir que ingrese un numero a buscar en la lista
bus = int(input("Ingrese el numero que desea buscar: "))

#Buscar e imprimir la cantidad de ocurrencias del numero a buscar
rep= numeros.count(bus)
print("El numero", bus, "aparece", rep, "veces en la lista")