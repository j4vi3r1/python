censo = {
    "ID region":[8]+[10] ,
    "Nombre":["BioBio"]+["Los Lagos"] ,
    "Superficie (Km2)":[23890]+[48583] ,
    "Habitantes (2017)":[1556805]+[828708]
}
c = round(1556805/23890,1)
d = round(828708/48583,1)

censo["Densidad"] = [c]+[d]
censo["Capital"] = ["Concepción"]+[" Puerto Montt"]
censo["Comunas"] = ["Lota, Lebu, Los Ángeles"]+["Castro, Puerto Varas, Purranque"]
censo["Provincia"] = ["Biobío, Arauco, Concepción"]+[" Osorno, Llanquihue, Chiloé, Palena"]
print("Censo:")
for clave, valor in censo.items():
    print(clave, ":", valor)
