#Este es un comentario
#GUIA RAPIDA: CONOCIENDO LAS VARIABLES DE PYTHON 10-04-2023 PROGRAMACIÓN

#un simple print
print("hello world")

#01- DECLARANDO VARIABLES DE TIPO CADENA DE TEXTO
nombre= "Hector"
name= "Javier"

PI= 3.14

#02- IMPRESION DE UNA VARIABLE
print(nombre)
print("Hola soy", name)

#Declarando una tercera variablede de tipo númerico 
edad= 19

#03- IMPRESION DE TEXTO + VARIABLE (IMPRESION DE VARIABLE EDAD)
print("Mi edad es", edad)

#04- IMPRIMIENDO DOS VARIABLES EN UNA MISMA LINEA
print("Hola mi nombre es", name,"y tengo", edad,"años")#impresion separando con comas
print("Hola mi nombre es"+" "+name+" "+"y tengo"+" "+str(edad)+" "+"años")#concatenación con signo +
print(f"Hola mi nombre es {name} y tengo {edad} años")#formato de cadenas literales (PYTHON 3.6 EN ADELANTE)

#05- ACTUALIZANDO LA VARIABLE NOMBRE (Mutable)
nombre= "Diego"
peso= 75.2
print("Hola mi nuevo nombre es", nombre)

#06- ¿VARIABLES EN UNA SOLA LINEA? (no es muy recomendable, solo en ciertas situaciones)
ciudad, region, pais, year = "Rio Bueno", "Los Rios", "Chile", "2003"
print("Yo naci en la ciudad de", ciudad, ", region de", region, pais,"en el año",year)

#07- UTILIZANDO LA INSTRUCCION INPUT
nombre1= input("¿Cual es tu nombre?\n")
edad1= input("¿Cual es tu edad?\n")

print("Tu nombre es", nombre1, "y tu edad", edad1)
