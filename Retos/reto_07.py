#Pedir que ingrese una frase por teclado
frase = input("\nIngrese una frase: ")

#Definir la función
def separar_palabras(frase):
    #Separar la frase en palabras con 'split'
    palabras = frase.split()
    #Definir diccionario
    diccionario = {}
    for palabra in palabras:
        #Definir la clave y el valor del diccionario
         diccionario[palabra] = len(palabra)#Contar los caracteres de cada palabra con la funcion 'len'
    return diccionario

#Definir 'resultado' como la función creada y la 'frase' a la cual afecta
resultado = separar_palabras(frase)
#Imprimir los valores en un diccionario
print("\n Diccionario:")
print()
print(resultado)
print()