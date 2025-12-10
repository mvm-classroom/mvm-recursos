# Solucions control de programació amb Python

## Exercici 1
Escriu una funció que rebi dos nombres decimals i retorni el màxim dels dos.
Escriu una funció que calculi l'àrea d'un triangle. 
Completa el programa per que calculi l'àrea d'un triangle de base 4 i altura 8, i l'àrea d'un triangle de base 6 i altura 6. El programa ha d'usar les funcions definides però no fa falta demanar les dades interactivament a l'usuari, ja que els valors seran sempre els mateixos.

>[!NOTE]
>L'àrea d'un triangle partint de la seva base (`b`) i altura (`h`) es calcula com
`a = (b * h) / 2`

### Funció per calcular el màxim de dos nº
```python
def max_de_2(num1,num2):
    if num1 > num2:
        return num1
    else
        return num2
```
### Funció per calcular l'àrea d'un triangle
```python
def area_triangle(num1, num2):
    return (num1 * num2) / 2
```
### Programa que fa servir les funcions definides
```python
area1 = area_triangle(4, 8)
area2 = area_triangle(6, 6)
maxim = max_de_2(area1, area2)
print (“L’àrea màxima es”,maxim)
```

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
