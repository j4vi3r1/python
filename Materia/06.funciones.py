#01-DECLARANDO LA PRIMERA FUNCIÓN
print("\n##### 01 - DECLARANDO UNA FUNCIÓN SIMPLE #####")

def mi_primera_funcion():
    print("Esta es mi primera función")
    
mi_primera_funcion()

#02-DECLARANDO UNA FUNCION Y UTILIZANDO LISTAS
print("\n##### 02 - DECLARANDO UNA FUNCION Y UTILIZANDO LISTAS #####")

def concatenar(lista1,lista2):
    return lista1 + lista2

lista1 = [1,2,3]
lista2 = [4,5,6]

#Llamando a la funcion: "concatenar()""
print(concatenar(lista1, lista2))

#03-DECLARANDO UNA FUNCIÓN MULTIPLICACIÓN PASANDO PARAMETROS
print("\n##### 03 - DECLARANDO UNA FUNCIÓN MULTIPLICACIÓN PASANDO PARAMETROS #####")

def multiplicación (num1,num2):
    return num1*num2

#Llamando a la función: "multiplicaión"
print(multiplicación(10,2))


#04-EJEMPLO DE UNA FUNCIÓN
print("\n##### 04 - FUNCIONES SUMA Y RESTA (POR TECLADO) #####")

def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

a = int(input("Ingrese un numero: "))
b = int(input("Ingrese segundo numero: "))

#se llama la función: "suma"
resultado = suma(a,b)
print("La suma es:",resultado)

#se llama la función: "resta"
resultado2 = resta(a,b)
print("La resta es:",resultado2)