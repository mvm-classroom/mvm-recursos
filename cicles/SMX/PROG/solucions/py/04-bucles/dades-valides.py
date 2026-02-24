def es_codi_correcte(valor, min, max):
    es_correcte = False
    # Comprovem si el que ens han entrat es realment un número
    if not valor.isnumeric():
        # Si no es un número mostrem un error
        print(f"El valor introduït no es un número, només es permeten números del {min} al {max}")
    else:
        # Si es un número, comprovem que estigui entre els valors acceptats
        codi = int(valor)
        if codi < min or codi > max:
            # Si no està entre els valors acceptats, mostrem un error
            print(f"El valor introduït no es un codi vàlid [{min} - {max}]")
        else:
            es_correcte = True

    return es_correcte

def demana_valor(minim, maxim):
    valor_correcte = False

    while not valor_correcte:
        valor_usuari = input("Introdueix el codi de producte [101-118]: ")
        valor_correcte = es_codi_correcte(valor_usuari, minim, maxim)
                    

    return int(valor_usuari)


valor = demana_valor(101,118)
print(f"Ha escollit el producte amb el codi {valor}")