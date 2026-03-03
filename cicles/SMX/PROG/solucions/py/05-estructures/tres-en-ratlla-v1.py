# En aquesta primera versió només farem dues tasques:
# - Demanar valors a l'usuari
# - Pintar la matriu després de cada valor

# Funció per omplir la matriu de caracters en blanc " "
# He aprofitat la funció de l'anterior exercici i l'he modificat només una mica
def omplir_matriu(matriu):
    for num_fila in range(3): # Farem 3 iteracions, una per cada fila
        fila = [] # Creem la fila buida
        for num_columna in range(3): # A cada fila, farem 3 iteracions més, una per cada columna            
            # L'afegim a la fila
            fila.append(" ") # En tots els casos posarem un valor en blanc
        
        # En acabar aquest for, hem afegit 3 elements a fila i ara afegim la fila a la matriu
        matriu.append(fila)

    # En acabar aquest for, hem afegit 3 files a la matriu

    # Resum: Hem afegit 3 files amb 3 elements a cada fila

# Funció per imprimir la matriu, tingui el que tingui dins
# He aprofitat la funció 'imprimir_matriu_3x3_claudators'
def imprimir_matriu(matriu):
    for fila in range(3):
        fila_a_imprimir = ""
        for columna in range(3):
            fila_a_imprimir += str(f"[{matriu[fila][columna]}]")

        print(fila_a_imprimir)


def obtenir_fila():
    fila = int(input("Fila: "))
    return fila

def obtenir_columna():
    columna = int(input("Columna: "))
    return columna

def obtenir_valor():
    valor = input("Valor: ")
    return valor

def afegir_valor(matriu):
    continuar = True

    fila = obtenir_fila()
    columna = obtenir_columna()
    valor = obtenir_valor()
    
    if valor == "STOP":
        continuar = False
    else:
        matriu[fila][columna] = valor

    return continuar



# Programa principal
matriu = []
omplir_matriu(matriu)
imprimir_matriu(matriu)
continuar = True

while continuar == True:
    continuar = afegir_valor(matriu)        
    imprimir_matriu(matriu)
