#08-EJERCICIO

mes = input("Ingrese un mes: ")
print()
estaciones = {
    "enero": "verano",
    "febrero": "verano",
    "marzo": "otoño",
    "abril": "otoño",
    "mayo": "otoño",
    "junio": "invierno",
    "julio": "invierno",
    "agosto": "invierno",
    "septiembre": "primavera",
    "octubre": "primavera",
    "noviembre": "primavera",
    "diciembre": "verano"
}

if mes in estaciones:
    estacion = estaciones[mes]
    print("La estación correspondiente al mes de", mes, "es", estacion)
    print()
else:
    print("Mes inválido. Por favor, ingrese un mes válido en minúsculas.")
    print()