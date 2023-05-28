#Parrafo a leer
parrafo = """La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional 
entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus
pilares fundamentales se basan en la inclusión, pluralismo, conciencia ambiental y participación
democrática"""

#Saber cuantas veces se repite la palabra 'universidad' tanto con mayuscula como con minuscula
rep1 = parrafo.count("universidad")
rep2 = parrafo.count("Universidad")
rep = rep1+rep2

#Imprimir la respuesta
print("La palabra 'universidad' se repite", rep , "veces")

#Guardar e imprimir las palabras encontradas dentro de una tupla
palabra = ("Universidad","universidad","Universidad")

print(palabra)
