print("Pots afegir tants noms de ciutat com vulguis. Escriu PROU per finalitzar")
nom_ciutat = ""
llista_ciutats = []

while nom_ciutat != "PROU":
    nom_ciutat = input("Introdueix un nom de ciutat: ")
    if nom_ciutat != "PROU":
        llista_ciutats.append(nom_ciutat)

llista_ciutats.sort()

for ciutat in llista_ciutats:
    print(ciutat)
