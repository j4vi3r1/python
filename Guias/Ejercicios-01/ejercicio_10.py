#10-EJERCICIO

agenda = {
    "Nombre": "Juan Perez",
    "Direccion": "Calle Principal 123",
    "Ciudad": "Ciudad Ejemplo",
    "Numero telefonico": "1234567890"
}

agenda["Redes Sociales"] = ["JuanPerezFB", "JuanPerezIG", "JuanPerezTW"]

print("Perfil de Facebook:", agenda["Redes Sociales"][0])

print("Agenda completa:")
for clave, valor in agenda.items():
    print(clave + ":", valor)