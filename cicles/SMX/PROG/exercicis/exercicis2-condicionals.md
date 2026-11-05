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

### v1
El programa demana el dia de la setmana en un número enter i el tradueix al seu equivalent en text:

```shell
Día de la setmana: 5
Traducció: Divendres
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


