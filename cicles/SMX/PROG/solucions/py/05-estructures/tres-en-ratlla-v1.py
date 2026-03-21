from colors import valor_amb_color

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
            valor = matriu[fila][columna]
            fila_a_imprimir += str(f"[{valor_amb_color(valor)}]")

        print(fila_a_imprimir)

def es_numero_valid(valor, min, max):
    es_valid = True

    if not valor.isnumeric():
        es_valid = False
    else:
        numero = int(valor)
        if numero < min or numero > max:
            es_valid = False

    return es_valid

def obtenir_fila(min, max):
    valor = input(f"Fila[{min}-{max}]: ")            
    while not es_numero_valid(valor, min, max): # Mentre el valor no sigui un nº o no sigui un nº valid, tornem a preguntar
        valor = input(f"Fila[{min}-{max}]: ")

    fila = int(valor) # Arribats a aquest punt estem segurs de que es un numero i podem fer int() sense por
    return fila

def obtenir_columna(min, max):
    columna = int(input(f"Columna[{min}-{max}]: "))
    while columna < min or columna > max:
        columna = int(input(f"Columna[{min}-{max}]: "))
    return columna

def es_valor_valid(valor):
    es_valid = True
    if valor.startswith("-"):
        return es_valid
    else:
        if valor != "x" and valor !="o" and valor !="stop":
            es_valid = False

    return es_valid

def obtenir_valor():
    valor = input("Valor [x/o]: ").lower()
    while not es_valor_valid(valor):
        valor = input("Valor [x/o]: ").lower()

    if valor.startswith("-"):
        valor = " "

    return valor

def afegir_valor(matriu):
    continuar = True

    fila = obtenir_fila(0,2)
    columna = obtenir_columna(0,2)
    valor = obtenir_valor()        

    if valor == "stop":
        continuar = False
    else:
        if matriu[fila][columna] == " " or valor == " ": # Si la posició està buida o ens han passat eliminar el valor
            matriu[fila][columna] = valor # Assignem el valor
        else: # Si la posició no està buida
            print(f"La posició[{fila}][{columna}] ja te un valor") # Mostrem error i no fem res, pero permetem continuar 

    return continuar


def comprovar_files(matriu):
    guanyador = "" # Per defecte no guanya ningú
    for fila in matriu:
        if fila[0] == fila[1] == fila[2] and fila[0] != " ": # Si els tres valors de la fila son iguals
            guanyador = fila[0] # Retornem el primer valor (encara que donaria igual retornar el segon o tercer)

    return guanyador

def comprovar_columnes(matriu):
    guanyador = "" # Per defecte no guanya ningú
    for col in range(3):
        #Comparem el mateix index de columna a diferents files
        if matriu[0][col] == matriu[1][col] == matriu[2][col] and matriu[0][col] != " ":
            guanyador = matriu[0][col]

    return guanyador

def comprovar_diagonals(matriu):
    guanyador = ""
    #Comprovem la diagonal principal (de [0][0] a [2][2])
    if matriu[0][0] == matriu[1][1] == matriu[2][2] and matriu[0][0] != " ":
        return matriu[0][0]

    #Comprovem la diagonal principal (de [2][0] a [0][2])
    if matriu[0][2] == matriu[1][1] == matriu[2][0] and matriu[0][2] != " ":
        return matriu[0][2]
    return guanyador

def comprovar_guanyador(matriu):
    guanyador = "" # Per defecte no guanya ningú

    guanyador = comprovar_files(matriu)
    if guanyador != "": # Si al comprovar les files hem trobat guanyador        
        return guanyador # El retornem directament, no cal fer més comprovacions

    guanyador = comprovar_columnes(matriu)
    if guanyador != "": # Si al comprovar les columnes hem trobat guanyador
        return guanyador # El retornem directament, no cal fer més comprovacions
    
    guanyador = comprovar_diagonals(matriu)        
    # Si revisem tot, retornem guanyador com estigui, tindrà "", "x" o "o"    
    return guanyador



# Programa principal
matriu = []
omplir_matriu(matriu)
imprimir_matriu(matriu)
continuar = True

while continuar == True:
    continuar = afegir_valor(matriu)        
    imprimir_matriu(matriu)
    resultat = comprovar_guanyador(matriu)
    if resultat != "":
        print(f"Ha guanyat {resultat}")
        continuar = False
