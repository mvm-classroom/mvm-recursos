# Fa el recorregut per una matriu N x M on N es un nº variable de files i M es un nº variable de columnes
# demanant tots els valors a l'usuari i retornant la matriu resultat al final
# N i M son definits a la crida de la funció en forma de paràmetres
def omplir_matriu(n, m):
    matriu = []

    for num_fila in range(n): # Farem N iteracions com files, per cada iteració crearem una fila buida i la omplirem amb M columnes
        fila = [] # Creem la fila buida
        for num_columna in range(m):
            # Demanem el valor a l'usuari            
            valor = int(input(f"Introdueix un nº per la posicio [{num_fila}][{num_columna}]:"))

            # L'afegim a la fila
            fila.append(valor)

        # Arribats a aquest punt, hem acabat el for per iterar columnes
        # La fila ja conté els valors de totes les columnes i la podem afegir a la matriu
        matriu.append(fila)

    # Arribats a aquest punt, hem acabat el for per iterar files, 
    # de manera que ja hem acabat tot el recorregut i podem retornar la matriu amb valors
    return matriu

def imprimir_matriu(matriu):
    files = len(matriu)
    for num_fila in range(files):
        columnes = len(matriu[num_fila])
        for num_columna in range(columnes):
            print(matriu[num_fila][num_columna])

def imprimir_matriu_claudators(matriu):
    files = len(matriu)
    for num_fila in range(files):
        fila_a_imprimir = ""
        columnes = len(matriu[num_fila])
        for num_columna in range(columnes):
            fila_a_imprimir += str(f"[{matriu[num_fila][num_columna]}]")

        print(fila_a_imprimir)    

matriu = omplir_matriu(4,3)
imprimir_matriu(matriu)
imprimir_matriu_claudators(matriu)