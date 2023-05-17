#04-EJERCICIO

nombre1 = input("Ingrese su nombre: ")
nombre2 = input("Ingrese el nombre de otra persona: ")    

primera_letra1 = nombre1[0]
primera_letra2 = nombre2[0]

ultima_letra1 = nombre1[-1]
ultima_letra2 = nombre2[-1]

if primera_letra1 == primera_letra2:
    print("Ambos nombres comienzan con la misma letra.")
elif ultima_letra1 == ultima_letra2:
    print("Ambos nombres terminan con la misma letra.")
else: print("Ambos nombres difieren tanto en la letra inicial como en la final.")