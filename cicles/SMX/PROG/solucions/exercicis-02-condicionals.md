# Exercicis de classe 2: Estructures condicionals

Exercicis relacionats amb l'ús i comportament de les estructures condicionals

## Recursos d'interés:
- [If..else](https://www.w3schools.com/python/python_conditions.asp)
- [Match](https://www.w3schools.com/python/python_match.asp)

## Exercici 1: Parell o senar

Volem un programa que faci una tasca molt simple. Preguntar a l'usuari un número enter i nosaltres li direm si el número es parell o senar (imparell).

Un exemple del funcionament sería:

```shell
Introdueix un número: 10

El número 10 es parell
```

```shell
Introdueix un número: 3

El número 3 es senar
```

### Solució

```python
num = int(input("Introdueix un numero: "))

if num % 2 == 0:
  print("es par")
else :
  print("es impar")
```

## Exercici 2: Comparació de números

Qué pot passar quan comparem dos números `A` y `B`?

Independentment dels números introduits, podríem reduir les possibilitats a 3:
- `A` es **MÉS GRAN** que `B`
- `A` es **MÉS PETIT** que `B`
- `A` es **IGUAL** que `B`


Doncs partint d'aquesta premisa demanarem a l'usuari dos números i li donarem la resposta.

Per exemple:

```shell
----------------------------
Introdueix el número A: 10
Introdueix el número B: 11
----------------------------
A es MÉS PETIT que B
----------------------------
```

### Solució

```python
a = int(input("Introdueix el número A:"))
b = int(input("Introdueix el número B:"))

if a > b:
  print("A es MÉS GRAN que B")
else:
  if a < b:
    print("A es MÉS PETIT que B")
  else:
    print("A ES IGUAL que B")
```

## Exercici 3: Traductor de díes de la setmana

Hem començat a fer les pràctiques duals a la Federació Unida de Planetes, al departament de xenolingüistica. Ens han demanat un prototip senzill de traductor entre dues civilitzacions, els **Interians** i els **Stringerians**.

Resulta que els Interians només entenen els díes de la setmana com a **números enters**, mentre que els Stringerians només els entenen com a **cadenes de text**.

Ens han demanat varies versions:

### v1
El programa demana el dia de la setmana en un número enter i el tradueix al seu equivalent en text:

```shell
Día de la setmana: 5
Traducció: Divendres
```

### Solució

```python
num_dia = int(input("Introdueix el dia de la setmana en nº:"))

if num_dia == 1:
  print("Traducció: Dilluns")
elif num_dia == 2:
  print("Traducció: Dimarts")
elif num_dia == 3:
  print("Traducció: Dimecres")
elif num_dia == 4:
  print("Traducció: Dijous")
elif num_dia == 5:
  print("Traducció: Divendres")
elif num_dia == 6:
  print("Traducció: Dissabte")
elif num_dia == 7:
  print("Traducció: Diumenge")
else:
  print("Nº de dia de la setmana incorrecte")
```

### v2
El programa demana el dia de la setmana en una cadena de text i el tradueix al seu equivalent numéric:

```shell
Día de la setmana: Diumenge
Traducció: 7
```

### Solució 1

```python
dia = input("Introdueix el nom del dia:")
if dia == "Dilluns":
  print("Traducció: 1")
elif dia == "Dimarts":
  print("Traducció: 2")
elif dia == "Dimecres":
  print("Traducció: 3")
elif dia == "Dijous":
  print("Traducció: 4")
elif dia == "Divendres":
  print("Traducció: 5")
elif dia == "Dissabte":
  print("Traducció: 6")
elif dia == "Diumenge":
  print("Traducció: 7")
else:
  print("No sé quin dia es aquest")

```

### Solució 2

```python
#Versió fent servir match en comptes de if/elif/else
#https://www.w3schools.com/python/python_match.asp

dia = input("Introdueix el nom del dia:")

match dia:
  case "Dilluns":
    print("Traducció: 1")
  case "Dimarts":
    print("Traducció: 2")
  case "Dimecres":
    print("Traducció: 3")
  case "Dijous":
    print("Traducció: 4")
  case "Divendres":
    print("Traducció: 5")
  case "Dissabte":
    print("Traducció: 6")
  case "Diumenge":
    print("Traducció: 7")
  case _:
    print("No sé quin dia es aquest")
```

### versió final v3
El programa ens preguntarà si som Interians (`I`) o Stringerians (`S`) i directament ja ens mostrarà el format de traducció més adient.

```shell
------------------------------------------
Es vosté Interiá (I) o Stringeriá (S)?: I
------------------------------------------
Día de la setmana: Diumenge
Traducció: 7
------------------------------------------
```

```shell
------------------------------------------
Es vosté Interiá (I) o Stringeriá (S)?: S
------------------------------------------
Día de la setmana: 5
Traducció: Divendres
------------------------------------------
```

### Solució

```python
especie = input("Es vosté Interià (I) o Stringerià (S)?: ")
if especie == "I":
  #Interià
  print("Vosté s'ha identificat com a Interià")
  dia = input("Introdueix el nom del dia:")

  match dia:
    case "Dilluns":
      print("Traducció: 1")
    case "Dimarts":
      print("Traducció: 2")
    case "Dimecres":
      print("Traducció: 3")
    case "Dijous":
      print("Traducció: 4")
    case "Divendres":
      print("Traducció: 5")
    case "Dissabte":
      print("Traducció: 6")
    case "Diumenge":
      print("Traducció: 7")
    case _:
      print("No sé quin dia es aquest")

elif especie == "S":
  #Stringerià
  print("Vosté s'ha identificat com a Stringerià")
  num_dia = int(input("Introdueix el dia de la setmana en nº:"))

  if num_dia == 1:
    print("Traducció: Dilluns")
  elif num_dia == 2:
    print("Traducció: Dimarts")
  elif num_dia == 3:
    print("Traducció: Dimecres")
  elif num_dia == 4:
    print("Traducció: Dijous")
  elif num_dia == 5:
    print("Traducció: Divendres")
  elif num_dia == 6:
    print("Traducció: Dissabte")
  elif num_dia == 7:
    print("Traducció: Diumenge")
  else:
    print("Nº de dia de la setmana incorrecte")
else:
  print("ERROR: Espècie no reconeguda a la federació")
  #Error
```

## Exercici 4: Mantenint-nos hidratats (v2)

### v1

A 'Abdullah li encanta el ping-pong.

Com que es preocupa per la seva hidratació, beu 0,5 litres d'aigua per hora de ciclisme. El que passa es que només li agrada beure ampolles senceres d'un litre i no obre una si no arriba al mínim d'aigua que ha de beure.

Ens demanen que calculem els litres que s'han de beure en funció del temps jugant.

Per exemple:

```
temps = 1 ----> litres = 0

temps = 2 ----> litres = 1

temps = 3 ----> litres = 1

temps = 6,7---> litres = 3

temps = 11,8--> litres = 5
```

Necessitem que el programa faci el següent:
- Demani el temps (en `hores`) que s'ha estat fent exercici (per exemple `3` )
- Ens mostri un missatge com:
  ```shell
  Com has estat 3 hores fent exercici, has de beure 1 litre de líquid per mantenir-te en un bon nivell d hidratació
  ```
### v2

Alguns usuaris s'han queixat de que el text que mostrem en pantalla a vegades no es del tot correcte, com per exemple:

> Com has estat `1 hores` fent exercici, has de beure `0 litre` de líquid per mantenir-te en un bon nivell d hidratació

> Com has estat 6 hores fent exercici, has de beure `3 litre` de líquid per mantenir-te en un bon nivell d hidratació

Correcció necessaria:
- Hem de fer que, si el nº es `1` no faci servir el `plural` si no el `singular`

- Per exemple:
  ```shell
  Com has estat 1 hora fent exercici, has de beure 0 litres de liquid per mantenir-te en un bon nivell d hidratació
  ```

  ```shell
  Com has estat 6 hores fent exercici, has de beure 3 litres de liquid per mantenir-te en un bon nivell d hidratació
  ```

### Solució

```python
#Quantitat beguda  per hora d'exercici = 0,5 litres

import math

temps = float(input("Temps d'exercici: "))
litres_a_beure = temps * 0.5
litres_sencers = math.floor(litres_a_beure)

text_hores = "hores"
if temps == 1:
    text_hores = "hora"

text_litres = "litres"
if litres_sencers == 1:
    text_litres = "litre"

print("Com has estat", int(temps), text_hores,"fent exercici, has de beure",
      litres_sencers, text_litres, "de líquid per mantenir-te en un bon nivell d'hidratació")
```

## Exercici 5: Controlar stock de la botiga de pocions (v2)

### v1
Al poble de hi una botiga que només ven un tipus de producte, `pocions`.
Es una botiga molt exclusiva i només atén a 3 clients al dia.
El NPC que la gestiona ens ha demanat un programa que:

- Demani al principi de dia quin stock inicial de pocions tenim (per exemple `300` ).

- Demani quantes unitats ha comprat el client 1 (per exemple `30` )

- Demani quantes unitats ha comprat el client 2 (per exemple `5` )

- Demani quantes unitats ha comprat el client 3 (per exemple `15` )

- Mostri un resum final com aquest:
  ```shell
  Stock inicial: 300
  ------------------------
  Compra client 1: -30
  Compra client 2: -5
  Compra client 3: -15
  ------------------------
  Stock al final del dia: 250 pocions
  ```

### v2
Tornem a tenir notícies de l'NPC de la botiga. Ens diu que està fart d'apuntar comandes amb stock negatiu i que vol fer algunes modificacions:

  - Si ens quedem en stock 0, ja no acceptarem mes clients.
  - Si algún client ens demana més stock que el disponible només li podrem vendre el que queda i dir-li que torni demà.

  Per exemple:
  
  #### Exemple 1
  - Comencem el dia amb un stock de `300`
  - El primer client compra `200`
  - El segon client compra `100`
  - Com que no queda stock, ja no preguntem al tercer client.
  - Posem un missatge de "Pocions exhaurides. Torni demà"

  #### Exemple 2
  - Comencem el dia amb un stock de `300`
  - El primer client compra `200`
  - El segon client compra `200`
  - Com que no tenim suficient per satisfer la comanda del client, mostrarem un missatge `Només li puc vendre 100 unitats`
  - Posem un missatge de "Pocions exhaurides. Torni demà"`

### Solució

```python
stock_inicial = int(input("Stock inicial: "))
stock_restant = stock_inicial

# Compra client 1
quant_cli1 = int(input("Quantitat de pocions a comprar: "))

if (quant_cli1 > stock_restant):
    print("Només li puc vendre", stock_restant, "unitats")
    stock_restant = 0;
else:
    stock_restant = stock_restant - quant_cli1
    print("S'han comprat", quant_cli1, "unitats")

# Compra client 2
if (stock_restant > 0):
    quant_cli2 = int(input("Quantitat de pocions a comprar: "))

    if (quant_cli2 > stock_restant):
        print("Només li puc vendre", stock_restant, "unitats")
        stock_restant = 0;
    else:
        stock_restant = stock_restant - quant_cli2
        print("S'han comprat", quant_cli2, "unitats")
else:
    print("Pocions exhaurides, torni demà")

# Compra client 3
if (stock_restant > 0):
    quant_cli2 = int(input("Quantitat de pocions a comprar: "))

    if (quant_cli2 > stock_restant):
        print("Només li puc vendre", stock_restant, "unitats")
        stock_restant = 0;
    else:
        stock_restant = stock_restant - quant_cli2
        print("S'han comprat", quant_cli2, "unitats")
else:
    print("Pocions exhaurides, torni demà")
```

## Exercici 6: Calculadora bàsica

Hem de crear un programa que imiti, de manera molt bàsica, el funcionament d'una calculadora.

### v1

El programa ha de funcionar de la següent manera:

```shell
Introdueix operació a realitzar (+,-,*,/): +
Introudeix el primer nº: 1000
Introdueix el segon nº: 450
----------------------------------------------
1000 + 450 = 1450
----------------------------------------------
```

### Solució

```python
operacio = input("Introdueix operació:")
n1 = float(input("Introdueix n1:"))
n2 = float(input("Introdueix n2:"))
resultat = 0

match operacio:
    case "+":
        print("Ha seleccionat sumar")
        resultat = n1 + n2
    case "-":
        print("Ha seleccionat restar")
        resultat = n1 - n2
    case "*":
        print("Ha seleccionat multiplicar")
        resultat = n1 * n2
    case "/":
        print("Ha seleccionat dividir")
        resultat = n1 / n2

print("El resultat es:", resultat)
```

### v2

Hem de millorar la v1 per fer el següent:

- Si ens introdueixen un valor d'operació no esperat, donar un error y acabar el programa sense tan sols demanar els nº

- Si el primer o segon valor no son números, donarem un error y acabarem el programa sense fer cap càlcul

### Solució

```python
operacio = input("Introdueix operació: ")
#if operacio != "+" and operacio != "-" and operacio != "*" and operacio != "/":
if operacio not in "+-*/":
    #Error
    print("Error: Operació incorrecta")
else:
    #Operació be, demanem els numeros
    print("Operació correcta")
    n1 = input("Introdueix n1: ")
    n2 = input("Introdueix n2: ")

    if not(n1.isnumeric()) or not(n2.isnumeric()):
        #Error
        print("Error: només podem operar amb números")
    else:
        #Números correctes podem continuar
        n1 = float(n1)
        n2 = float(n2)
        print("Numeros correctes")

        resultat = 0
        #En aquest punt bifurquem el nostre codi en les 4 possibilitats
        match operacio:
            case "+":
                resultat = n1 + n2
            case "-":
                resultat = n1 - n2
            case "*":
                resultat = n1 * n2
            case "/":
                resultat = n1 / n2

        #Hora de mostrar el resultat
        print(n1, operacio, n2, "=", resultat)
```

