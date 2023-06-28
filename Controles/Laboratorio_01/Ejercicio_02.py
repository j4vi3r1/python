import statistics

a = [10,9,12,15,18]
b = [21,8,15,3,12]

lista = a+b
print("a:",lista)

lista.insert(1,30)
print("b:", lista)

print("c:",set(lista))

d = [4, 5, 6]

c = lista + d
print("d:", c)

media = statistics.mean(c)
mediana = statistics.median(c)

suma = sum(c)
print("e:", suma)

print("Media:", media)
print("mediana:", mediana)
