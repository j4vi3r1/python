a = ["Rojo","Verde","Celeste","Violeta"]
b = ["Osorno","Puerto Montt","Puerto Varas", "Valdivia"]
#a
def palabra_mayorA():
    rojo,verde,violeta,celeste=a
    c = len(rojo)
    d = len(verde)
    e = len(celeste)
    f = len(violeta)
    if c>d and c>e and c>f:
        print("Rojo tiene mas caracteres")
    elif d>c and d>e and d>f:
        print("verde tiene mas caracteres")
    elif e>c and e>d and e>f:
        print("celeste tiene mas caracteres")
    elif f>c and f>d and f>e:
        print("violeta tiene mas caracteres")
    elif e>c and e>d and c==f:
        print("Celeste y Violeta tienen mas caracteres")
    else: print()
#b 
def mayor_palabra2():
    osorno,puerto_montt, puerto_varas,valdivia = b
    c = len(osorno)
    d = len(puerto_montt)
    e = len(puerto_varas)
    f = len(valdivia)
    if c>d and c>e and c>f:
        print("Osorno tiene mas caracteres")
    elif d>c and d>e and d>f:
        print("Puerto montt tiene mas caracteres")
    elif e>c and e>d and e>f:
        print("Puerto Varas tiene mas caracteres")
    elif f>c and f>d and f>e:
        print("Valdivia tiene mas caracteres")
#c
def concatenar():
    listas = a+b
print(concatenar)
#d
def mayusculas():
    listas = ["ROJO","VERDE","CELESTE","VIOLETA","OSORNO","PUERTO MONTT","PUERTO VARAS", "VALDIVIA"]
print(mayusculas)
#e
def ordenar():
    listas = ["ROJO","VERDE","CELESTE","VIOLETA","OSORNO","PUERTO MONTT","PUERTO VARAS", "VALDIVIA"]
    c = listas.sort()
print(ordenar)