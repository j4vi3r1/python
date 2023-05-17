#09-EJERCICIO

import statistics

numeros = [4, 3, 8, 12, 6, 10, 14, 3, 6]

numeros.pop()

numeros.insert(0, 2)

numeros = list(set(numeros))


media = statistics.mean(numeros)
mediana = statistics.median(numeros)

print("Lista de números:", numeros)
print("Media:", media)
print("Mediana:", mediana)