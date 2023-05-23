#WHILE
edad = 15
num = 0

#while edad<18:
    #print("Eres menor de eddad, no puedes manejar")

#Bucle infinito
#while True:
 #   print(num)
  #  num+2
  
print("##### 01-while #####")
print("Impresion de numeros de")

num = 0
while num <= 100:
    print(num)
    num += 2
print("Primer bucle terminado")

while num <= 200:
    print(num)
    num += 2
else:
    print("Mi condicion es igual o mayor a 200")
print("Segundo bucle se cerro")

while num <= 300:
    print(num)
    num += 2
    if num == 250:
        print("Mi condicion es igual a 250")
print("Tercer bucle terminado")

#Utilizando el break

while num <=400:
    print(num)
    num += 2
    if num == 350:
        print("Se detiene la ejecucion")
        break
print(num)
print("Cuarto bucle terminado")

#Loop infinito + Break
while True:
    parametro = input(">")
    if parametro == "exit":
        break
    else:
        print(parametro)
        

print("##### 02-FOR #####")

print("Impresion de una lista de 10 elementos de forma vertical utilizando for")
print("FOR N°1")

#No esta bien optimisado
for i in (1,2,3,4,5,6,7,8,9,10):
    print(i)
    
print("FOR N°2")
newlista = [1,2,3,4,5,6,7,8,9,10]
for i in newlista:
    print(i)
    
print("FOR N°3")
for i in range(1, 11):
    print(i)