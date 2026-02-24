def bloc_interia():
    #Interià
    print("Vosté s'ha identificat com a Interià")
    dia = input("Introdueix el nom del dia:")
    text_a_mostrar = "..."

    match dia:
        case "Dilluns":
            text_a_mostrar = "Traducció: 1"
        case "Dimarts":
            text_a_mostrar = "Traducció: 2"
        case "Dimecres":
            text_a_mostrar = "Traducció: 3"
        case "Dijous":
            text_a_mostrar = "Traducció: 4"
        case "Divendres":
            text_a_mostrar = "Traducció: 5"
        case "Dissabte":
            text_a_mostrar = "Traducció: 6"
        case "Diumenge":
            text_a_mostrar = "Traducció: 7"
        case _:
            text_a_mostrar = "No sé quin dia es aquest"

    return text_a_mostrar

def bloc_stringeria():
    #Stringerià
    print("Vosté s'ha identificat com a Stringerià")
    num_dia = int(input("Introdueix el dia de la setmana en nº:"))

    if num_dia == 1:
        return "Traducció: Dilluns"
    elif num_dia == 2:
        return "Traducció: Dimarts"
    elif num_dia == 3:
        return "Traducció: Dimecres"
    elif num_dia == 4:
        return "Traducció: Dijous"
    elif num_dia == 5:
        return "Traducció: Divendres"
    elif num_dia == 6:
        return "Traducció: Dissabte"
    elif num_dia == 7:
        return "Traducció: Diumenge"
    else:
        return "Nº de dia de la setmana incorrecte"


# Programa principal
especie = input("Es vosté Interià (I) o Stringerià (S)?: ")
#text_a_mostrar = ""
if especie == "I":
    text_a_mostrar = bloc_interia()
elif especie == "S":
    text_a_mostrar = bloc_stringeria()
else:
    text_a_mostrar = "ERROR: Espècie no reconeguda a la federació"


print("Resultat:", text_a_mostrar)