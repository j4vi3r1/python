pacientes = [["Pedro",1.78],["Constanza",1.56],["Amanda",1.62],["Dario",1.89],["Fernanda",1.67]]
a = 1.78
b = 1.56
c = 1.62
d = 1.89
e = 1.67
#a
def estatura_minima():
    if a>b and a>c and a>d and a>e:
        print("la estatura minima es de Pedro,midiendo: ",a, "cm")
    elif b>a and b>c and b>d and b>e:
        print("la estatura minima es de constanza, midiendo: ",b, "cm")
    elif c>a and c>b and c>d and c>e:
        print("la estatura minima es de amanda, midiendo: ",c, "cm")
    elif d>a and d>b and d>c and d>e:
        print("la estatura minima es de dario, midiendo: ",d, "cm")
    elif e>a and e>b and e>c and e>d:
        print("la estatura minima es de fernanda, midiendo: ",e, "cm")
    else : print()
#b
def agregar_elemento():
    agregar = pacientes.append(["Ricardo",[1.71]])
    print(agregar_elemento)
#c
def encontrar_elementos():
    agregar = pacientes.append(["Ricardo",[1.71]])
    if agregar(0) ==["Dario", 1.89]:
        print(agregar(0))
    elif agregar(1) ==["Dario", 1.89]:
        print(agregar(1))
    elif agregar(2) ==["Dario", 1.89]:
        print(agregar(2))
    elif agregar(3) ==["Dario", 1.89]:
        print(agregar(3))
    elif agregar(4) ==["Dario", 1.89]:
        print(agregar(4))
    elif agregar(5) ==["Dario", 1.89]:
        print(agregar(5))
    else: print("el dato no se encuentra")
#d
estatura_minima()
agregar_elemento()
encontrar_elementos()