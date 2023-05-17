ciudades = ["Santiago", "Temuco", "Osorno", "Punta Arenas"]
ica = [134, 99, 245, 50]

calidad_aire_alto = list(zip(ciudades, ica))

print(calidad_aire_alto)
print()
print("ICA: índice de calidad del aire")
print()
print("La ciudad con ICA más bajo es", ciudades[-1],"con un ICA de", ica[-1])
if ica[-1]>=0 and ica[-1]<=50:
    print("Buena")
if ica[-1]>=51 and ica[-1]<=100:
    print("Moderada")
if ica[-1]>=101 and ica[-1]<=150:
    print("Dañina a la salud para grupos sensibles")
if ica[-1]>=151 and ica[-1]<=200:
    print("Dañina a la salud")
if ica[-1]>=201 and ica[-1]<=300:
    print("Muy dañina a la salud")
if ica[-1]>300:
    print("Peligrosa")
print()
print("La ciudad con ICA más alto es", ciudades[-2], "con un ICA de", ica[-2])
if ica[-2]>=0 and ica[-2]<=50:
    print("Buena")
if ica[-2]>=51 and ica[-2]<=100:
    print("Moderada")
if ica[-2]>=101 and ica[-2]<=150:
    print("Dañina a la salud para grupos sensibles")
if ica[-2]>=151 and ica[-2]<=200:
    print("Dañina a la salud")
if ica[-2]>=201 and ica[-2]<=300:
    print("Muy dañina a la salud")
if ica[-2]>300:
    print("Peligrosa")
print()