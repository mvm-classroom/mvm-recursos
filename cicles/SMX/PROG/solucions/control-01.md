# Solucions control de programació amb Python

## Exercici 4

```python
# Funció per demanar el simbol
def demanar_simbol():
    simbol = input("Simbol de la carta:")
    simbols_correctes = ["cors", "piques", "diamants", "trevols"]
    if simbol not in simbols_correctes:
        #El simbol es incorrecte i assignarem el valor per defecte
        print("El simbol es incorrecte, s'assignará 'cors'")
        simbol = "cors"
    return simbol

# Funció per demanar el valor
def demanar_valor():
    valor = input("Valor de la carta:")
    valors_correctes = "2345678910JQKA"
    if valor not in valors_correctes:
        #El valor es incorrecte i assignarem el valor per defecte
        print("El valor es incorrecte, s'assignará 'A'")
        valor = "A"

    match valor:
        case "A":
            valor = "as"
        case "K":
            valor = "rei"
        case "Q":
            valor = "reina"
        case "J":
            valor = "sota"

    return valor

def ajustar_article(valor):
    nou_article = "el"
    match valor:
        case "as":
            nou_article = "l'"
        case "reina":
            nou_article = "la"
        case "sota":
            nou_article = "la"
    
    return nou_article


# Programa per fer la resta que ens demanen

simbol_carta = demanar_simbol()
valor_carta = demanar_valor()
article = ajustar_article(valor_carta)

print("Has seleccionat", article, valor_carta, "de", simbol_carta)
```
