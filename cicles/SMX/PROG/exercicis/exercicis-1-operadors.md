# Exercicis de classe 1: Operadors

Exercicis relacionats amb l'ús i comportament d'operadors

## Exercici 1: Calculadora de propina

Hem anat a sopar a un restaurant nou que han instal.lat unes taules amb una pantalla táctil per veure el menú i fer comandes.

Parlant amb un cambrer (que resulta ser també el propietari) et comenta que estaría molt bé fer tenir una calculadora de propines integrada, pero que ell no sap programar.

Com per tú es un codi relativament senzill t'ofereixes a fer-li un cop de mà amb un prototip molt bàsic.


El que ha de fer es el següent:
>- Demanar l'import inicial ( per exemple `200` )
>- Demanar el % de propina ( per exemple `10` )
>- Calcular la propina
>- Mostrar un resum d'aquest estil:
>
>  ```shell
>  Import inicial: 200€
>  Propina (10%): 20€
>  ---------------------
>  Total a pagar: 220€
>  ```

## Exercici 2: Controlar stock de la botiga de pocions

Al poble de hi una botiga que només ven un tipus de producte, `pocions`.
Es una botiga molt exclusiva i només atén a 3 clients al dia.
El NPC que la gestiona ens ha demanat un programa que:

- Demani al principi de dia quin stock inicial de pocions tenim (per exemple `300` ).

- Demani quantes unitats ha comprat el client 1 (per exemple `30` )
- Mostri quantes pocions queden després de la compra

- Demani quantes unitats ha comprat el client 2 (per exemple `5` )
- Mostri quantes pocions queden després de la compra

- Demani quantes unitats ha comprat el client 3 (per exemple `15` )
- Mostri quantes pocions queden després de la compra

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

## Exercici 3: Aficionats a la aviació

Un grup d'amics aficionats a l'aviació volen un petit programa que calculi la distància recorreguda per una aeronau en base a les dades que els hi han passat en un fitxer.

Per cada viatge sempre coneixem dues dades:
- La velocitat (en nusos)
- El temps de vol (en minuts)

Necessitem que el programa faci el següent:
- Demanar la velocitat (per exemple `100` )
- Demanar el temps de vol (per exemple `120` )
- Ens mostri un resultat com:
  ```shell
  La nostra aeronau ha viatjat durant 120 minuts a 100 nusos, de manera que ha recorregut 370,4 Km
  ```

## Exercici 4: Mantenint-nos hidratats

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

## Exercici 5: Mentalitat de *Toblerone*

L'Àngel ha estat uns dies de vacanes i, just abans de tornar, ha vist que a la botiga *duty free* de l'aeroport, venen *Toblerones* amb un bon descompte. Ha tingut, segons ell, una idea genial. Comprarà els *Toblerones* amb descompte per revendre després i recuperar el que s'ha gastat a les vacances.

Al marge de si ens sembla realment una bona idea, i dels problemes legals que pot comportar, farem un petit programa per calcular quants *Toblerones* hem de revendre per recuperar les despeses de les vacances.

El nostre programa ha de demanar el següent:
- El preu actual del *Toblerone* (per exemple, `10`€)
- El % de descompte actual del *Toblerone* (per exemple, `20`%)
- L'import de les despeses de les vacances (per exemple, `1000`€)

Ha de fer els càlculs necessaris per donar un resultat com:
```shell
--------------------------------------------------------------------------------
Preu per unitat: 10€
Descompte per cada unitat: 20%
Benefici per unitat: 2€
Despeses de les nostres vacances: 1000€
--------------------------------------------------------------------------------
Nº de Toblerones que hem de comprar i revendre per amortitzar les vacances: 500
--------------------------------------------------------------------------------
```
  
