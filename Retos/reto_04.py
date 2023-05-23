num = int(input("Ingrese un numero: "))

if num%2 == 0:
    print("El numero es par")
else: 
    print("El numero es impar")
    
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero/2) + 1):
        if numero % i == 0:
            return False
    return True

if es_primo(num):
    print("Es un numero primo")
else:
    print("No es un numero primo")
    
if num > 50:
    print("Es un numero mayor a 50")
else:
    print("Es un numero menor que 50")