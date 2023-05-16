#Clase 26-04-2023 apuntes de tipo de datos

#{} = llaves
#[] = corchetes
#() = parentecis
#/ = division
#** = exponente

edad = 29
estatura = 1.71
peso = 70.5
complejo = 1 + 41 #complejos

print("01. datos numericos")
print(f"mi estatura es de {estatura} y el peso es de {peso}")
print("impresion de un numero complejo:", complejo,"\n")

#TRANSFORMACION DE ENTERO A REAL
print(peso)
print("transformando un valor real a entero:", int(peso))

#OPERACIONES ARITMETICAS BASICAS
imc = peso / (estatura**2)
print("Mi IMC es de:", imc,"\n")

print("Mi IMC es de: {:.2f}". format(imc),"\n") #FORMATEANDO EL VALOR DE SALE 2 DECIMALES

#02- DATOS DE TIPO CADENA DE CARACTERES
asignatura = "programacion"
carrera = "Ingenieria Civil en Informatica"
print("#### 02-strings ####")
print("La asignatura de", asignatura,"corresponde a la carrera de", carrera)

#UTILIZANDO LA FUNCION LEN (cuenta la cantidad de caracteres)
print("la cantidad de caracteres de la palabra", asignatura, "es de:", len(asignatura))
print("la cantidad de caracteres de la palabra", carrera, "es de:", len(carrera))

#03-VALORES DE VERDADERO Y FALSO
ampolleta = False
interruptor = True

print("##### 03-BOOLEANS #####")
print(ampolleta, interruptor)
print("La variable ampolleta es de tipo:", type(interruptor), "\n") #type reconoce el tipo de dato que se esta trabajando

#podemos transformar cualquier valor a un booleano al igual que un string, int, etc
#booleano es un tipo de dato
print(bool(0))
print(bool(""))
print(bool(None))
print(bool("true"))
print(bool(1))
print("\n")

#04-DATOS DE TIPO LIST (objetos de tipo colección) - (mutable)
print("##### 04 - LISTA #####")

#inicializando lista de 2 maneras
nueva_lista = list()
otra_lista = []
print("esta es una lista vacia:",nueva_lista)
print("esta es otra lista vacia:", otra_lista)
print(type(otra_lista))

#declarando tres listas diferentes
estudiantes = ["Matias","Marco","Cristobal","Sebastian","Marco"]
num  = [1,2,3,4,5,6]
lenguaje = ["python"]

mixta = ["Juan", 18, "Pepe", 14]

print(estudiantes)
print(num)
print(lenguaje)
print(mixta)

#se puede realizar una lista de datos cumpuestos
data = ["osorno",{"UV":"nivel bajo","Temp *C":15}, {-40.5725,-72.1353}]
listamixta = ["Felipe", 100, True]

print("Lista de cadena de caracteres:", estudiantes)
print("Lista de numeros:", num)
print("Lista de un elemento:", lenguaje)
print("Esta es una lista mixta:", listamixta)
print("Esto igual es una lista", data)
print(len(listamixta))#para saber la cantidad de elementos de una lista
print(estudiantes.count("Marco"))#cuenta la cantidad de elementos de Marco
print(num.count(5000))#cantidad de ocurrencias de un elemtento en especifico

lenguaje = ["javascript"]
print("Nuevo valor del arreglode un elemento:", lenguaje)

#¿como accedo a un alemento especifico de la lista?
print(estudiantes[0])#correcto (1° elemento de la lista)
print(estudiantes[1])#(2° elemento de la lista)
#print(estudiantes[5]) #incorrecto 
print("posicion -2", estudiantes[-2])

#¿se pueden sumar listas?
print("suma de listas",estudiantes+num)

#que hacen estas funciones
print(list("python"))
print(list(range(10)))
print("\n")

#> En el fichero de listas se mostraran mas funciones

#05- TUPLAS - (No mutables)
newtupla = tuple()
grupo1 = ("Daniel","Cristian", "Felipe",200,100,"Daniel")
print("##### 05 - TUPLAS #####")
print(type(grupo1))

#Accediendo al primer elemento de la tupla
print(grupo1[0])

#Consultando el elemento "Daniel" cuantas veces se encuentra en la tupla
print("El elemento se repite:",grupo1.count("Daniel"))

#Muestra el indice del primer elemento buscado
print("Indice de elemento:",grupo1.index("Daniel"))

#Reasignando el prmer elemento de la tupla
"""grupo1[0] = "Constanza"
print(grupo1)"""

#¿Se pueden sumar las tuplas?

#Obteniendo un trozo de la tupla
grupo2 = ("Pedro",100,"Felipe","Diego",2020,"Alejandra")
print("Trozo de la tupla",grupo2[0:3])

#¿Entonces como no puedo modificar una tupla, que puedo hacer?
grupo1 = list(grupo1)
print("La tupla ahora es de tipo:",type(grupo1),"\n")
print("\n")

#06 - SETS (Conjuntos) - Estructura fija
#Formas de iniciar un set
print("##### 06- SETS #####")
conjunto_vacio = set()
conjunto_vacio1 = {} #¿Diccionario o set?
print(type(conjunto_vacio1))
conjunto_colores = set({"Azul","Rojo","Verde"}) #Utilizando la funcion set
conjunto_animales = {"Gato","Perro","Loro"} #Utilizando llaves

print(type(conjunto_colores)) #Tipo de dato set
print(type(conjunto_animales)) #Tipo de dato set
print("El primer set contiene los siguientes colores:",conjunto_colores)
print("El segundo set contiene los siguientes animales:", conjunto_animales)

#print(conjunto_animales[0]) #Accediendo añ primer elemento del set
conjunto_colores.add("Celeste") #Agregando un cuarto color
print("El set de colores lo conforman:",conjunto_colores)

#Conjunto_animales.add("Gato")
print("El set de animales lo conforman:", conjunto_animales)

print('######### DICCIONARIOS #########')
diccionario1 = dict()
diccionario2 = {}

datos_personales = {
        'Nombre' : 'Monse',
        'Institucion' : 'Ulagos', 
        'Edad' : 17,
        'Periodo' : {'Primer Semestre', 'ICINF'}
}

#imprimir diccionario
print('Diccionario inicial: ',datos_personales)

#consulta la cantidad de elementos en el diccionario
print(len(datos_personales))

#agregando un nuevo campo al diccionario
#datos_personales['Ciudad' : 'Osorno']
print()
