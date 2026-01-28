# Exercicis de classe 4: Bucles

Exercicis relacionats amb l'us de bucles

## Exercici 1: Compte enrere
Crea un programa per fer un compte enrere.

Hem de demanar a l'usuari quants segons vol que duri el compte enrere i després mostrar el compte amb un "JA!" al final.

Exemple
```text
Quants segons vols que duri el compte enrere?: 5
5
4
3
2
1
JA!
```
### Solució amb `for`
```python
import time

numero = int(input("Quants segons vols que duri el compte enrere?: "))

for i in range(numero, 0, -1):
    print(i)
    time.sleep(1)  # Espera 1 segon

print("¡JA!")
```

### Solució amb `while`

```python
import time

numero = int(input("Quants segons vols que duri el compte enrere?: "))

while numero > 0 :
    print(numero)    
    time.sleep(1)  # Espera 1 segon
    numero -= 1

print("¡JA!")
```


## Exercici 2: Endevina el nº secret

Crea un joc per endevinar un nº aleatori que canviarà en cada execució.

El programa ha d'anar demanant nº a l'usuari i indicar si es més gran o més petit que el nº a endevinar.

En el moment que endevini el nº exacte ha de notificar a l'usuari que ha encertat i en quants intents ho ha fet.

Exemple

```text
Endevina el nº entre 1 i 100
Nº: 50
El teu nº es més petit que el secret
Nº: 100
El teu nº es més gran que el secret
Nº: 75
El teu nº es més gran que el secret
Nº: 60
Correcte! L'has endevinat en 4 intents
```

### Solució

```python
import random

num_secret = random.randint(1, 100)
intents = 0
endevinat = False

print("Endevina el nº entre 1 i 100")

while not endevinat:
    num_usuari = int(input("Nº: "))
    intents += 1
    
    if num_usuari < num_secret:
        print("El teu nº es més petit que el secret")
    elif num_usuari > num_secret:
        print("El teu nº es més gran que el secret")
    else:
        endevinat = True
        print(f"Correcte! L'has endevinat en {intents} intents")
```

## Exercici 3: Funció per controlar dades vàlides

Tenim una màquina de vending on s'ha d'indicar el nº de producte que volem comprar abans de posar-hi les monedes.

Hem de fer una funció que s'encarregarà de demanar les dades a l'usuari verificant que son dades vàlides. Si no ho son, ho farem saber a l'usuari i li tornarem a demanar.

Els codis de producte vàlids van des del `101` al `118`.

Hem de verificar que:
- L'usuari entra realment un nº i no pas text
- El nº es un dels valors permesos

### Solució

```python
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
```

