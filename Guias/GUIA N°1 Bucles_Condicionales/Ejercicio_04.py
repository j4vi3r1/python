numero = int(input("Ingrese un numero: "))

#Para sarar el primer numero impar
inpar = (numero*(numero-1))+1
print(inpar)

#Variable acumular es para acumular la suma
acum = 0

#Para sumar los numeros impares
for i in range(numero):
    acum = acum + inpar
    if i == (numero-1):
        break
    #Para que la variable se vaya incrementando en 2
    inpar = inpar + 2
    print(inpar)
print("El cubo de",numero,"es:",acum)