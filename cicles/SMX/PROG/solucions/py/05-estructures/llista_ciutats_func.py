

# Funció que demana noms de ciutat a l'usuari fins que escrigui PROU
def omplir_llista():
    nom_ciutat = ""
    llista = []

    while nom_ciutat != "PROU":
        nom_ciutat = input("Introdueix un nom de ciutat: ")
        if nom_ciutat != "PROU":
            llista.append(nom_ciutat)

    return llista

# Funció que demana a l'usuari com vol ordenar la llista
def ordenar_llista(llista):
    opcio_ordre = input("Vols llista ordenada en ascendent(A) o en descendent(Z): ")
    if opcio_ordre == "A":
        llista.sort()
    else:
        llista.sort(reverse=True)

def ajusta_linia(text, longitud):
    return text.ljust(longitud," ")+"│"

# Funció per imprimir la llista
def imprimir_llista(llista):
    LONGITUD_FILA = 45
    # Imprimim una capçalera fixaAAA
    print("┌────────────────────────────────────────────┐")
    print("│ CIUTATS                                    │")
    print("├────────────────────────────────────────────┤")
    
    # Imprimim cada ciutat de la llista
    for ciutat in llista:
        #print(f"│ {ciutat}".ljust(45," ")+"│")
        print(ajusta_linia(f"│ {ciutat}", LONGITUD_FILA))
        print("├────────────────────────────────────────────┤")

    # Imprimim el peu amb el total d'elements    
    #print(f"│ Total: {len(llista)} ciutats".ljust(45, " ") + "│")
    print(ajusta_linia(f"│ Total: {len(llista)} ciutats", LONGITUD_FILA))    
    print("└────────────────────────────────────────────┘")

llista_ciutats = omplir_llista()
ordenar_llista(llista_ciutats)
imprimir_llista(llista_ciutats)
