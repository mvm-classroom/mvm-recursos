# Funció per Interians
def bloc_interia():
    resultat = ""

    #Interià
    print("Vosté s'ha identificat com a Interià")
    dia = input("Introdueix el nom del dia:")

    match dia:
        case "Dilluns":
            resultat = "Traducció: 1"
        case "Dimarts":
            resultat = "Traducció: 2"
        case "Dimecres":
            resultat = "Traducció: 3"
        case "Dijous":
            resultat = "Traducció: 4"
        case "Divendres":
            resultat = "Traducció: 5"
        case "Dissabte":
            resultat = "Traducció: 6"
        case "Diumenge":
            resultat = "Traducció: 7"
        case _:
            resultat = "No sé quin dia es aquest"

    return resultat

# Funció per Stringerians
def bloc_stringeria():
    resultat = ""

    #Stringerià
    print("Vosté s'ha identificat com a Stringerià")
    num_dia = int(input("Introdueix el dia de la setmana en nº:"))

    if num_dia == 1:
        resultat = "Traducció: Dilluns"
    elif num_dia == 2:
        resultat = "Traducció: Dimarts"
    elif num_dia == 3:
        resultat = "Traducció: Dimecres"
    elif num_dia == 4:
        resultat = "Traducció: Dijous"
    elif num_dia == 5:
        resultat = "Traducció: Divendres"
    elif num_dia == 6:
        resultat = "Traducció: Dissabte"
    elif num_dia == 7:
        resultat = "Traducció: Diumenge"
    else:
        resultat = "Nº de dia de la setmana incorrecte"

    return resultat


# Programa principal
especie = input("Es vosté Interià (I) o Stringerià (S)?: ")

if especie == "I":
    r = bloc_interia()
elif especie == "S":
    r = bloc_stringeria()
else:
    r = "ERROR: Espècie no reconeguda a la federació"

print(r)