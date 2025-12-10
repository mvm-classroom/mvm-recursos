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

## Exercici 3
Crea una funció anomenada `son_iguals` que rebi dos paraules `paraula1` i `paraula2`. La funció ha de retornar si les paraules son iguals sense tenir en compte les majúscules.
Crea un programa que demani a l’usuari dues paraules, faci servir la funció i, finalment, retorni un missatge indicant si les paraules son iguals o no

### Exemples d'execució

```shell
Introduir paraula 1: PROVA
Introduir paraula 2: prova
Les paraules PROVA i prova son iguals
```
```shell
Introduir paraula 1: prova
Introduir paraula 2: prueba
Les paraules prova i prueba no son iguals
```

### Exemple de resolució

```python
def son_iguals(paraula1, paraula2):
    if (paraula1.lower() == paraula2.lower()):
        #Son iguales
        return True
    else:
        #Son distintas
        return False


p1 = input("Paraula 1:")
p2 = input("Paraula 2:")

#iguals = son_iguals(p1, p2)
text_igual = "son iguals"
if (not son_iguals(p1, p2)):
    text_igual = "no son iguals"
    
print("Les paraules", p1, "i", p2, text_igual)

# if (son_iguals(p1, p2)):
#     #Mensaje que son iguales
#     print("Les paraules", p1, "i", p2, "son iguals")
# else:
#     #Mensaje que son diferentes
#     print("Les paraules", p1, "i", p2, "no son iguals")
```

## Exercici 4

Crea un programa que faci el següent:

Demani, **fent servir una funció**, a l’usuari escollir primer el símbol de la carta (cors, piques, trèvols o diamants). Si s’informa un valor incorrecte, informar a l’usuari i assignar **cors** com el valor per defecte. Per exemple: `El símbol seleccionat no és correcte, s’assignarà Cors.`

Demani, **fent servir una funció**,  el valor de la carta (els valors vàlids son 2,3,4,5,6,7,8,9,10,J,Q,K,A). Si s’informa un valor incorrecte, informar a l’usuari i assignar A com el valor per defecte. Per exemple: `El valor seleccionat no es correcte, s’assignarà A.`

En funció del que l’usuari ha escollit en cadascuna de les preguntes, mostrar un missatge informant de la seva elecció. Per exemple: `Ha seleccionat el 2 de piques.`

Millora no obligatòria pero que es valorarà positivament: Si l’usuari escull com valor una de les lletres A, J, Q, K, mostrar el missatges com els següents:
- `Ha seleccionat l’as de piques`
- `Ha seleccionat la sota de cors`
- `Ha seleccionat la reina de trèvols`
- `Ha seleccionat el rei de diamants`


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
