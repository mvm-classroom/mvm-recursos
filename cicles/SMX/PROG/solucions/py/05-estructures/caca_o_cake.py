import random

def caca_o_cake():    
    valor_aleatori = random.choice(["💩","🎂"])
    return valor_aleatori

def omplir_matriu_4x4():
    matriu = []

    for num_fila in range(4): 
        fila = [] # Creem la fila buida
        for num_columna in range(4): # A cada fila, farem 4 iteracions més, una per cada columna
            # Obtenim el valor aleatori de la funció caca_o_cake()
            valor = caca_o_cake()

            # L'afegim a la fila
            fila.append(valor)
        
        # En acabar aquest for, hem afegit 3 elements a fila i ara afegim la fila a la matriu
        matriu.append(fila)


    return matriu

def imprimir_matriu_4x4_espai(matriu):
    for fila in range(4):
        fila_a_imprimir = ""
        for columna in range(4):
            fila_a_imprimir += str(matriu[fila][columna]) + " "
        print(fila_a_imprimir)
    

#matriu = omplir_matriu_4x4()
#imprimir_matriu_4x4_espai(matriu)

imprimir_matriu_4x4_espai(omplir_matriu_4x4())