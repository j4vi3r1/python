import time
import os

#Definir valores
hora = 0
min = 0
seg = 0
 
#Definir el rango de hora, minuto y segundo
for hora in range(24):
    for min in range(60):
        for seg in range(60):
            #Formato a imprimir
            print(hora,":", min,":", seg)
            #Definir tiempo de espera hasta que digite el siguiente valor
            time.sleep(0)
            #Limpiar la terminal despues de digitar un numero
            os.system("cls")
            #Hacer que el valor de cada segundo incremente en uno de forma consecutiva
            seg = seg+1
        else:
            #Cuando seg sea igual a 60, min incrementara en 1 y seg volvera a cero
            min = min+1
            seg = 0
    else:
        #Cuando min sea igual a 60, hora incrementara en 1 y min volvera a 60
        hora = hora+1
        min = 0
        

