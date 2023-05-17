#02-EJERCICIO

palabra1 = input("Ingrese primera palabra: ")
palabra2 = input("Ingrese segunda palabra: ")

longitud_palabra1 = len(palabra1)
longitud_palabra2 = len(palabra2)

if longitud_palabra1>longitud_palabra2:
    print("La palabra con mas caracteres es:", palabra1)
    print("La palabra con menos caracteres es:", palabra2)
elif longitud_palabra1<longitud_palabra2:
    print("La palabra con mas caracteres es:", palabra2)
    print("La palabra con menos caracteres es:", palabra1)
else: print("La dos palabras tiene la misma longitud")