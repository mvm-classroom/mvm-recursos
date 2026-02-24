# Fa el recorregut per una matriu de 3x3 demanant valors a l'usuari
def omplir_matriu_3x3(matriu):
    for num_fila in range(3): # Farem 3 iteracions, una per cada fila
        fila = [] # Creem la fila buida
        for num_columna in range(3): # A cada fila, farem 3 iteracions més, una per cada columna
            # Demanem el valor a l'usuari            
            valor = int(input(f"Introdueix un nº per la posicio [{num_fila}][{num_columna}]:"))

            # L'afegim a la fila
            fila.append(valor)
        
        # En acabar aquest for, hem afegit 3 elements a fila i ara afegim la fila a la matriu
        matriu.append(fila)

    # En acabar aquest for, hem afegit 3 files a la matriu

    # Resum: Hem afegit 3 files amb 3 elements a cada fila

def imprimir_matriu_3x3_seguit(matriu):
    for fila in range(3):
        for columna in range(3):
            print(matriu[fila][columna])

def imprimir_matriu_3x3_tres_files(matriu):
    for fila in range(3):
        fila_a_imprimir = ""
        for columna in range(3):
            fila_a_imprimir += str(matriu[fila][columna])

        print(fila_a_imprimir)

def imprimir_matriu_3x3_tres_files_coma(matriu):
    for fila in range(3):
        fila_a_imprimir = ""
        for columna in range(3):
            fila_a_imprimir += str(matriu[fila][columna]) + ","

        print(fila_a_imprimir)

def imprimir_matriu_3x3_tres_files_espai(matriu):
    for fila in range(3):
        fila_a_imprimir = ""
        for columna in range(3):
            fila_a_imprimir += str(matriu[fila][columna]) + " "

        print(fila_a_imprimir)

def imprimir_matriu_3x3_claudators(matriu):
    for fila in range(3):
        fila_a_imprimir = ""
        for columna in range(3):
            fila_a_imprimir += str(f"[{matriu[fila][columna]}]")

        print(fila_a_imprimir)    

matriu = []
omplir_matriu_3x3(matriu)

print("")
print("Matriu impresa tot seguit")
imprimir_matriu_3x3_seguit(matriu)

print("")
print("Matriu impresa en tres files")
imprimir_matriu_3x3_tres_files(matriu)

print("")
print("Matriu impresa en tres files, valors separats per coma")
imprimir_matriu_3x3_tres_files_coma(matriu)

print("")
print("Matriu impresa en tres files, valors separats per espai")
imprimir_matriu_3x3_tres_files_espai(matriu)

print("")
print("Matriu impresa en format graella 3x3 amb claudàtors")
imprimir_matriu_3x3_claudators(matriu)
